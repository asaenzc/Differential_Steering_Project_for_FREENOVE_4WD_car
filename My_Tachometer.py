import time

from Motor import*            
PWM=Motor()          
def To_measured_by_stroboscopic_Tachometer():
    global Velo
    try:
        print ("The Right_Rear_Wheel is turning at", Velo)  
        PWM.setMotorModel(Velo,Velo,Velo,Velo)       #Only Wheel Right Rear
        time.sleep(100)
        PWM.setMotorModel(0,0,0,0)                   #Stop
        print ("\nEnd of program")
    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")
        
        
# Main program logic follows:
if __name__ == '__main__':

    Velo= 4095    #Assign Velo to be a number
    print ('Program is starting ... ')
    import sys
    if len(sys.argv)<2:
        print ("Parameter error: Please assign the speed is wanted to turn (1 to 4095)")
        exit()
    Velo= int(sys.argv[1])
    print ('Velocity selected is: ', Velo)
    To_measured_by_stroboscopic_Tachometer()
    exit() 
    

