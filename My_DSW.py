# My_DSW = My Differential Steering Wheel
import _thread
import time
import math
from Led import *
led=Led()
def Led_Rear_Middle_Right():
        led.ledIndex(0x01,255,0,0)      #Red
def Led_Rear_Middle_Right_Off():
        led.ledIndex(0x01,0,0,0)        #Red
def Led_Rear_Right():
        led.ledIndex(0x02,255,125,0)    #orange
def Led_Rear_Right_Off():
        led.ledIndex(0x02,0,0,0)        #orange
def Led_Rear_Left():
        led.ledIndex(0x04,255,255,0)    #yellow
def Led_Rear_Left_Off():
        led.ledIndex(0x04,0,0,0)        #yellow
def Led_Rear_Middle_Left():
        led.ledIndex(0x08,0,255,0)      #green
def Led_Rear_Middle_Left_Off():
        led.ledIndex(0x08,0,0,0)        #green

def Led_Front_Middle_Left():        
        led.ledIndex(0x10,0,255,255)    #cyan-blue
def Led_Front_Middle_Left_Off():        
        led.ledIndex(0x10,0,0,0)        #cyan-blue
def Led_Front_Left():
        led.ledIndex(0x20,0,0,255)      #blue
def Led_Front_Left_Off():
        led.ledIndex(0x20,0,0,0)         #blue
def Led_Front_Right():
        led.ledIndex(0x40,128,0,128)    #purple
def Led_Front_Right_Off():
        led.ledIndex(0x40,0,0,0)        #purple
def Led_Front_Middle_Right():
        led.ledIndex(0x80,255,255,255)  #white'''
def Led_Front_Middle_Right_Off():
        led.ledIndex(0x80,0,0,0)        #white'''
#        print ("The LED has been lit, the color is red orange yellow green cyan-blue blue white")
#        time.sleep(3)               #wait 3s
def Led_Off():        
        led.colorWipe(led.strip, Color(0,0,0))  #turn off the light


#Velo    #Global Variable and assign Velo to be a number
#StW     #Global Variable too and assign Sterreing Wheel to be a number as well


#Aquí tot el tema del teclat 
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


def My_Steering_by_the_Keyboard():
            global Velo,StW
            k=''
            k=GetKey()     #Get Key from keyboard
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


#Aquí les formules pel Electronic Differential Steering
AR= 128
AE= 145
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
        global Velo,StW
        global DriveMode
        
        if DriveMode==0:
#        Vo= (Velo/4096)*math.sqrt((4096+StW)**2 + (StW*FF)**2)
#        Vo= (Velo/128)*math.sqrt((128+StW)**2 + (StW*FF)**2)
            Vo= (Velo/128)*(128+StW)
#        Vi= (Velo/4096)*math.sqrt((4096-StW)**2 + (StW*FF)**2)
#        Vi= (Velo/128)*math.sqrt((128-StW)**2 + (StW*FF)**2)
            Vi= (Velo/128)*(128-StW)
        else:
            Vo= (Velo+StW)
            Vi= (Velo-StW)
#        print ("The Outer_Wheels turn at", Vo)
#        print ("The Inner_Wheels turn at", Vi)
        Vo=int(round(Vo))
        Vi=int(round(Vi))
#        print ("The Outer_Wheels turn at", Vo)
#        print ("The Inner_Wheels turn at", Vi)
        PWM.setMotorModel(Vo,Vo,Vi,Vi)
#        print("\fStW=", StW, " || Velo=", Velo, " | Outer Wheel=", Vo, " | Inner=", Vi, "                        ")



from servo import *
pwm=Servo()
class My_Servo:
    global forServo0,forServo1
    def __init__(self):
        forServo0=90
        forServo1=90

def Servo0_Right():
            global forServo0
            forServo0+= 1
            pwm.setServoPwm('0',forServo0)
def Servo0_Left():
            global forServo0
            forServo0-= 1
            pwm.setServoPwm('0',forServo0)
def Servo1_Up():
            global forServo1
            forServo1+= 1
            pwm.setServoPwm('1',forServo1)
def Servo1_Down():
            global forServo1
            forServo1-= 1
            pwm.setServoPwm('1',forServo1)
            
