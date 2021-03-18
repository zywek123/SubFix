import wx
class view(wx.Frame):
	def __init__(self, parent, title):
		btnLoadText = None
		btnLoadMv = None
		self.textFile = ""
		self.videoFile = ""
		self.w, self.h = wx.GetDisplaySize()
		frame = wx.Frame.__init__(self, parent, wx.ID_ANY, title=title, size=(self.w, self.h), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
		self.SetBackgroundColour("black")
		self.SetForegroundColour("white")
		panel = wx.Panel(self, -1, size=(800, 400))
		panel.SetBackgroundColour("black")
		panel.SetForegroundColour("white")
		if self.textFile == "":
			btnLoadText = wx.Button(panel, -1, "Załaduj plik z tekstem")
			btnLoadText.SetSize((25, 25))
			self.Bind(wx.EVT_BUTTON, self.loadText, btnLoadText)
		if self.videoFile == "":
			btnLoadMv = wx.Button(panel, -1, "Załaduj plik z nagraniem")
			btnLoadMv.SetSize((25, 25))
			self.Bind(wx.EVT_BUTTON, self.loadRec, btnLoadMv)
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		btnBox = wx.BoxSizer(wx.HORIZONTAL)
		if btnLoadText != None:
			btnBox.Add(btnLoadText, 0, wx.ALIGN_RIGHT, 10)
		if btnLoadMv != None:
			btnBox.Add(btnLoadMv, 0, wx.ALIGN_RIGHT, 10)
		self.sizer.Add(btnBox, 0, wx.ALL, 5)
		panel.SetSizer(self.sizer)
		self.SetAutoLayout(1)
		self.sizer.Fit(self)
		self.Show(1)

	def loadRec(self, e):
		dlg = wx.FileDialog(self, "Wybierz plik do otwarcia", "", "*.*", style=wx.FD_OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.videoFile = dlg.GetFilename()
			dir = dlg.GetDirectory()
		dlg.Destroy()

	def loadText(self, e):
		dlg = wx.FileDialog(self, "Wybierz plik do otwarcia", "", "*.*", style=wx.FD_OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.textFile = dlg.GetFilename()
			dir = dlg.GetDirectory()
		dlg.Destroy()

