"""
Simple control of Maestro.
Maestro user doc: https://www.pololu.com/docs/0J40

This code initially was written by a guest instructor.
"""

from time import sleep
import serial

DEVICE = 12
PULSE_WIDTH_MAX = 2500
PULSE_WIDTH_MIN = 1000


class ServoController(object):

    def __init__(self, tty, baud):
        """Take serial connection needed to communicate with Maestro."""
        self.connection = get_serial(tty, baud)

    def set_target(self, servo, pulse_width):
        """
        Move given servo to given pulse width
        (range [PULSE_WIDTH_MIN, PULSE_WIDTH_MAX], 0 disables servo).
        """
        if (pulse_width != 0) and (
           pulse_width < PULSE_WIDTH_MIN or pulse_width > PULSE_WIDTH_MAX):
            return

        pulse_width = pulse_width * 4
        cmd = chr(0xaa) + chr(DEVICE & 0x7f) + chr(0x04) + chr(servo & 0x7f) \
            + chr(pulse_width & 0x7f) + chr((pulse_width >> 7) & 0x7f)

        self.connection.write(cmd)
        sleep(1)

    def get_position(self, servo):
        """Get position of given servo as pulse width."""
        cmd = chr(0xaa) + chr(DEVICE & 0x7f) + chr(0x10) + chr(servo & 0x7f)
        self.connection.write(cmd)

        byte1 = self.connection.read()
        byte2 = self.connection.read()

        return int((ord(byte1) | (ord(byte2) << 8)) / 4)

    def reset_position(self):
        self.set_target(0, 2150)
        sleep(1)
        self.set_target(1, 1700)
        sleep(1)
        self.set_target(2, 2100)
        sleep(1)
        self.set_target(3, 1760)


def get_serial(tty, baud):
    """Retrieve and open UART connection to Maestro."""
    ser = serial.Serial()
    ser.port = tty
    ser.baudrate = baud
    ser.timeout = 0.5
    ser.open()
    return ser
