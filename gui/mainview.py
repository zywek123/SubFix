import wx
import player
import os
import loader
class view(wx.Frame):
	def __init__(self, parent, title):
		btnLoadText = None
		btnLoadMv = None
		self.player = None
		self.sub = None
		self.text = []
		self.textFile = ""
		self.videoFile = ""
		self.w, self.h = wx.GetDisplaySize()
		frame = wx.Frame.__init__(self, parent, wx.ID_ANY, title=title, size=(self.w, self.h), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
		self.SetBackgroundColour("black")
		self.SetForegroundColour("white")
		panel = wx.Panel(self, -1)
		panel.SetBackgroundColour("black")
		panel.SetForegroundColour("white")
		if self.textFile == "":
			btnLoadText = wx.Button(panel, -1, "Załaduj plik z tekstem")
			btnLoadText.SetSize(btnLoadText.GetBestSize())
			self.Bind(wx.EVT_BUTTON, self.loadText, btnLoadText)
		if self.videoFile == "":
			btnLoadMv = wx.Button(panel, -1, "Załaduj plik z nagraniem")
			btnLoadMv.SetSize(btnLoadMv.GetBestSize())
			self.Bind(wx.EVT_BUTTON, self.loadRec, btnLoadMv)
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		btnBox = wx.BoxSizer(wx.HORIZONTAL)
		self.btnPlay = wx.Button(panel, -1, "Odtwórz")
		self.btnPlay.SetSize(self.btnPlay.GetBestSize())
		btnBox.Add(self.btnPlay, 0, wx.ALL, 5)
		btnClose = wx.Button(panel, -1, "Zamknij")
		btnClose.SetSize(btnClose.GetBestSize())
		btnBox.Add(btnClose, 0, wx.ALL, 5)
		self.Bind(wx.EVT_BUTTON, self.onPlay, self.btnPlay)
		onEdit = wx.Button(panel, -1, "Edytuj")
		onEdit.SetSize(onEdit.GetBestSize())
		btnBox.Add(onEdit, 0, wx.ALL, 5)
		self.Bind(wx.EVT_BUTTON, self.onEdit, onEdit)
		onSave = wx.Button(self, -1, "Zapisz")
		onSave.SetSize(onSave.GetBestSize())
		btnBox.Add(onSave, 0, wx.ALL, 5)
		self.Bind(wx.EVT_BUTTON, self.onSave, onSave)
		if btnLoadText != None:
			btnBox.Add(btnLoadText, 0, wx.ALIGN_BOTTOM, 10)
		if btnLoadMv != None:
			btnBox.Add(btnLoadMv, 0, wx.ALIGN_BOTTOM, 10)
		self.sizer.Add(btnBox, 0, wx.ALL, 5)
		self.SetSizer(self.sizer)
		self.SetAutoLayout(1)
		self.sizer.Fit(self)
		self.Show(1)

	def loadRec(self, e):
		dlg = wx.FileDialog(self, "Wybierz plik do otwarcia", "", "*.*", style=wx.FD_OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.videoFile = dlg.GetFilename()
			dir = dlg.GetDirectory()
			self.player = player.Player(self, os.path.join(dir, self.videoFile))
		dlg.Destroy()

	def loadText(self, e):
		dlg = wx.FileDialog(self, "Wybierz plik do otwarcia", "", "*.*", style=wx.FD_OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.textFile = dlg.GetFilename()
			dir = dlg.GetDirectory()
		self.sub = loader.Loader(os.path.join(dir, self.textFile))
		dlg.Destroy()
		self.text = self.sub.getText()

	def onSave(self, e):
		dlg = wx.FileDialog(self, "Wybierz plik do zapisu", "", "*.*", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
		if dlg.ShowModal() == wx.ID_OK:
			file = dlg.GetFilename()
			dir = dlg.GetDirectory()
			file2 = file+".txt"
			self.save(os.path.join(dir, file2))
		dlg.Destroy()

	def save(self, file):
		f = open(file,  "w")
		for t in self.text:
			f.write(t+"\n")
		f.close()

	def onPlay(self, e):
		self.player.playPause()
		if self.player.playing == True:
			self.btnPlay.SetLabel("Wstrzymaj")
		else:
			self.btnPlay.SetLabel("Odtwórz")


	def onEdit(self, e):
		self.onPlay(0)
		print("Current pos: ", self.player.getPosition())
		dlg = wx.TextEntryDialog(self, "Edytuj", "Edytuj napis")
		dlg.SetValue(self.sub.getSubText(self.sub.getIndexAt(self.player.getPosition())))
		resp = dlg.ShowModal()
		if resp == wx.ID_OK:
			text = dlg.GetValue()
			self.text[self.sub.getIndexAt(self.player.getPosition())] = text
		dlg.Destroy()
		self.onPlay(0)

