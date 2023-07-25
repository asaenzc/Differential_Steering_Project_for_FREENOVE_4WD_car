echo "Current date : $(date) @ $(hostname) w/ IP @ $(hostname -I)"
#o también:  #echo "ping raspeberrypi.local -c 1"
echo "Network configuration"
/sbin/ifconfig wlan0
<<COMMENT1
	Be sure you first start the USBIP by executing
	<<sh Str_USB.sh>> in the PC-ASUS (w/ the SSD Crucial connected) side. 
COMMENT1
read -p "Press [Enter] key to ATTACH the usbip has bin by the USB Server..." fakeEnterKey
#See USB SERVER
usbip list --remote 192.168.1.144
#attach busid of USB SERVER 
sudo usbip attach -r 192.168.1.144 -b 1-2
#See USB ports of Client including USB SERVER
sleep 1.5
lsusb
#Start My Application My_DSW.py
cd ./Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/Code/MY_PRGs
echo "cd to new DIR is" 
pwd
read -p "and now press [Enter] key again to start My_DSW..." fakeEnterKey
#Start My_appplication
sudo python My_DSW.py
