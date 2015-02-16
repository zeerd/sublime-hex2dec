import sublime, sublime_plugin

class DecToHexCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		i = int(self.view.substr(self.view.sel()[0]))
		self.view.replace(edit, self.view.sel()[0], str(hex(i)))