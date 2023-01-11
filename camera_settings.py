#!/usr/bin/python3

from datetime import datetime

camera_rotation = 0
camera_resolution = (1640, 1232)
social_camera_resolution = (3280, 2464)
camera_color_effects = None
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
camera_shutter_speed = 'auto'
camera_awb_mode = 'tungsten'
camera_sharpness = 30
camera_contrast = 25
feeder_start = 8
feeder_end = 17
social_start = 8
social_end = 17
social_photos_start1 = 8
social_photos_end1 = 930
social_photos_start2 = 1030
social_photos_end2 = 17
social_videos_start = 930
puzzle_start = 6
puzzle_end = 20
observ_start = 6
observ_end = 20
sensitivity_value = 200

def set_exposure_shutter(hour):
    if hour < 8:
        camera_exposure_mode = 'auto'
        camera_shutter_speed = 33330
        camera_ISO = 0
    elif hour < 10 and hour >=8:
        camera_exposure_mode = 'auto'
        camera_shutter_speed = 16600
        camera_ISO = 0
    elif hour >= 10 and hour < 13:
        camera_exposure_mode = 'auto'
        camera_shutter_speed = 8000
        camera_ISO = 0
    elif hour >= 13 and hour < 15:
        camera_exposure_mode = 'auto'
        camera_shutter_speed = 8000
        camera_ISO = 0
    elif hour >= 15 and hour < 16:
        camera_exposure_mode = 'auto'
        camera_shutter_speed = 12000
        camera_ISO = 800
    elif hour >= 16 and hour < 17:
        camera_exposure_mode = 'auto'
        camera_shutter_speed = 16600
        camera_ISO = 16600
    else:
        camera_exposure_mode = 'auto'
        camera_shutter_speed = 3000
        camera_ISO = 0

    return camera_exposure_mode, camera_shutter_speed, camera_ISO
