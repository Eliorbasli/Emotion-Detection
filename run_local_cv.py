# Run this file on CV2 in local machine to construct a Concentration Index (CI).


from util.analysis_realtime import analysis
import cv2
import numpy as np

# Initializing
cap = cv2.VideoCapture(0)
ana = analysis()

# Capture every frame and send to detector
while True:
    _, frame = cap.read()
    bm = ana.detect_face(frame) #from analysis_realtime

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
# Exit if 'q' is pressed
    if key == ord('q'):
        break

# Release the memory
cap.release()
cv2.destroyAllWindows()
