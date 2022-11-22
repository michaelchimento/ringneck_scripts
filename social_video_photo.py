#!/usr/bin/python3
import subprocess, socket, os, shutil, time, picamera, signal, sys, traceback
from io import StringIO
from datetime import datetime
from PIL import Image
from rpi_info import name
from camera_settings import *
from sigterm_exception import *

filepath = "/home/pi/APAPORIS/CURRENT/"
moved_path_video = "/home/pi/APAPORIS/MOVED/video/"
moved_path_photo = "/home/pi/APAPORIS/MOVED/photo"
filenamePrefix = name
video_duration = 30

def crop_folder(directory):
    for item in os.listdir(directory):
        try:
            fullpath = directory+"/"+item
            if os.path.isfile(fullpath):
                im = Image.open(fullpath)
                imCrop = im.crop((0,1080/5,1920,1080/5*4))
                imCrop.save(fullpath, 'JPEG', quality=100)
        except Exception:
            raise Exception

def make_video(hour):
    global filepath
    global moved_path_video
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
        print("recording " + filename)
        camera.annotate_text_size = 15
        camera.start_recording(filepath + filename)
        start = datetime.now()
        while (datetime.now()-start).seconds < video_duration:
            camera.annotate_text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')        	
            camera.wait_recording(0.5)
        camera.stop_recording()
    os.rename(filepath + filename, moved_path_video + filename)

def make_photos(hour):
    global filepath
    global moved_path_photo
    with picamera.PiCamera() as camera:
        camera.rotation = camera_rotation
        camera.zoom = social_zoom
        camera.resolution = social_camera_resolution
        camera.brightness = camera_brightness
        camera.sharpness = camera_sharpness
        camera.contrast = camera_contrast
        camera.awb_mode = camera_awb_mode
        camera.color_effects = camera_color_effects
        camera.exposure_mode, camera.shutter_speed, camera.iso = set_exposure_shutter(hour)
        time_stamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        dir_name = '{}{}_{}'.format(filepath,filenamePrefix,time_stamp)
        os.mkdir(dir_name)
        camera.annotate_text_size = 15
        camera.annotate_text = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
        resize_tuple = (int(resize_scale*camera.resolution[0]),int(resize_scale*camera.resolution[1]))
        try:        
            print("Beginning new photo round")
            for i, filename in enumerate(camera.capture_continuous("{}/{}_".format(dir_name,filenamePrefix)+"{timestamp:%Y-%m-%d-%H-%M-%S-%f}.jpg", resize = resize_tuple, quality = 100)):
                camera.annotate_text = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')
                time.sleep(1)
                if i == 599:
                    return dir_name
        except Exception as e:
            print("Exception during photo capture: {}".format(e))
            return dir_name

signal.signal(signal.SIGTERM, signal_handler)

try:
    while True:
        hour = datetime.now().hour
        if (hour >= social_photos_start1 and hour < social_photos_end1) or (hour >= social_photos_start2 and hour < social_photos_end2):
            dir_name = make_photos(hour)
            #crop_folder(dir_name)
            shutil.move(dir_name,moved_path_photo)  
        elif (hour == social_videos_start):      
            make_video(hour)
        else:
            pass
except:
    traceback.print_exc()
