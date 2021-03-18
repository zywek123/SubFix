import vlc
import wx
class Player(wx.Frame)):
	def __init__(self, parent, path):
		self.instance = vlc.Instance("--no-xlib --quiet")
		w, h = wx.GetDisplaySize()
		frame = wx.Frame.__init__(self, parent, -1, title="Odtwarzacz - SubFix", size=(w, h), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
		panel = wx.Panel(self, -1, style=wx.WANTS_CHARS)
		panel.SetBackgroundColour("black")
		panel.SetForegroundColour("white")
		sizer = wx.BoxSizer(wx.VERTICAL)
		psizer = wx.BoxSizer(wx.HORIZONTAL)
		psizer.Add(panel, 0, wx.ALL, 5)
		sizer.add(psizer, 0, wx.ALL, 5)
		self.SetSizer(sizer)
		self.Show()
		self.stream = self.instance.media_player_new(path)

	def play(self):
		if sys.platform = "win32":
			self.stream.set_hwnd(self.GetHandle())
		else:
			self.stream.set_xwindow(self.GetHandle())

