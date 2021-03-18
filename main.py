from gui import mainview
import wx
app = wx.App()
frame = mainview.view(None, "SubFix")
app.SetTopWindow(frame)
app.MainLoop()
