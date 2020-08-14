import time
import datetime
from picamera import PiCamera
from sense_hat import SenseHat, ACTION_RELEASED
from hat_disp import HatDisp


"""
Camera settings
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
operating = True


def exit_prog(event):
    global operating
    if event.action == ACTION_RELEASED:
        operating = False


def start_stop_rec(event):
    global recording
    if event.action == ACTION_RELEASED:
        recording = not recording
        print('Recording = ' + str(recording))


# assign callback functions for joystick inputs
sense.stick.direction_up = exit_prog
sense.stick.direction_middle = start_stop_rec


def stop_recording(camera):
    try:
        camera.stop_recording()
        print('Stop recording.')
    except Exception as e:
        print(e)


# main
sense.clear()
hat_disp.show_msg("Ready.")
hat_disp.show_stop()

# main loop
while operating:
    if recording:
        if not camera.recording:
            dt_now = datetime.datetime.now()
            file_name = '/home/pi/Videos/video' + \
                dt_now.strftime('%Y%m%d%H%M%S')+".h264"
            camera.start_recording(file_name)
            hat_disp.show_rec()
            print('Recording start...')
    else:
        if camera.recording:
            recording = False
            hat_disp.show_stop()
            stop_recording(camera)
    time.sleep(0.1)

# Terminate process
if camera.recording:
    stop_recording(camera)
camera.close()
hat_disp.show_msg("Bye!")