def Servo_Check():
            for i in range(90,180,1):
                pwm.setServoPwm('0',i)
                time.sleep(0.01)
            for i in range(180,0,-1):
                pwm.setServoPwm('0',i)
                time.sleep(0.01)
            for i in range(0,90,1):
                pwm.setServoPwm('0',i)
                time.sleep(0.01)
            for i in range(90,180,1):
                pwm.setServoPwm('1',i)
                time.sleep(0.01)
            for i in range(180,80,-1):
                pwm.setServoPwm('1',i)
                time.sleep(0.01)
            for i in range(80,90,1):
                pwm.setServoPwm('1',i)
                time.sleep(0.01)

def Servo_Home():
        global forServo0,forServo1
        forServo0=90
        forServo1=90
        pwm.setServoPwm('0',forServo0)
        pwm.setServoPwm('1',forServo1)
        
from ADC import *
adc=Adc()
def Read_Adc():
            Left_IDR=adc.recvADC(0)
            print ("The photoresistor voltage on the left is "+str(Left_IDR)+"V")
            Right_IDR=adc.recvADC(1)
            print ("The photoresistor voltage on the right is "+str(Right_IDR)+"V")
            Power=adc.recvADC(2)
            print ("The battery voltage is "+str(Power*3)+"V")



#Aquí tot per fer us del volant ("USB Steering Wheel")
#Presentar la llista dels dispositius conectats | prints out device info connected at the begining
#print(My_StW)

aBtn = 304		#Triangle o LEVA DERETA
bBtn = 305		#Cercle O LEVA ESQUERRA
cBtn = 306		#La Creu X
xBtn = 307		#Cuadrat
yBtn = 308		#R2
zBtn = 309		#L2
tlBtn = 310		#L1
trBtn = 311		#R1
tl2Btn = 312	#Select
tr2Btn = 313	#Start
absHATOX=16		#ABS_HATOX
absHATOY=17		#ABS_HATOY

import evdev
from evdev import InputDevice, categorize, ecodes
#crear objecte My_StW | creates object My_StW	
My_StW = InputDevice('/dev/input/event0')

from Buzzer import *
buzzer=Buzzer()

class My_SteerWheel:

#    def __init__(self):
        
    def SteerWD(event):
            global Velo,StW
            global DriveMode
            #Mostrar els codis interceptats |  display codes
            #Boutons | buttons 
            if event.type == ecodes.EV_KEY:
                #print(event)
                if event.value == 1:
                    if event.code == xBtn:
                        Servo_Home()
#                        Servo_Check()
#                        print("X_Quadrat")
                    elif event.code == yBtn:
                        Led_Rear_Right()
#                        print("Y_R2")
                    elif event.code == zBtn:
                        Led_Rear_Left()
#                        print("Z_L2")
                    elif event.code == aBtn:
                         Led_Front_Middle_Right()        
#                        print("A_Triangle_LLEVA-DERETA")
                    elif event.code == bBtn:
                         Led_Front_Middle_Left()        
#                        print("B_Cercle_LLEVA-ESQUERRA")
                    elif event.code == cBtn:
                        buzzer.run('1')
#                        print("C_CREU-X")
                    elif event.code == tlBtn:
                        Led_Front_Left()
#                        print("L1_LEFT")
                    elif event.code == trBtn:
                        Led_Front_Right()
#                        print("R1_RIGHT")
                    elif event.code == tl2Btn:
#                        print("Select")
                        if DriveMode==0:
                            DriveMode=1
                            Led_Rear_Middle_Left()       
                            Led_Rear_Middle_Right()       
                        else:
                            DriveMode=0
                            Led_Rear_Middle_Left_Off()       
                            Led_Rear_Middle_Right_Off()       
                            Led_Off()       
                    elif event.code == tr2Btn:
                        Read_Adc()
#                        print("Start")

                elif event.value == 0:
                    if event.code == xBtn:
                        Servo_Home()
#                        print("X_Quadrat_0")
                    elif event.code == yBtn:
                        Led_Rear_Right_Off()                         
#                        print("Y_R2_0")
                    elif event.code == zBtn:
                        Led_Rear_Left_Off()
#                        print("Z_L2_0")
                    elif event.code == aBtn:
                        Led_Front_Middle_Right_Off()        
#                        print("A_Triangle_LLEVA-DERETA_0")
                    elif event.code == bBtn:
                        Led_Front_Middle_Left_Off()        
#                        print("B_Cercle_LLEVA-ESQUERRA_0")
                    elif event.code == cBtn:
                        buzzer.run('0')
