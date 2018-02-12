import sublime
import sublime_plugin
import re

# Commentate command for ESDoc style JavaScript comments.
# Tested extensively using SublimeText3 console and view.run_command('commentate_esdoc'); the name is (so far?) auto
# generated based on the class name. Note that the class must end with "Command" per ST3 plugin API requirements.
class CommentateEsdocCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    indentRegex = re.compile('\s*(?=\S)')

    # https://stackoverflow.com/questions/30115649/get-current-line-in-sublime-text-3-plugin -
    # self.view.sel() gets the array of selected regions tracked on the view.
    # self.view.line(*) gets the line (or lines?) within the specified region.
    #   The value is returned as the starting and ending indices of the line.
    # self.view.substr(*) gets the substring corresponding to those indices.
    commenteeLine = view.line(view.sel()[0])
    commenteeText = view.substr(commenteeLine)

    indentMatch = indentRegex.match(commenteeText)
    if indentMatch:
      indentEnd = indentMatch.end()
      indent = ' ' * indentEnd
    else:
      indentEnd = 0
      indent = ''

    name = commenteeText[indentEnd:commenteeText.find('(')].split(' ')[-1]

    args = []
    for arg in commenteeText[commenteeText.find('(') + 1:commenteeText.find(')')].split(','):
      args.append(arg.strip().split('=')[0].strip())

    commentText    = indent + '/**' + '\n'
    commentText   += indent + ' * ' + name + '\n'
    for arg in args:
      commentText += indent + ' * @param {*} ' + arg + '\n'
    commentText   += indent + ' */' + '\n'

    self.view.insert(edit, commenteeLine.begin(), commentText)
