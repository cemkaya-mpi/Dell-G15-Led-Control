#!/usr/bin/python3
import sys
from elc import *
from elc_constants import *
import binascii
def main():
        if (len(sys.argv)==5):
                red=int(sys.argv[2])
                green=int(sys.argv[3])
                blue=int(sys.argv[4])
        elif(len(sys.argv)==2 and sys.argv[1]=="off"):
                red=0
                green=0
                blue=0
        elif(len(sys.argv)==2 and sys.argv[1]=="on"):
                red=255
                green=255
                blue=255
        else:
                print("Usage:")
                print("awcc.py off                      -> Turn lights off.")
                print("awcc.py on                       -> Turn lights on.")
                print("awcc.py red green blue           -> With custom colors.")
                print("Range for red,green,blue is 0-255")
                print("eg.: awcc.py on 255 255 255      -> Bright white")
                print("eg.: awcc.py on 128 128 128      -> Dim white")
                red=255
                green=255
                blue=255
        
        print("Red:%d, Green:%d, Blue:%d" % (red,green,blue))
        #So that we don't get an USB device busy error
        device=usb.core.find(idVendor=0x187c, idProduct=0x0550)
        ep = device[0].interfaces()[0].endpoints()[0]
        i = device[0].interfaces()[0].bInterfaceNumber
        device.reset()
        if device.is_kernel_driver_active(i):
                device.detach_kernel_driver(i)

        #Create the elc object
        vid=0x187C
        pid=0x0550
        elc=Elc(vid,pid,debug=0)

        #Define zones
        zones=[0, 1, 2, 3]

        #White color is default, test this line to see if it works at all!
        #elc.set_color(zones,red,green,blue) # White 
        #elc.dim(zones, dim)                # No dimming

        #Off on AC Sleep
        elc.remove_animation(AC_SLEEP)
        elc.start_new_animation(AC_SLEEP)
        elc.start_series(zones)
        elc.add_action((Action(COLOR,2000,100,red,green,blue),)) # Static color, 2 second duration, 100 tempo (who cares?)
        elc.finish_save_animation(AC_SLEEP)

        #Full brightness on AC, charged
        elc.remove_animation(AC_CHARGED)
        elc.start_new_animation(AC_CHARGED)
        elc.start_series(zones)
        elc.add_action((Action(COLOR,2000,100,red,green,blue),)) # Static color, 2 second duration, 100 tempo (who cares?)
        elc.finish_save_animation(AC_CHARGED)
        
        #Full brightness on AC, charging
        elc.remove_animation(AC_CHARGING)
        elc.start_new_animation(AC_CHARGING)
        elc.start_series(zones)
        elc.add_action((Action(COLOR,2000,100,red,green,blue),)) # Static color, 2 second duration, 100 tempo (who cares?)
        elc.finish_save_animation(AC_CHARGING)

        #Off on DC Sleep
        elc.remove_animation(DC_SLEEP)
        elc.start_new_animation(DC_SLEEP)
        elc.start_series(zones)
        elc.add_action((Action(COLOR,2000,100,red,green,blue),)) # Static color, 2 second duration, 100 tempo (who cares?)
        elc.finish_save_animation(DC_SLEEP)

        #Half brightness on Battery
        elc.remove_animation(DC_ON)
        elc.start_new_animation(DC_ON)
        elc.start_series(zones)
        elc.add_action((Action(COLOR,2000,100,int(red/2),int(green/2),int(blue/2)),)) # Static color, 2 second duration, 100 tempo (who cares?)
        elc.finish_save_animation(DC_ON)
        
        #Red flashing on battery low (untested)
        elc.remove_animation(DC_LOW)
        elc.start_new_animation(DC_LOW)
        elc.start_series(zones)
        elc.add_action((Action(COLOR,2000,100,255,0,0),)) # Static color, 2 second duration, 100 tempo (who cares?)
        elc.add_action((Action(COLOR,2000,100,0,0,0),)) # Static color, 2 second duration, 100 tempo (who cares?)
        elc.finish_save_animation(DC_LOW)

        #Off on boot, start and finish
        elc.remove_animation(DEFAULT_POST_BOOT)
        elc.start_new_animation(DEFAULT_POST_BOOT)
        elc.start_series(zones)
        elc.add_action((Action(COLOR,2000,100,0,0,0),)) # Static color, 2 second duration, 100 tempo (who cares?)
        elc.finish_save_animation(DEFAULT_POST_BOOT)
        elc.remove_animation(RUNNING_START)
        elc.start_new_animation(RUNNING_START)
        elc.start_series(zones)
        elc.add_action((Action(COLOR,2000,100,0,0,0),)) # Static color, 2 second duration, 100 tempo (who cares?)
        elc.finish_save_animation(RUNNING_START)
        elc.remove_animation(RUNNING_FINISH)
        elc.start_new_animation(RUNNING_FINISH)
        elc.start_series(zones)
        elc.add_action((Action(COLOR,2000,100,0,0,0),)) # Static color, 2 second duration, 100 tempo (who cares?)
        elc.finish_save_animation(RUNNING_FINISH)

if __name__ == "__main__":
	main()
