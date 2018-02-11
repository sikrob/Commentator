import sublime
import sublime_plugin

# A lot of this is likely to be cobbled together from StackOverflow or otherwise be pretty messy.
# Haven't had a lot of practice with Python in the past year+, but let's see what happens.
class CommentateEsdocCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print(edit)

    print(self.view.substr(self.view.line(self.view.sel()[0])))
    self.view.insert(edit, 1, "Hello, World!")
