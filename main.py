from time import sleep
import maestro
import numpy as np
import cv2

THRESHOLD = 200

if __name__ == "__main__":

    # controller = maestro.ServoController('/dev/ttyACM0', 9600)
    #
    # # Close the claw
    # controller.set_target(3, 1850)
    #
    # # Rotate 45 degree
    # controller.set_target(0, 1600)
    #
    # # Dip the strip to water
    # controller.set_target(1, 1200)
    #
    # # Move back up
    # controller.set_target(1, 1700)
    #
    # # Rotate 45 degree
    # controller.set_target(0, 1200)
    #
    # # Bring it to the front of the camera
    # controller.set_target(1, 1440)
    # controller.set_target(2, 2380)

    # cap = cv2.VideoCapture(0)

    # Setup the camera manually if needed
    # while(True):
    #     # Capture frame-by-frame
    #     ret, frame = cap.read()
    #
    #     # Display the resulting frame
    #     cv2.imshow('frame', frame)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    #
    # # When everything done, release the capture
    # cap.release()
    # cv2.destroyAllWindows()

    # ret, frame = cap.read()
    # sleep(5)
    # cv2.imwrite('example.jpg', frame)

    # Reset the arm position
    # controller.reset_position()

    image = cv2.imread('example.jpg', 1)

    # safe_boundaries = [
    #     # [G, B, R] (Higher, Lower)
    #     ([195, 199, 224], [218, 223, 236]),  # NO3 and NO2
    #     ([118, 57, 228], [214, 101, 254]),   # PH
    #     ([187, 155, 132], [230, 160, 237]),  # KH
    #     ([158, 173, 102], [216, 204, 166]),  # GH
    # ]
    #
    unsafe_boundaries = [
        # [G, B, R] (Higher, Lower)
        ([128, 146, 211], [188, 195, 239]),  # NO3 and NO2
        ([67, 82, 219], [92, 71, 213]),      # PH
        ([166, 163, 86], [210, 184, 146]),   # KH
        ([83, 127, 54], [150, 171, 105]),    # GH
    ]

    # GH_unsafe_boundaries = [([83, 127, 54], [150, 171, 105])]

    element = 0
    safe = True
    for (lower, upper) in unsafe_boundaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        mask = cv2.inRange(image, lower, upper)
        result = cv2.bitwise_and(image, image, mask=mask)

        # cv2.imwrite('mask.jpg', mask)
        # cv2.imwrite('result.jpg', result)

        if cv2.countNonZero(mask) > THRESHOLD:
            safe = False

        if element == 0 and not safe:
            print "NO3 & N02 are not safe"
        elif element == 0 and safe:
            print "NO3 & N02 are safe"
        elif element == 1 and not safe:
            print "PH is not safe"
        elif element == 1 and safe:
            print "PH is safe"
        elif element == 2 and not safe:
            print "KH is not safe"
        elif element == 2 and safe:
            print "KH is safe"
        elif element == 3 and not safe:
            print "GH is not safe"
        elif element == 3 and safe:
            print "GH is safe"

        element += 1
