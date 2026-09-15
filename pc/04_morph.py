import cv2
import numpy as np

cap = cv2.VideoCapture('evidence/stage2/output.mp4')

kernel = np.ones((5,5),np.uint8)
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
    mask_erode = cv2.erode(mask, kernel, iterations=1)
    mask_clean = cv2.dilate(mask_erode, kernel, iterations=1)
    cv2.imshow("mask", np.hstack((mask, mask_clean)))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()