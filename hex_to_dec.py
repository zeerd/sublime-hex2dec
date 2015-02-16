import sublime, sublime_plugin

class HexToDecCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		i = int(self.view.substr(self.view.sel()[0]), 16)
		self.view.replace(edit, self.view.sel()[0], str(i))
