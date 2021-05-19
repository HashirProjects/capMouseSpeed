from mouseSpeedController import cursor
import threading

mouse=cursor()#you can change the params if u want but default values have been set

#start thread which runs mouse.capMouseSpeed and mouse.updateMousePosition in an infinite loop

stop=input('This program will cap your mouse speed \nIf you want the the program to stop please enter X: \n ')

while stop != "X":
	stop=input('If you want the the program to stop please enter X: \n ')

#stop the thread






