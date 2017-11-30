from picamera import PiCamera
from time import sleep
import argparse
import datetime as dt
import os
import sys

camera = PiCamera()
camera.vflip = True
camera.brightness = 70
camera.sharpness = 40
camera.contrast = 60
camera.saturation = 60
camera.exposure_mode = 'auto'


def record(rec_time, file_path):
    camera.start_recording(file_path)
    sleep(rec_time)
    camera.stop_recording()


def live_feed(feed):
    # live feed
    while feed:
        camera.start_preview()
        sleep(10)
        camera.stop_preview()


if __name__ == '__main__':
    input_parser = argparse.ArgumentParser()
    input_parser.add_argument("time", type=int,
                              help="Recording Time")
    input_parser.add_argument("-l", "--live", action="store_true",
                              help="live Feed")
    args = input_parser.parse_args()
    if args.live:
        live_feed(args.live)
    else:
        print("Recording")
        file_path = str(dt.date) + 'video.h264'
        record(args.time, file_path)
