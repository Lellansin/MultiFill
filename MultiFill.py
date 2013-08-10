
import sublime
import sublime_plugin
import os
import random

#
#	inner function
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
# 	text insert part
#

def getList():
    return ['Numbers since 0 (Ordered)', 'Numbers since 1 (Ordered)', 'Uppercase letters (Ordered)', 'Lower case letters (Ordered)' ];


class MultiFillSetTextCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        global func
        # get the chonsen index from the tmp file ( wait a better way? )
        tmp_settings = sublime.load_settings('MultiFill.tmp')
        chosen = tmp_settings.get('chosen')

        if (chosen > len(func) - 1):
            # custom fill
            global settings
            custom = settings.get("custom")
            item = custom[chosen - len(func)]
            points = self.view.sel()
            count = len(points)
            for i in xrange(0, count):
                # echo(str(len(item["values"])));
                self.view.replace(edit, points[i], userCustom(
                    item['way'], item["values"], len(item["values"]), i))
        else:
            points = self.view.sel()
            count = len(points)
            for i in xrange(0, count):
                self.view.replace(edit, points[i], func[chosen](i))

#
#	select panel
#


def getCustom():
    # get the custom list from the config file
    global settings
    settings = sublime.load_settings('MultiFill.sublime-settings')
    custom = settings.get("custom")
    result = []
    for i in xrange(0, len(custom)):
        result += [custom[i]["name"]];
    return result


class MultiFillCommand(sublime_plugin.WindowCommand):

    def run(self):
        # get the fill list
        self.command_list = getList() + getCustom();
        if not self.command_list:
            echo('There may be some error with the config file.')
            return
        # call the panel
        self.window.show_quick_panel(self.command_list, self.on_done)

    def on_done(self, index):
        if (index == -1):
            return
        # mark the index user choose ( this may be a bad way :( )
        settings = sublime.load_settings('MultiFill.tmp')
        settings.set('chosen', index)
        c = settings.get('chosen')
        sublime.save_settings('MultiFill.tmp')

        # call the text fill
        view = sublime.active_window().active_view()
        if view:
            view.run_command('multi_fill_set_text')

#
# 	debug
#


def echo(str):
    sublime.message_dialog(str);
