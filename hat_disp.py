# Control LED matrix display on SenseHat
#
#
from sense_hat import SenseHat


class HatDisp:
    b = (0, 0, 255)
    r = (255, 0, 0)
    g = (0, 255, 0)
    k = (0, 0, 0)

    def __init__(self):
        self.sense = SenseHat()

    def show_stop(self):
        k = self.k
        g = self.g
        stop_icon = [
            k, k, k, k, k, k, k, k,
            k, g, g, g, g, g, g, k,
            k, g, g, g, g, g, g, k,
            k, g, g, g, g, g, g, k,
            k, g, g, g, g, g, g, k,
            k, g, g, g, g, g, g, k,
            k, g, g, g, g, g, g, k,
            k, k, k, k, k, k, k, k
        ]
        self.sense.set_pixels(stop_icon)

    def show_rec(self):
        k = self.k
        r = self.r
        rec_icon = [
            k, k, k, k, k, k, k, k,
            k, k, r, r, r, r, k, k,
            k, r, r, r, r, r, r, k,
            k, r, r, r, r, r, r, k,
            k, r, r, r, r, r, r, k,
            k, r, r, r, r, r, r, k,
            k, k, r, r, r, r, k, k,
            k, k, k, k, k, k, k, k
        ]
        self.sense.set_pixels(rec_icon)

    def show_msg(self, msg_txt):
        self.sense.show_message(msg_txt)
