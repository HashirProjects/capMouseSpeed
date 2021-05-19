import pynput
import math

class cursor():
		
	def __init__(self, maxDistancePerAxis=5, timeInterval=0.05):
		self.maxDistancePerAxis= maxDistancePerAxis #the maximum distance moved in each axis in the given time period before the program starts to cap speed
		self.maxDistance= math.sqrt(2) * maxDistancePerAxis
		self.timeInterval= timeInterval #1/sample rate

	def getMousePosition(self):
		#update self.x and self.y

	def getMouseDistanceMoved(self):
		#calls getMousePosition twice with a small interval inbetween and uses pythagorus to work out the distance moved

	def capMouseSpeed(self):
		#call getMouseDistanceMoved, if the distance moved is larger than what you want (maxDistance), then:
		#for the axis in which the cursor moved the most, self.[other axis]= self.[other axis] * maxDistancePerAxis/self.[the axis] 
		#and self.[the axis]= maxDistancePerAxis (which is the same thing as self.[the axis]= self.[the axis] * maxDistancePerAxis/self.[the axis])
		#the idea is that you want to scale down the movement in each axis by the same amount to ensure that direction is preserved
		#make sure to round to the nearest int

	def updateMousePosition(self):
		#uses pynput to update the position of the mouse to self.x and self.y 


