# Hand Gesture LED Control using Python and Arduino

An interactive AI-powered robotics project that translates real-time human hand gestures into hardware control signals. This system uses a computer vision pipeline developed in Python to detect hand landmarks and communicates state changes via serial communication to an Arduino microcontroller, dynamically toggling an array of LEDs.



## 📸 Project Showcase

Below are the visual highlights, software interfaces, and hardware setups representing the system in operation.

| Demo Photo 1 | Demo Photo 2 |
| :---: | :---: |
| ![Demo Photo 1](1.png) | ![Demo Photo 2](2.png) |

| Demo Photo 3 | Demo Photo 4 |
| :---: | :---: |
| ![Demo Photo 3](3.png) | ![Demo Photo 4](4.png) |

| Demo Photo 5 | Demo Photo 6 |
| :---: | :---: |
| ![Demo Photo 5](5.png) | ![Demo Photo 6](6.png) |

| Demo Photo 7 | Demo Photo 8 | Demo Photo 9 |
| :---: | :---: | :---: |
| ![Demo Photo 7](7.png) | ![Demo Photo 8](8.png) | ![Demo Photo 9](9.png) |

---

## 🎥 Demonstration

Watch the complete hardware responsiveness and gesture tracking precision video:

[▶ Watch the Demo Video](demo_video.mov)

---

## 🚀 Features

- **Real-time Landmark Tracking:** High-fidelity hand tracking with sub-millisecond coordination processing using MediaPipe.
- **Robust Feature Mapping:** Robust finger counting logic that translates physical states directly into numerical indices.
- **Low-Latency Serial Interface:** Optimized Python-to-Arduino serial messaging protocol (115200 Baud) preventing packet loss.
- **Dynamic Hardware Feedback:** Instantaneous multi-LED control mapped to discrete finger tracking permutations.
- **Visual Telemetry Overlay:** OpenCV-driven HUD showcasing tracking FPS, detection confidence values, and sending-state metrics.

---

## 🛠️ How It Works

The system operates over a modular three-tier closed-loop pipeline:

[ Web Camera ] ---> [ Python OpenCV/MediaPipe ] ---> [ Serial Command ] ---> [ Arduino Uno ] ---> [ LED Array ]


1. **Computer Vision & Processing Tier:** The local webcam captures video frames. OpenCV processes the image matrix and forwards it to the MediaPipe hands model. The model extracts a multi-dimensional array of 21 unique 3D hand landmark coordinates.
2. **Decision & Translation Tier:** Python script calculates logical state differences between specific finger joints (specifically comparing tip coordinates like `TIP_ID` against pip joints `PIP_ID`). It evaluates the count of extended fingers and writes a single-byte command sequence to the serial bus.
3. **Execution Tier:** The Arduino microcontroller polls its hardware serial buffer, reads incoming byte commands, routes them through a switch-case statement, and applies `HIGH` or `LOW` digital signals to the corresponding GPIO pins wiring the LED matrix.

---

## 🔌 Hardware & Software Requirements

### Hardware Components
- Arduino Uno R3 (or compatible microcontroller)
- 5x LEDs (Different colors preferred for state visibility)
- 5x 220Ω Resistors (Current limiting)
- 1x Breadboard
- Solid/Stranded jumper wires
- USB Type-A to Type-B interface cable
- Standard Web Camera (Built-in or External USB module)

### Software & Dependencies
- Python 3.10+
- Arduino IDE (v2.0+)
- OpenCV Python (`pip install opencv-python`)
- MediaPipe (`pip install mediapipe`)
- PySerial (`pip install pyserial`)

---

## 📐 Arduino Wiring Diagram

Ensure your hardware connections mirror the structural definitions detailed below to guarantee error-free matching with the firmware logic:

  Arduino Uno               Resistor       LED
+-------------------+       +-------+     +-----+
|       Digital D2  |------[ 220 Ω ]---->|  A  |----+
|       Digital D3  |------[ 220 Ω ]---->|  B  |----+
|       Digital D4  |------[ 220 Ω ]---->|  C  |----+
|       Digital D5  |------[ 220 Ω ]---->|  D  |----+
|       Digital D6  |------[ 220 Ω ]---->|  E  |----+
|                   |                             |
|              GND  |<----------------------------+ (Common Cathode)
+-------------------+


| Arduino Digital Pin | Component | Target Specification |
| :---: | :---: | :---: |
| **D2** | LED 1 Anode | Red LED / Indicator 1 |
| **D3** | LED 2 Anode | Yellow LED / Indicator 2 |
| **D4** | LED 3 Anode | Green LED / Indicator 3 |
| **D5** | LED 4 Anode | Blue LED / Indicator 4 |
| **D6** | LED 5 Anode | White LED / Indicator 5 |
| **GND** | Rail Common | Common Ground Return |

---

## 📊 Finger Gesture Mapping

The system firmware maps specific coordinate logical states to exact programmatic outputs inside the execution loop:

| Extended Fingers Count | Serial Output (Byte) | Arduino Execution Behavior |
| :---: | :---: | :--- |
| **0** | `'0'` | Turn OFF all LEDs |
| **1** | `'1'` | Pin D2 `HIGH` \| Pins D3-D6 `LOW` |
| **2** | `'2'` | Pins D2, D3 `HIGH` \| Pins D4-D6 `LOW` |
| **3** | `'3'` | Pins D2, D3, D4 `HIGH` \| Pins D5-D6 `LOW` |
| **4** | `'4'` | Pins D2, D3, D4, D5 `HIGH` \| Pin D6 `LOW` |
| **5** | `'5'` | Turn ON all LEDs (Pins D2 to D6 `HIGH`) |

---

## ⚡ Installation & Execution Steps


### 1. Microcontroller Flash
1. Connect your Arduino Uno to your PC/Mac using the USB data cable.
2. Launch **Arduino IDE**, navigate to `File > Open`, and load your `.ino` controller file.
3. Choose the appropriate COM Port (`Tools > Port`) and board type (`Tools > Board > Arduino Uno`).
4. Click **Upload** (Right-pointing arrow icon) to flash the firmware.

### 2. Software Environment Deployment
Open a terminal instance or command window within your repository directory and execute the setup instructions:


# Clone the repository
git clone [https://github.com/birsyangbo/hand-gesture-led-control.git](https://github.com/birsyangbo/hand-gesture-led-control.git)
cd hand-gesture-led-control

# Install core runtime dependencies
pip install opencv-python mediapipe pyserial
3. Running the Application
Ensure that your Arduino remains connected to the USB communication port, then start the computer vision application loop:

Bash
python main.py
Note: If your system utilizes multiple video capture assets, modify the camera device index configuration inside the instantiation block: cv2.VideoCapture(0).
