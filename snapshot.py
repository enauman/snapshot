#!/usr/bin/python
from time import sleep
from picamera import PiCamera
import argparse
parser = argparse.ArgumentParser(description="one shot script")
parser.add_argument('-hf','--hflip', help='flip horizontally if True, default False',required=False)
parser.add_argument('-vf','--vflip',help='flip vertically if True, default False', required=False)
args = parser.parse_args()
camera = PiCamera(resolution=(1280, 720), framerate=30)
# Set ISO to the desired value
camera.iso = 200
# Wait for the automatic gain control to settle
sleep(2)
# Now fix the values
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g
camera.hflip = args.hflip
print('hflip = ',camera.hflip)
camera.vflip = args.vflip
print('vflip = ',camera.vflip)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('snap.jpg')
camera.close()
