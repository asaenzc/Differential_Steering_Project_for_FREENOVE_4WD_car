#import evdev
from evdev import InputDevice, categorize, ecodes

#cree un objet My_StW | creates object My_StW	
My_StW = InputDevice('/dev/input/event0')

#Presentar la llista dels dispositius conectats | prints out device info connected at the begining
print(My_StW)

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

#Mostrar 3ls codis interceptats |  display codes
for event in My_StW.read_loop():
    #Boutons | buttons 
    if event.type == ecodes.EV_KEY:
        #print(event)
        if event.value == 1:
            if event.code == xBtn:
                print("X_Quadrat")
            elif event.code == yBtn:
                print("Y_R2")
            elif event.code == zBtn:
                print("Z_L2")
            elif event.code == aBtn:
                print("A_Triangle_LLEVA-DERETA")
            elif event.code == bBtn:
                print("B_Cercle_LLEVA-ESQUERRA")
            elif event.code == cBtn:
                print("C_CREU-X")
            elif event.code == tlBtn:
                print("L1_LEFT")
            elif event.code == trBtn:
                print("R1_RIGHT")
            elif event.code == tl2Btn:
                print("Select")
            elif event.code == tr2Btn:
                print("Start")
        elif event.value == 0:
          print("Pulsador liberado | Button Release")

    #Volant analogic | Analog Steering_Wheel
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        #print ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value
        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
             val= absevent.event.value
             if val < 0:
                print("LEFT ", val)
             elif val > 0:
                print("RIGHT ", val)
             elif val == 0:
                print("Centre | Center")
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
             val= absevent.event.value
             if val == 0:
                print("Brake | Throttle not pressed")
             elif val > 0:
                print("BRAKE ", val)
             elif val < 0:
                print("THROTTLE ", val)
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0X":
             if absevent.event.value == 0:
                print("Joystick not pressed")
             elif absevent.event.value == 1:
                print("Joystick RIGHT")
             elif absevent.event.value == -1:
                print("Joystick LEFT")
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0Y":
             if absevent.event.value == 0:
                print("Joystick not pressed")
             elif absevent.event.value == -1:
                print("Joystick UP")
             elif absevent.event.value == 1:
                print("Joystick DOWN")


