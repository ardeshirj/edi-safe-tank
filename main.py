import numpy as np
import cv2

# Arm will pick up the test strip
# Dip it in water for 5 seconds
# Move it in front of the camera

# Take a picture after 10-15 seconds

# For each chemical unsafe boundaries
#   If the result is not complete black (requires clear background)
#       then the water is in unsafe condition for that chemical

image = cv2.imread('example.jpg', 1)

safe_boundaries = [
    # [G, B, R] (Higher, Lower)
    ([195, 199, 224], [218, 223, 236]),  # NO3 and NO2
    ([118, 57, 228], [214, 101, 254]),   # PH
    ([187, 155, 132], [230, 160, 237]),  # KH
    ([158, 173, 102], [216, 204, 166]),  # GH
]

unsafe_boundaries = [
    # [G, B, R] (Higher, Lower)
    ([128, 146, 211], [188, 195, 239]),  # NO3 and NO2
    ([67, 82, 219], [92, 71, 213]),      # PH
    ([166, 163, 86], [210, 184, 146]),   # KH
    ([83, 127, 54], [150, 171, 105]),    # GH
]

for (lower, upper) in safe_boundaries:
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    cv2.imwrite('mask.jpg', mask)
    cv2.imwrite('result.jpg', output)
