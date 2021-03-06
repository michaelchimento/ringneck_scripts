#!/usr/bin/python3

from datetime import datetime

camera_rotation = 0
camera_resolution = (3280, 2464)
social_camera_resolution = (3280, 2464)
camera_color_effects = (128,128)
focus_zoom = (0.25, 0.25, 0.5, 0.5)
feeder_zoom = (0, 0, 1, 1)
observ_zoom = (0, 0, 1, 1)
social_zoom = (0, 0, 1, 1)
resize_scale = .6
feeder_resize_scale = .8
camera_ISO = 0
camera_brightness = 40
camera_shutter_speed = 3500
camera_framerate = 30
camera_exposure_mode = 'auto'
camera_awb_mode = 'tungsten'
camera_sharpness = 30
camera_contrast = 25
feeder_start = 6
feeder_end = 20
social_start = 6
social_end = 20
puzzle_start = 6
puzzle_end = 20
observ_start = 6
observ_end = 20
sensitivity_value = 200

def set_exposure_shutter(hour):
    if hour < 8:
        camera_exposure_mode = 'auto'
        camera_shutter_speed = 3000   
    elif hour < 10 and hour >=8:
        camera_exposure_mode = 'auto'
        camera_shutter_speed = 2500
    elif hour >= 10 and hour < 16:
        camera_exposure_mode = 'auto'
        camera_shutter_speed = 1500
    elif hour >= 16 and hour < 19:
        camera_exposure_mode = 'auto'
        camera_shutter_speed = 2500
    else:
        camera_exposure_mode = 'auto'
        camera_shutter_speed = 3000

    return camera_exposure_mode, camera_shutter_speed
