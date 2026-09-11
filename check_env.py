"""OpenCV 环境自检脚本。

运行方式（在项目根目录）：
    .venv\\Scripts\\python.exe check_env.py

不依赖外部图片，不弹窗，可反复运行。
"""
import sys
from pathlib import Path

import cv2
import numpy as np

print("=" * 48)
print("OpenCV 环境自检")
print("=" * 48)
print(f"Python 版本 : {sys.version.split()[0]}")
print(f"OpenCV 版本 : {cv2.__version__}")
print(f"NumPy  版本 : {np.__version__}")

# 1. 构造测试图：黑色背景 + 绿色实心圆 + 文字（不依赖外部图片）
img = np.zeros((240, 320, 3), dtype=np.uint8)
cv2.circle(img, (160, 120), 80, (0, 255, 0), -1)  # 注意 BGR 通道顺序
cv2.putText(img, "OpenCV OK", (60, 130),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
print(f"测试图像尺寸 : {img.shape} (高, 宽, 通道)")

# 2. 灰度转换 + Canny 边缘检测
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)

# 3. 写入磁盘，验证读写链路
out_dir = Path(__file__).parent / "output"
out_dir.mkdir(exist_ok=True)
ok1 = cv2.imwrite(str(out_dir / "check_circle.png"), img)
ok2 = cv2.imwrite(str(out_dir / "check_edges.png"), edges)
print(f"图像写入     : circle={'成功' if ok1 else '失败'}, "
      f"edges={'成功' if ok2 else '失败'}")

# 4. 常用模块可用性抽查
checks = {
    "图像 GUI (imshow)": hasattr(cv2, "imshow"),
    "DNN 深度神经网络": hasattr(cv2, "dnn"),
    "SIFT 特征提取": hasattr(cv2, "SIFT_create"),
    "ArUco 标记检测": hasattr(cv2, "aruco"),
    "相机标定": hasattr(cv2, "calibrateCamera"),
}
print("-" * 48)
for name, ok in checks.items():
    print(f"{name:<20}: {'可用' if ok else '不可用'}")

print("=" * 48)
print("[OK] 环境自检通过，OpenCV 可以正常使用")
