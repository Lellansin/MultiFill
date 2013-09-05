
import sublime
import sublime_plugin

class MultiSelectCommand(sublime_plugin.WindowCommand):
    points = {};
    def run(self, **args):
        view = self.window.active_view();
        view_id = view.id();
        points_new = list(view.sel());

        # if it's the first
        if ( not view_id in MultiSelectCommand.points ):
            # first save
            MultiSelectCommand.points.setdefault(view_id, points_new);
        else:
            # judge if it's too many points
            saved_num = len(MultiSelectCommand.points[view_id])
            to_saved = len(points_new)
            settings = sublime.load_settings('MultiFill.sublime-settings')
            limit = settings.get('multi_select_limit')
            if ((saved_num + to_saved) > limit):
                echo('There are to many points and selections saved and this may case some problem. If you trust the performance of you CPU and RAM, you can change the limit of the MultiFill config file')
                return
            # save new points
            MultiSelectCommand.points[view_id][0:0] = points_new;

        # mark all the points saved
        mark = [s for s in points_new]
        view.add_regions("mark", MultiSelectCommand.points[view_id], "mark", "dot",
            sublime.HIDDEN | sublime.PERSISTENT)


class MultiSelectAllCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        view_id = self.view.id();

        if ( not view_id in MultiSelectCommand.points ):
            return

        # get points data
        points = MultiSelectCommand.points[view_id] 

        # restore all the points and selections
        count = len(points)
        for i in range(0, count):
            self.view.sel().add(points[i])

        # clear the mark
        self.view.add_regions("mark", [s for s in points], "", "", sublime.HIDDEN | sublime.PERSISTENT)
        # clear the data
        del MultiSelectCommand.points[view_id]


class MultiSelectLastCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        points = self.view.sel();
        num_sel = len(points);        
        if (num_sel < 2):
            return 
        last_points = points[-1];
        # clear all
        self.view.sel().clear()
        # add last
        self.view.sel().add(last_points)

#
#   debug
#
def echo(message):
    sublime.message_dialog(message)