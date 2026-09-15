import cv2

map = cv2.VideoCapture(0)

while True:
    ret, frame = map.read()
    if not ret:
        print("读取失败")
        break

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

map.release()
cv2.destroyAllWindows()