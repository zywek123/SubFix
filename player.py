import vlc
import sys
class Player():
	def __init__(self, par, path):
		self.playing = False
		self.instance = vlc.Instance("--no-xlib --quiet")
		self.stream = self.instance.media_player_new(path)
		self.parent = par

	def play(self):
		if sys.platform == "win32":
			self.stream.set_hwnd(self.parent.GetHandle())
		else:
			self.stream.set_xwindow(self.parent.GetHandle())
		self.stream.audio_set_volume(50)
		self.stream.play()
		self.playing = True

	def pause(self):
		self.stream.pause()

	def playPause(self):
		if self.playing == True:
			self.pause()
			self.playing = False
		else:
			self.play()
			self.playing = True

	def onClose(self):
		self.stream.stop()
		self.stream = None

	def getPosition(self):
		pos = self.stream.get_position()*1000000
		pos2 = str(pos).split(".")[0]
		return int(pos2)
