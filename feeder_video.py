#!/usr/bin/python3
# You need to install PIL to run this script
# type "sudo apt-get install python-imaging-tk" in an terminal window to do this

import subprocess, socket, os, shutil, time, picamera, signal
from io import StringIO
from datetime import datetime
from PIL import Image
from rpi_info import name
from camera_settings import *
from sigterm_exception import *

filepath = "/home/pi/APAPORIS/CURRENT/"
moved_path = "/home/pi/APAPORIS/MOVED/"
filenamePrefix = name
video_duration = 60


def make_video(hour):
    global filepath
    global moved_path
    with picamera.PiCamera() as camera:
        #change these values in camera_settings on github and push to all pis for quick universal changes
        camera.rotation = camera_rotation
        camera.resolution = camera_resolution
        camera.brightness = camera_brightness
        camera.sharpness = camera_sharpness
        camera.contrast = camera_contrast
        camera.awb_mode = camera_awb_mode
        camera.iso = camera_ISO
        camera.exposure_mode, _shutter_speed = set_exposure_shutter(hour)
        camera.framerate = camera_framerate
        filename = "{}_{}.h264".format(filenamePrefix,datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        camera.annotate_text_size = 15
        camera.start_recording(filepath + filename)
        start = datetime.now()
        while (datetime.now()-start).seconds < video_duration:
            camera.annotate_text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')        	
            camera.wait_recording(0.5)
        camera.stop_recording()
        
        os.rename(filepath + filename, moved_path + filename)


signal.signal(signal.SIGTERM, signal_handler)

#try:
#    while True:
#        hour = datetime.now().hour
#        if hour >= feeder_start and hour < feeder_end:
#            dir_name = make_video(hour)
#            shutil.move(dir_name,moved_path)
#        else:
#            pass

dir_name = make_video(hour)
shutil.move(dir_name,moved_path)
            
            
#except (SigTermException, KeyboardInterrupt):
#    try:
#        shutil.move(dir_name,moved_path)
#    except:
#        print("failed to move directory")
#    finally:
#        sys.exit()
