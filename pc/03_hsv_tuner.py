import cv2
import numpy as np

cap = cv2.VideoCapture('evidence/stage2/output.mp4')

cv2.namedWindow("mask")
cv2.createTrackbar("H", "mask", 32, 180, lambda x: None)


while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    h = cv2.getTrackbarPos("H", "mask")
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (h-10, 100, 100), (h+10, 255, 255))
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    cv2.imshow("mask", np.hstack((mask_bgr, frame)))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
