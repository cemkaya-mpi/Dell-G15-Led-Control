#!/usr/bin/python3
import sys
import random
from elc import *
from elc_constants import *


DURATION_MAX=0xffff
DURATION_BATTERY_LOW=0xff
DURATION_MIN=0x00
TEMPO_MAX=0xff
TEMPO_MIN=0x01

def main():
    command = "on"
    red = 0
    green = 0
    blue = 0
    dim=255
    if (len(sys.argv) == 5):  # With rgb values given by user
        command = sys.argv[1]
        red = int(sys.argv[2])
        green = int(sys.argv[3])
        blue = int(sys.argv[4])
        dim=0
    elif (len(sys.argv) == 2):  # No rgb values specified.
        command = sys.argv[1]
        if (command == "on"):
            red = 255
            green = 255
            blue = 255
            dim=0
        elif (command == "off"):
            red = 0
            green = 0
            blue = 0
            dim=255
        elif (command == "morph"):  # Random morph colors
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            dim=0
    else:
        print("Usage:")
        print("awcc.py off                      -> Turn lights off.")
        print("awcc.py on                       -> Turn lights on, white.")
        print("awcc.py on red green blue        -> Turn lights on, with given colors.")
        print("awcc.py morph                    -> Turn lights on, with morph effect, random colors.")
        print("awcc.py morph red green blue     -> Turn lights on, with morph effect, given colors.")
        print()
        print("Range for red,green,blue is 0-255")
        print("eg.: awcc.py on 255 255 255      -> Bright white")
        print("eg.: awcc.py on 128 128 128      -> Dim white")

    print("Operation:%s" % (command))
    print("Red:%d, Green:%d, Blue:%d" % (red, green, blue))
    # So that we don't get an USB device busy error
    device = usb.core.find(idVendor=0x187c, idProduct=0x0550)
    ep = device[0].interfaces()[0].endpoints()[0]
    i = device[0].interfaces()[0].bInterfaceNumber
    device.reset()
    if device.is_kernel_driver_active(i):
        device.detach_kernel_driver(i)
    # Create the elc object
    vid = 0x187C
    pid = 0x0550
    elc = Elc(vid, pid, debug=0)

    # Define zones
    zones = [0, 1, 2, 3]

    # White color is default, test this line to see if it works at all!
    # elc.set_color(zones,red,green,blue) # White
    
    # elc.dim(zones, dim)                # No dimming

    # Off on AC Sleep
    elc.remove_animation(AC_SLEEP)
    elc.start_new_animation(AC_SLEEP)
    elc.start_series(zones)
    # Static color, 2 second duration, tempo tempo (who cares?)
    elc.add_action((Action(COLOR, DURATION_MAX, TEMPO_MAX, 0, 0, 0),))
    elc.finish_save_animation(AC_SLEEP)

    # Full brightness on AC, charged
    elc.remove_animation(AC_CHARGED)
    elc.start_new_animation(AC_CHARGED)
    elc.start_series(zones)
    if command == "morph":
        elc.add_action((Action(MORPH, DURATION_MAX, TEMPO_MIN, red, green, blue), Action(MORPH, DURATION_MAX, TEMPO_MIN, green,
                       blue, red), Action(MORPH, DURATION_MAX, TEMPO_MIN, blue, red, green)))  # Morph based on given values.
    else:
        # Static color, 2 second duration, tempo tempo (who cares?)
        elc.add_action((Action(COLOR, DURATION_MAX, TEMPO_MAX, red, green, blue),))

    elc.finish_save_animation(AC_CHARGED)

    # Full brightness on AC, charging
    elc.remove_animation(AC_CHARGING)
    elc.start_new_animation(AC_CHARGING)
    elc.start_series(zones)
    if command == "morph":
        elc.add_action((Action(MORPH, DURATION_MAX, TEMPO_MIN, red, green, blue), Action(MORPH, DURATION_MAX, TEMPO_MIN, green,
                       blue, red), Action(MORPH, DURATION_MAX, TEMPO_MIN, blue, red, green)))  # Morph based on given values.
    else:
        # Static color, 2 second duration, tempo tempo (who cares?)
        elc.add_action((Action(COLOR, DURATION_MAX, TEMPO_MAX, red, green, blue),))

    elc.finish_save_animation(AC_CHARGING)

    # Off on DC Sleep
    elc.remove_animation(DC_SLEEP)
    elc.start_new_animation(DC_SLEEP)
    elc.start_series(zones)
    # Static color, 2 second duration, tempo tempo (who cares?)
    elc.add_action((Action(COLOR, DURATION_MAX, TEMPO_MAX, 0, 0, 0),))
    elc.finish_save_animation(DC_SLEEP)

    # Half brightness on Battery
    elc.remove_animation(DC_ON)
    elc.start_new_animation(DC_ON)
    elc.start_series(zones)
    if command == "morph":
        elc.add_action((Action(MORPH, DURATION_MAX, TEMPO_MIN, int(red/2), int(green/2), int(blue/2)), Action(MORPH, DURATION_MAX, TEMPO_MIN, int(green/2),
                       int(blue/2), int(red/2)), Action(MORPH, DURATION_MAX, TEMPO_MIN, int(blue/2), int(red/2), int(green/2))))  # Morph based on given values.
    else:
        # Static color, 2 second duration, tempo tempo (who cares?)
        elc.add_action(
            (Action(COLOR, DURATION_MAX, TEMPO_MAX, int(red/2), int(green/2), int(blue/2)),))

    elc.finish_save_animation(DC_ON)

    # Red flashing on battery low. Use custom tempo
    elc.remove_animation(DC_LOW)
    elc.start_new_animation(DC_LOW)
    elc.start_series(zones)
    # Static color, 2 second duration, tempo tempo (who cares?)
    elc.add_action((Action(COLOR, DURATION_BATTERY_LOW, TEMPO_MIN, 255, 0, 0),))
    # Static color, 2 second duration, tempo tempo (who cares?)
    elc.add_action((Action(COLOR, DURATION_BATTERY_LOW, TEMPO_MIN, 0, 0, 0),))
    elc.finish_save_animation(DC_LOW)

    # Off on boot, start and finish
    elc.remove_animation(DEFAULT_POST_BOOT)
    elc.start_new_animation(DEFAULT_POST_BOOT)
    elc.start_series(zones)
    # Static color, 2 second duration, tempo tempo (who cares?)
    elc.add_action((Action(COLOR, DURATION_MAX, TEMPO_MAX, 0, 0, 0),))
    elc.finish_save_animation(DEFAULT_POST_BOOT)
    elc.remove_animation(RUNNING_START)
    elc.start_new_animation(RUNNING_START)
    elc.start_series(zones)
    # Static color, 2 second duration, tempo tempo (who cares?)
    elc.add_action((Action(COLOR, DURATION_MAX, TEMPO_MAX, 0, 0, 0),))
    elc.finish_save_animation(RUNNING_START)
    elc.remove_animation(RUNNING_FINISH)
    elc.start_new_animation(RUNNING_FINISH)
    elc.start_series(zones)
    # Static color, 2 second duration, tempo tempo (who cares?)
    elc.add_action((Action(COLOR, DURATION_MAX, TEMPO_MAX, 0, 0, 0),))
    elc.finish_save_animation(RUNNING_FINISH)
    # if not device.is_kernel_driver_active(i):
    #     device.attach_kernel_driver(i)

if __name__ == "__main__":
    main()
