# 云台视觉跟踪自瞄

基于 **OpenCV + STM32** 的视觉追踪云台学习项目。

PC 端用 OpenCV 识别目标并计算像素偏差，通过串口把偏差发送给 STM32；STM32 在本地做 PID 闭环，驱动二自由度云台追踪目标。

## 系统架构

```
摄像头 → PC（OpenCV 识别目标 / 计算偏差）→ 串口 → STM32（PID 闭环）→ 云台舵机
```

- **PC 端**：Python + OpenCV，负责视觉识别与偏差计算，只发"看见什么"，不做闭环
- **STM32 端**：接收偏差，PID 计算角度增量，输出 PWM 控制云台

## 学习路线与进度

| 阶段 | 内容 | 状态 |
|---|---|---|
| 0 | 环境准备与基线 | 进行中 |
| 1 | 串口通信闭环（UART + DMA + 协议） | 未开始 |
| 2 | OpenCV 基础与颜色识别 | 未开始 |
| 3 | 云台控制与 PID | 未开始 |
| 4 | 优化与鲁棒性 | 未开始 |
| 5 | 装甲板识别进阶（选做） | 未开始 |
| 6 | 作品化与复盘 | 未开始 |

完整的学习计划、推进规则与进度记录见 [PROGRESS.md](PROGRESS.md)；各阶段任务书见 `docs/` 目录。

## 目录结构

```
├── pc/          # PC 端 Python 脚本（视觉识别、串口通信）
├── firmware/    # STM32 工程（CubeMX 配置、固件代码）
├── evidence/    # 各阶段验收证据（截图、视频、日志，按 stageX 归档）
├── docs/        # 项目文档（通信协议、接线图、任务书等）
├── check_env.py        # Python 环境自检脚本
├── 01_hello_opencv.py  # OpenCV 入门示例
├── PROGRESS.md         # 学习计划与进度（主文档）
└── requirements.txt    # Python 依赖清单
```

## 环境搭建

1. 安装 Python 3.12，在项目根目录创建虚拟环境：

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. 环境自检（不依赖外部图片，验证 OpenCV 读写、边缘检测、常用模块可用性）：

   ```powershell
   python check_env.py
   ```

## 技术栈

| 端 | 技术 |
|---|---|
| PC | Python 3.12 / OpenCV 5.0（contrib）/ NumPy / PySerial |
| 嵌入式 | STM32（CubeMX + HAL）/ UART + DMA 空闲中断 / PWM |

## 说明

这是一个进行中的学习项目：按阶段推进，每完成一个阶段会提交对应的代码、文档与验收证据，提交历史即成长记录。
