from mouseSpeedController import cursorController
import threading

def runCapMouseSpeedThread(finish):
        mouse=cursorController(sampleRate= 100)#you can change the params if u want but default values have been set
        while finish[0]:
                mouse.capMouseSpeed()
finish= [True]

#start thread which runs mouse.capMouseSpeed and mouse.updateMousePosition in an infinite loop
thread = threading.Thread(target=runCapMouseSpeedThread, args=[finish])
thread.start()

stop=input('This program will cap your mouse speed \nIf you want the the program to stop please enter (x):\n')

while stop != "x":
	stop=input('If you want the program to stop please enter (x):\n')

finish[0]= False#stops the thread 






