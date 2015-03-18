from time import sleep
import maestro

if __name__ == "__main__":
    controller = maestro.ServoController('/dev/ttyACM0', 9600)
    controller.reset_position()
