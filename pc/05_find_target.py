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
        """ break """

    h = cv2.getTrackbarPos("H", "mask")
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (h-10, 100, 100), (h+10, 255, 255))
    mask_erode = cv2.erode(mask, kernel, iterations=1)
    mask_clean = cv2.dilate(mask_erode, kernel, iterations=1)

    contours,_ = cv2.findContours(mask_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        area = cv2.contourArea(c)
        if area > 1000:
            bx, by, bw,bh = cv2.boundingRect(c)
            cv2.rectangle(frame, (bx, by), (bx+bw, by+bh), (0, 255, 0), 2)
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)

    mask_clean_bgr = cv2.cvtColor(mask_clean, cv2.COLOR_GRAY2BGR)
    cv2.imshow("mask", np.hstack((mask_clean_bgr, frame)))
        
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()