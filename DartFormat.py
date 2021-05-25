import os.path
import sublime
import sublime_plugin
import subprocess

SETTINGS_FILE = "DartFormat.sublime-settings"

class DartFormatOnSave(sublime_plugin.EventListener):

    def on_post_save(self, view):
        if sublime.load_settings(SETTINGS_FILE).get("run_on_save", False):
            return view.run_command("dart_format")
        return


class DartFormatCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        if not self.is_dart():
            return

        filename = self.view.file_name()
        settings = sublime.load_settings(SETTINGS_FILE)
        dart_bin = settings.get("dart", "dart")

        cmd = [dart_bin, "format"] + settings.get("args", []) + [filename]
        cwd = os.path.dirname(filename)

        self.save_viewport_state()

        proc = subprocess.Popen(cmd, cwd=cwd)
        proc.wait()

        self.view.window().run_command("reload_all_files")
        self.reset_viewport_state()

    def is_dart(self):
        return 'source.dart' in self.view.scope_name(0)

    def save_viewport_state(self):
        self.previous_selection = [(region.a, region.b)
                                   for region in self.view.sel()]
        self.previous_position = self.view.viewport_position()

    def reset_viewport_state(self):
        self.view.set_viewport_position((0, 0,), False)
        self.view.set_viewport_position(self.previous_position, False)
        self.view.sel().clear()
        for a, b in self.previous_selection:
            self.view.sel().add(sublime.Region(a, b))
