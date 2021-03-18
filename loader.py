class Loader():
	def __init__(self, path):
		self.path = path
		self.f = open(self.path, "r")

def getProps(self):
		line = self.f.readline()
		time = self.f.readline().split(",")
		text = self.f.readline()
		self.f.readline()
		return (line, time[0], time[1], text)