#                        print("C_CREU-X_0")
                    elif event.code == tlBtn:
                        Led_Front_Left_Off()
#                        print("L1_LEFT_0")
                    elif event.code == trBtn:
                        Led_Front_Right_Off()
#                        print("R1_RIGHT_0")
                    elif event.code == tl2Btn:
                        Read_Adc()
#                        print("Select_0")
                    elif event.code == tr2Btn:
                        Read_Adc()
#                        print("Start_0")
#                    print("Pulsador liberado | Button Release")

    def SteerWA(event):
        global Velo,StW
        global Servo0ON, Servo1ON
        global DriveMode
        if event.type == ecodes.EV_ABS:
            absevent = categorize(event)
            #print ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
#                 val= absevent.event.value
#                 StW=val*32
                if DriveMode==0:
                    StW= absevent.event.value
                else:
                    StW= 12*absevent.event.value
#                 if val < 0:
#                    print("LEFT ", val, "| StW ", StW)
#                 elif val > 0:
#                    print("RIGHT ", val, "| StW ", StW)
#                 elif val == 0:
#                    print("Centre | Center")
            elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
#                 val= absevent.event.value
#                 Velo=-val*14
                if DriveMode==0:
                    Velo=-16*absevent.event.value
                else:
                    Velo=-20 *absevent.event.value
#                 if val<0:
#                     Led_Front_Middle_Left()        
#                     Led_Front_Middle_Right()        
#                 elif val>0:
#                     Led_Rear_Middle_Left()       
#                     Led_Rear_Middle_Right()       
#                 elif val==0:
#                     Led_Off()                         
#                 if val == 0:
#                    print("Brake | Throttle not pressed")
#                 elif val > 0:
#                    print("BRAKE ", val, "| Velo ", Velo)
#                 elif val < 0:
#                    print("THROTTLE ", val, "| Velo ", Velo)
            elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0X":
                Servo0ON= absevent.event.value
#                 if absevent.event.value == 1:
#                     Servo0_Right()
#                     print("Joystick RIGHT")
#                 elif absevent.event.value == -1:
#                     Servo0_Left()
#                     print("Joystick LEFT")
#                 elif absevent.event.value == 0:
#                     print("Joystick not pressed")
            elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0Y":
                 Servo1ON= absevent.event.value
#                  if absevent.event.value == -1:
#                    Servo1_Up()
#                    print("Joystick UP")
#                 elif absevent.event.value == 1:
#                     Servo1_Down()
#                    print("Joystick DOWN")
#                 elif absevent.event.value == 0:
#                      print("Joystick not pressed")
        

#Aquí el bucle de execució miran el volant (Steering Wheel), l'accelerador y el teclat (que s'anularà segur).
def ejecuta():
        
        for event in My_StW.read_loop():
            My_SteerWheel.SteerWD(event)
            My_SteerWheel.SteerWA(event)
            Chg_Speed()    #Change Speed
#            My_Steering_by_the_Keyboard()

def Temporiza(delay):
    global Servo0ON, Servo1ON
    while 1:
        if Servo1ON == 1:
            Servo1_Down()
        elif Servo1ON == -1:
            Servo1_Up()
        if Servo0ON == 1:
            Servo0_Right()
        elif Servo0ON == -1:
            Servo0_Left()
#        time.sleep(delay)
        time.sleep(0.1)
  

# Main program logic follows:
if __name__ == '__main__':
    global Velo,StW, forServo0, forServo1, Servo0ON, Servo1ON, DriveMode
    #print ('Program is starting ... ')
    import sys
    Velo= 0
    StW= 0
    forServo0=90
    forServo1=90
    Servo0ON=0
    Servo1ON=0
    DriveMode=0

    try:
#        if len(sys.argv)<3:
#            print ("Parameter error: Please assign the speed of the car is wanted (0 to 4095)\n\t\t and the angle of the handwheel (0 to 4095)")
#            exit()
#        Velo= int(sys.argv[1])
#        StW= int(sys.argv[2])
#        print ('Velocity: ', Velo, '|| Steering Wheel angle: ', StW, '(means: ', 360*StW/4095, 'º )')
#        print('Use ARROWs to (de)increment by 10 and with CTRL by 100 and with ALT by 1')
#######        ejecuta()
         _thread.start_new_thread( Temporiza, (1, ) )
         _thread.start_new_thread( ejecuta() )
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        del My_StW
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")
        destroy()
        exit()
