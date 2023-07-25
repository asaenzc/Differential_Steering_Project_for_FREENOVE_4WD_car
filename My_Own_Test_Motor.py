import time
from Motor import*            
PWM=Motor()          
def My_Own_Test_Motor(): 
    try:
        PWM.setMotorModel(4000,4000,4000,4000)       #Forward
        print ("The car is moving forward")
        time.sleep(1)
        PWM.setMotorModel(-4000,-4000,-4000,-4000)   #Back
        print ("The car is going backwards")
        time.sleep(1)
        PWM.setMotorModel(-500,-500,4000,4000)       #Left 
        print ("The car is turning left")
        time.sleep(1)
        PWM.setMotorModel(4000,4000,-500,-500)       #Right 
        print ("The car is turning right")  
        time.sleep(1)
        PWM.setMotorModel(4095,0,0,0)       #Only Wheel Left Front
        print ("The car is moving forward")
        time.sleep(1)
        PWM.setMotorModel(0,4095,0,0)   #Only Wheel Left Rear
        print ("The car is going backwards")
        time.sleep(1)
        PWM.setMotorModel(0,0,4095,0)       #Only Wheel Right Front
        print ("The car is turning left")
        time.sleep(1)
        PWM.setMotorModel(0,0,0,4095)       #Only Wheel Right Rear
        print ("The car is turning right")  
        time.sleep(1)
        PWM.setMotorModel(0,0,0,0)                   #Stop
        print ("\nEnd of program")
    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")
        
        
# Main program logic follows:
if __name__ == '__main__':

    print ('Program is starting ... ')
    import sys
    if len(sys.argv)<2:
        print ("Parameter error: Please assign the device Motor at the end of the command")
        exit() 
    if sys.argv[1] == 'Motor':
        My_Own_Test_Motor()
        exit()      
    print ("Parameter error: Please assign ONLY the device named as Motor")
    exit() 
    

