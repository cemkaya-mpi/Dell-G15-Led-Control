#!/usr/bin/python3

from elc import *
from elc_constants import *
import binascii

# For this script, we are setting up the power zones
# Since the 'power' zones can be anything, we are going to use
# zones 0 and 3 (outside and inside alien heads)

# We aren't setting behavior for any of the other zones, so let's hope
# that the other slots aren't going to interfere, since that looks ugly.

def main():
	vid=0x187C
	pid=0x0550
	elc=Elc(vid,pid,debug=1)

	print("Setting AC SLEEP")
	elc.remove_animation(AC_SLEEP)
	elc.start_new_animation(AC_SLEEP)
	elc.start_series((0,3))

	# Fade from #00F0F0 to Black (#000000), 1 second duration, 100 tempo
	elc.add_action((Action(MORPH,1000,100,0,255,0),Action(MORPH,1000,100,0,0,0)))
	elc.finish_save_animation(AC_SLEEP)

	print("Setting AC CHARGED")
	elc.remove_animation(AC_CHARGED)
	elc.start_new_animation(AC_CHARGED)
	elc.start_series((0,3))

	# Static color (#00F0F0), 2 second duration, 100 tempo (who cares?)
	elc.add_action((Action(COLOR,2000,100,0,255,0),))
	elc.finish_save_animation(AC_CHARGED)

	print("Setting AC CHARGING")
	elc.remove_animation(AC_CHARGING)
	elc.start_new_animation(AC_CHARGING)
	elc.start_series((0,3))

	# Fade from #00F0F0 to #FF9900
	elc.add_action((Action(MORPH,1000,100,0,255,0),Action(MORPH,1000,100,255,153,0)))
	elc.finish_save_animation(AC_CHARGING)

	print("Setting DC SLEEP")
	elc.remove_animation(DC_SLEEP)
	elc.start_new_animation(DC_SLEEP)
	elc.start_series((0,3))

	# Fade from #FF9900 to Black, 1 second duration, 100 tempo
	elc.add_action((Action(MORPH,1000,100,255,153,00),Action(MORPH,1000,100,0,0,0)))
	elc.finish_save_animation(DC_SLEEP)

	print("Setting DC ON")
	elc.remove_animation(DC_ON)
	elc.start_new_animation(DC_ON)
	elc.start_series((0,3))

	# Static color (#FF9900), 2 second duration, 100 tempo (who cares?)
	elc.add_action((Action(COLOR,2000,100,255,153,0),))
	elc.finish_save_animation(DC_ON)

	print("Setting DC LOW")
	elc.remove_animation(DC_LOW)
	elc.start_new_animation(DC_LOW)
	elc.start_series((0,3))

	# Static color (#FF0000), 2 second duration, 100 tempo (who cares?)
	elc.add_action((Action(COLOR,2000,100,255,0,0),))
	elc.finish_save_animation(DC_LOW)


if __name__ == "__main__":
	main()
