# Dell-G15-Led-Control
An insanely simple script to control keyboard brightness and color on Dell G15 (5525) Laptops. Untested on any other laptop, but can probably be used with models that have the ```Bus *** Device ***: ID 187c:0550 Alienware Corporation LED controller```

## Installation
No installation necessary, besides creating the udev rule ```/etc/udev/rules.d/00-aw-elc.rules```, and rebooting. Make sure the user is part of the ```plugdev``` group. Alternatively, run the script as root.
```
SUBSYSTEM=="usb", ATTRS{idVendor}=="187c", ATTRS{idProduct}=="0550", MODE="0660", GROUP="plugdev", SYMLINK+="awelc"
```
## Usage
```
awcc.py off                 -> Turn lights off.
awcc.py on                  -> Turn lights on.
awcc.py red green blue      -> With custom colors.
awcc.py on 255 255 255      -> Bright white
awcc.py on 128 128 128      -> Dim white
```
## Contributions
Written using the information and code from https://github.com/trackmastersteve/alienfx/issues/41. Please let me know if you'd like this repository removed!
