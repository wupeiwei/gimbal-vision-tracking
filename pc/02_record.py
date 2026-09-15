import cv2

cap = cv2.VideoCapture(0)
""" print(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) """
video = cv2.VideoWriter('evidence/stage2/red_ball_01.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        print("读取失败")
        break

    cv2.imshow("frame", frame)
    video.write(frame)
      
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
video.release()
cv2.destroyAllWindows()