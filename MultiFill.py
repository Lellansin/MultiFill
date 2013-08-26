
import sublime
import sublime_plugin
import random
import string

#
#   inner function
#


def nums(i):
    return str(i)


def nums2(i):
    return str(i + 1)


def upAlphabet(i):
    return chr(i + 65)


def lwAlphabet(i):
    return chr(i + 97)

func = [nums, nums2, upAlphabet, lwAlphabet]


def userCustom(order, data, length, pos):
    if (order == 'ordered'):
        if pos >= length:
            pos %= length
        return data[pos]
    elif (order == 'random'):
        return data[random.randint(0, length - 1)]


#
#   text insert part
#

def getList():
    return ['Numbers since 0 (Ordered)', 'Numbers since 1 (Ordered)', 'Uppercase letters (Ordered)', 'Lower case letters (Ordered)']


class MultiFillSetTextCommand(sublime_plugin.TextCommand):

    def run(self, edit, **args):

        chosen = args.get('chosen')
        if (chosen > len(func) - 1):
            # custom fill
            custom = args.get("custom")
            item = custom[chosen - len(func)]
            points = self.view.sel()
            count = len(points)
            for i in range(0, count):
                self.view.replace(edit, points[i], userCustom(
                    item['way'], item["values"], len(item["values"]), i))
        else:
            points = self.view.sel()
            count = len(points)
            for i in range(0, count):
                self.view.replace(edit, points[i], func[chosen](i))

#
#   select panel
#


class MultiFillCommand(sublime_plugin.WindowCommand):

    def run(self):
        # get the fill list
        self.command_list = getList() + self.get_custom()
        if not self.command_list:
            echo('There may be some error with the config file.')
            return
        # call the panel
        self.window.show_quick_panel(self.command_list, self.on_done)

    def get_custom(self):
        # get the custom list from the config file
        self.settings = sublime.load_settings('MultiFill.sublime-settings')
        custom = self.settings.get("custom")
        result = []
        for i in range(0, len(custom)):
            result += [custom[i]["name"]]
        return result

    def on_done(self, index):
        if (index == -1):
            return
        # call the text fill
        view = sublime.active_window().active_view()
        if view:
            view.run_command('multi_fill_set_text', {'chosen': index, 'custom': self.settings.get("custom")})


#
#   formula insert part
#
class MultiIntegerSetTextCommand(sublime_plugin.TextCommand):

    def run(self, edit, **args):
        text = args.get('formula')
        points = self.view.sel()
        count = len(points)
        for x in range(0, count):
            try:
                self.view.replace(edit, points[x], str(eval(text)))
            except:
                echo("Sorry! Parse error, MultiFill dose not support pure math-like formula yet.")
                return


#
#   formula input
#

def isDigit(c):
    if c not in string.digits:
        return False
    else:
        return True

class MultiIntegerCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel("Multi Integer formula: ", "y = ", self.on_done, None, None)

    def on_done(self, text):
        text = text.replace(" ", "").replace("y=", "")
        flag = 1
        deal = []
        for i in xrange(0, len(text)):
            if text[i] == 'x':
                flag = 0
                if i > 0 and isDigit(text[i - 1]):
                    deal.append('*')
                deal.append('x')
            elif text[i] == '(':
                if i > 0 and isDigit(text[i - 1]):
                    deal.append('*')
                deal.append('(')
            else:
                deal.append(text[i])
        if flag:
            echo("You should type the independent variable 'x' in the formula.")
            return
        deal = str(''.join(deal))
        echo(deal)
        # call the formula text fill
        view = sublime.active_window().active_view()
        if view:
            view.run_command('multi_integer_set_text', {'formula': deal})


#
#   debug
#
def echo(message):
    sublime.message_dialog(message)
