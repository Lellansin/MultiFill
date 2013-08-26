
import sublime
import sublime_plugin
import random

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
            view.run_command('multi_fill_set_text', {'chosen':index, 'custom': self.settings.get("custom")})


#
#   debug
#


def echo(message):
    sublime.message_dialog(message)
