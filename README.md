# Edi-Safe-Tank
Safe fish tank with Intel Edison

## Host-setup
Host is your computer that will communicate with Edison

There are two major ways to controll MeArm servos.
### Adafruit Servo Driver
```shell
# Install libffi-dev package
opkg install libffi-dev

# Install smbus-cffi
pip install cffi
pip install smbus-cffi
```

### Pololu Micro Maestro
We may need install maestro-linux.
There is a readme.txt file in tar file, which tell you about how to install it
in Ubuntu but not in Fedora. Here are the required packages in Fedora
```shell
sudo yum install mono-basic libusb-devel
```

## Edison-Setup
Install opencv through opkg package manager
```shell
vi /etc/opkg/base-feeds.conf

src/gz all http://repo.opkg.net/edison/repo/all
src/gz edison http://repo.opkg.net/edison/repo/edison
src/gz core2-32 http://repo.opkg.net/edison/repo/core2-32

opkg update

opkg install python-numpy
opkg install opencv python-opencv

python
>>> import numpy
>>> import cv2
```
