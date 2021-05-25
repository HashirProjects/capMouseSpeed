import pynput
import math
import time

class cursorController():
		
	def __init__(self, sampleRate=60, speed=500):
		self.timeInterval= 1/sampleRate
		self.mouse=pynput.mouse.Controller()
		self.maxDistancePerAxis= speed * self.timeInterval # maxDistancePerAxis is the maximum distance moved in each axis in the given time period before the program starts to cap speed
		self.maxDistance= math.sqrt(2) * self.maxDistancePerAxis

	def getMouseDistanceMoved(self):
		#calls getMousePosition twice with a small interval inbetween
		
		self.prevX, self.prevY = self.mouse.position

		time.sleep(self.timeInterval)
		
		self.x, self.y = self.mouse.position
		
	def capMouseSpeed(self):
                
		#call getMouseDistanceMoved, if the distance moved is larger than what you want (maxDistance), then:
		#for the axis in which the cursor moved the most, (change in self.[other axis])= (change in self.[other axis]) * maxDistancePerAxis/(change in self.[the axis]) 
		#and change in self.[the axis]= maxDistancePerAxis (which is the same thing as (change in self.[the axis])= (change in self.[the axis]) * maxDistancePerAxis/(change in self.[the axis]))
		#the idea is that you want to scale down the movement in each axis by the same amount to ensure that direction is preserved

		self.getMouseDistanceMoved()
		
		changeX= self.x - self.prevX
		changeY= self.y - self.prevY
		
		distanceMoved= math.sqrt((self.x-self.prevX)*(self.x-self.prevX)+(self.y-self.prevY)*(self.y-self.prevY))

		if distanceMoved > self.maxDistance:

			try:
				if abs(changeX) > abs(changeY):
                                        
					self.y= self.prevY + changeY * self.maxDistancePerAxis/abs(changeX)
					self.x= self.prevX + changeX * self.maxDistancePerAxis/abs(changeX)
				
				if abs(changeY) > abs(changeX):
                                        
					self.x= self.prevX + changeX * self.maxDistancePerAxis/abs(changeY)
					self.y= self.prevY + changeY * self.maxDistancePerAxis/abs(changeY)
					
			except Exception as ex:
				print(ex)	
			finally:
				
				self.mouse.position = (self.x, self.y)


		




