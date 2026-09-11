"""第一个 OpenCV 示例：绘制图形并弹窗显示。

运行方式（在项目根目录）：
    .venv\\Scripts\\python.exe 01_hello_opencv.py

窗口会显示 3 秒，期间按任意键可提前关闭。
"""
import cv2
import numpy as np

# 生成一张黑色背景图（高 480，宽 640，3 通道 BGR）
img = np.zeros((480, 640, 3), dtype=np.uint8)

# 画图形和文字
cv2.circle(img, (320, 240), 100, (0, 255, 0), 3)              # 绿色圆环
cv2.rectangle(img, (120, 320), (300, 430), (255, 0, 0), 2)    # 蓝色矩形
cv2.putText(img, "Hello, OpenCV!", (150, 120),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)

# 弹窗显示
cv2.imshow("Hello OpenCV", img)
cv2.waitKey(3000)  # 等待 3000 毫秒（按任意键提前关闭）
cv2.destroyAllWindows()

print("示例运行完成，窗口已关闭")
