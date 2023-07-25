import time
import math

# antes he instalado la librería pynput con: sudo pip install pynput

AR= 124
AE= 143
FF= AE/AR
print ( "AR= {0}, AE= {1}, FF= {2}", AR, AE, FF )
#Velo= Throttle (from 0 to 4095 speed to go)
#Handbar or Sterring Wheel= StW (from 0 to 4096 angle selected: 4096 means it is turned 360º)

#Vo=VelOutside=(Velo/(2*4096))*RAIZ(POTENCIA(((2*4096+HWheel);2)+POTENCIA((HWheel*FF);2))
#Vi=VelInside=((Velo/(2*4096))*RAIZ(POTENCIA(((2*4096)-HWheel);2)+POTENCIA(HWheel*FF);2))
#Vo= (Velo/8192)*math.sqrt((8192+HWheel)**2 + (HWheel*FF)**2)
#Vi= (Velo/8192)*math.sqrt((8192-HWheel)**2 + (HWheel*FF)**2)
from Motor import*            
PWM=Motor()         
def Chg_Speed():
        Vo= (Velo/8192)*math.sqrt((8192+StW)**2 + (StW*FF)**2)
        Vi= (Velo/8192)*math.sqrt((8192-StW)**2 + (StW*FF)**2)
#        print ("The Outer_Wheels turn at", Vo)
#        print ("The Inner_Wheels turn at", Vi)
        Vo=int(round(Vo))
        Vi=int(round(Vi))
#        print ("The Outer_Wheels turn at", Vo)
#        print ("The Inner_Wheels turn at", Vi)
        print ("Wheels turn: OUTER", Vo, "and INNER to", Vi)
        PWM.setMotorModel(Vo,Vo,Vi,Vi)

import os,sys,tty,termios
TERMIOS = termios

def GetKey():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
        new[6][TERMIOS.VMIN] = 1
        new[6][TERMIOS.VTIME] = 0
        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
        key = None
        try:
            key = os.read(fd, 4)
#            if key == b'\x1b':
#                key = "Escape"
#            else:
#                key = key.decode()
            key = key.decode()

        finally:
            termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
        return key
 
def ejecuta():
    global Velo, StW
    k=''
    try:  
        while(1):
            Chg_Speed()
            k=GetKey()
#            print ("Key pressed was: ", int(k))    #Interpreter ERROR allows see code of key in "base 10"
            if k=='\x1b[A':    #Arror UP is pressed
                Velo+= 10
                print (">>> UP: Velo=", Velo, "| StW=", StW)
            elif k=='\x1b[B':
                Velo-= 10
                print (">>> DOWN: Velo=", Velo, "| StW=", StW)
            elif k=='\x1b[C':
                StW+= 10
                print (">>> RIGHT: Velo=", Velo, "| StW=", StW)
            elif k=='\x1b[D':
                StW-= 10
                print (">>> LEFT: Velo=", Velo, "| StW=", StW)
            elif k=='\x1bOA':    #Ctrl is pressed as well
                Velo+= 100
                print (">>> CtrlUP: Velo=", Velo, "| StW=", StW)
            elif k=='\x1bOB':
                Velo-= 100
                print (">>> CtrlDOWN: Velo=", Velo, "| StW=", StW)
            elif k=='\x1bOC':
                StW+= 100
                print (">>> CtrlRIGHT: Velo=", Velo, "| StW=", StW)
            elif k=='\x1bOD':
                StW-= 100
                print (">>> CtrlLEFT: Velo=", Velo, "| StW=", StW)
            elif k=='\x1b\x1b[A':    #Alt is pressed as well
                Velo+= 1
                print (">>> AltUP: Velo=", Velo, "| StW=", StW)
            elif k=='\x1b\x1b[B':
                Velo-= 1
                print (">>> AltDOWN: Velo=", Velo, "| StW=", StW)
            elif k=='\x1b\x1b[C':
                StW+= 1
                print (">>> AltRIGHT: Velo=", Velo, "| StW=", StW)
            elif k=='\x1b\x1b[D':
                StW-= 1
                print (">>> AltLEFT: Velo=", Velo, "| StW=", StW)
            else:
                print ("Key pressed was: ", k)
    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")
        
   

# Main program logic follows:
if __name__ == '__main__':
    Velo= 4095    #Assign Velo to be a number
    StW= 4095  #Assign HandWheel to be a number as well
    #print ('Program is starting ... ')
    import sys
    if len(sys.argv)<3:
        print ("Parameter error: Please assign the speed of the car is wanted (0 to 4095)\n\t\t and the angle of the handwheel (0 to 4095)")
        exit()
    Velo= int(sys.argv[1])
    StW= int(sys.argv[2])
    print ('Velocity: ', Velo, '|| Steering Wheel angle: ', StW, '(means: ', 360*StW/4095, 'º )')
    print('Use ARROWs to (de)increment by 10 and with CTRL by 100 and with ALT by 1')
    ejecuta()
    exit() 
    

