import vlc
import wx
class Player(wx.Frame):
	def __init__(self, parent, path):
		self.playing = False
		self.instance = vlc.Instance("--no-xlib --quiet")
		w, h = wx.GetDisplaySize()
		frame = wx.Frame.__init__(self, parent, -1, title="Odtwarzacz - SubFix", size=(w, h), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL | wx.WANTS_CHARS)
		self.btnPlay = wx.Button(self, -1, "Odtwórz")
		self.btnPlay.SetSize(self.btnPlay.GetBestSize())
		btnClose = wx.Button(self, -1, "Zamknij")
		btnClose.SetSize(btnClose.GetBestSize())
		sizer = wx.BoxSizer(wx.VERTICAL)
		psizer = wx.BoxSizer(wx.HORIZONTAL)
		psizer.Add(self.btnPlay, 0, wx.ALL, 5)
		psizer.Add(btnClose, 0, wx.ALL, 5)
		sizer.Add(psizer, 0, wx.ALL, 5)
		self.SetSizer(sizer)
		self.SetAutoLayout(1)
		self.Show()
		self.stream = self.instance.media_player_new(path)
		self.Bind(wx.EVT_BUTTON, self.onPlay, self.btnPlay)
		self.Bind(wx.EVT_CLOSE, self.onClose)
		self.Bind(wx.EVT_BUTTON, self.onClose, btnClose)

	def play(self):
		if sys.platform == "win32":
			self.stream.set_hwnd(self.GetHandle())
		else:
			self.stream.set_xwindow(self.GetHandle())
		self.stream.audio_set_volume(50)
		self.stream.play()
		self.playing = True

	def playPause(self):
		if self.playing == True:
			self.stream.pause()
			self.playing = False
		else:
			self.stream.play()
			self.playing = True

	def onPlay(self, e):
		self.playPause()
		if self.playing == True:
			self.btnPlay.SetLabel("Wstrzymaj")
			self.btnPlay.SetFocus()
		else:
			self.btnPlay.SetLabel("Odtwórz")
			self.btnPlay.SetFocus()

	def onClose(self, e):
		self.stream.stop()
		self.stream = None
		self.Destroy()

