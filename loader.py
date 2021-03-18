import pysrt
class Loader():
	def __init__(self, path):
		self.path = path
		self.subs = pysrt.open(self.path)

	def getDuration(self):
		duration = 0
		for i in range(len(self.subs)):
			duration += self.subs[i].duration.seconds*100
		return duration

	def getSubDuration(self, index):
		return self.subs[index].duration.seconds*100

	def getSubText(self, index):
		return self.subs[index].text

	def getSubsCount(self):
		return len(self.subs)

	def getText(self):
		text = []
		for i in range(len(self.subs)):
			text.append(self.subs[i].text)
		return text

	def getIndexAt(self, time):
		dur = 0
		for i in range(len(self.subs)):
			dur += self.getSubDuration(i)
			if dur > time + 150:
				return i
				break

