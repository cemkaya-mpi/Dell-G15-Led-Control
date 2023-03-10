#!/usr/bin/python3

# Major Commands
ELC_QUERY=0x20
USER_ANIMATION=0x21
POWER_ANIMATION=0x22
START_SERIES=0x23
ADD_ACTION=0x24
SET_EVENT=0x25
DIMMING=0x26
SET_COLOR=0x27
RESET=0x28
SPI_FLASH=0xFF

# ELC_QUERY Subcommands
GET_VERSION=0x00
GET_STATUS=0x01
GET_PLATFORM=0x02
GET_ANIMATION_COUNT=0x03
GET_ANIMATION_BY_ID=0x04
READ_SERIES=0x05

# Animation Subcommands
START_NEW=0x01
FINISH_SAVE=0x02
FINISH_PLAY=0x03
REMOVE=0x04
PLAY=0x05
SET_DEFAULT=0x06
SET_STARTUP=0x07

# Action Effect codes
COLOR=0x00
PULSE=0x01
MORPH=0x02

# Animation ID's
AC_SLEEP=0x5b
AC_CHARGED=0x5c
AC_CHARGING=0x5d
DC_SLEEP=0x5e
DC_ON=0x5f
DC_LOW=0x60
DEFAULT_POST_BOOT=0x61
RUNNING_START=0xFFFF
RUNNING_FINISH=0x00FF
