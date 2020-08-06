import sys
from picamera import PiCamera
from sense_hat import SenseHat, ACTION_RELEASED
from hat_disp import HatDisp
from signal import pause

"""
Camera setting
"""
camera = PiCamera()
camera.rotation = 180
camera.resolution = (1920, 1080)
camera.framerate = 30
"""
Settings for display on Sensor Hat
"""
hat_disp = HatDisp()
hat_disp.show_stop()

sense = SenseHat()

recording = False
operation = True


def exit_prog(event):
    global operation
    if event.action == ACTION_RELEASED:
        operation = False
        hat_disp.show_msg("Bye!")
        sys.exit(0)


def start_stop_rec(event):
    global recording, camera
    if event.action == ACTION_RELEASED:
        if recording:
            camera.stop_recording()
            hat_disp.show_stop()
        else:
            camera.start_recording('/home/pi/Videos/video.h264')
            hat_disp.show_rec()
        recording = not recording


# assign callback functions for joystick inputs
sense.stick.direction_up = exit_prog
sense.stick.direction_middle = start_stop_rec

# main
sense.clear()
hat_disp.show_msg("Ready.")
hat_disp.show_stop()
pause()
