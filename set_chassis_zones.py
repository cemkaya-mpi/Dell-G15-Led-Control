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

	elc.start_new_animation(RUNNING_START)
	elc.start_series((1,2,8,9,10,11))
	elc.add_action((Action(COLOR,500,100,0,255,0),Action(COLOR,500,100,255,255,255),Action(COLOR,500,100,255,136,0)))

	elc.finish_play_animation(RUNNING_FINISH)


if __name__ == "__main__":
	main()
