🚀 Distraction-Free Study Lamp (MicroPython + Micro:bit + Radio Communication)

A hardware-based study-focus system built using two Micro:bits.
The system detects when a student lifts or touches their phone and automatically pauses the study timer, helping maintain deep focus without apps or external notifications.

This project integrates embedded systems, real-time sensing, wireless communication, and 3D-printed design into a polished, functional device.

📸 Project Demo

Here is the working prototype of the Distraction-Free Study Lamp:

📌 Project Overview

The system uses two Micro:bits working together:

🎯 Microbit A — Study Timer

25-minute Pomodoro countdown

Start → Button A

Reset → Button B

Displays remaining minutes on a 5×5 LED display

Pauses automatically when distraction signal is received

Shows ❌ and plays an alert until the phone is placed back

📱 Microbit B — Phone Detector

Uses the light sensor to detect whether the phone is covering it

Sends “OK” when phone is placed

Sends “ALARM” when the phone is lifted

Plays a buzzer alert and shows ❌

Responds instantly and continuously monitors ambient light

📡 System Architecture
          (Light Sensor)
     ┌─────────────────────────┐
     │   Microbit B (Sensor)   │
     │  Detects Phone Position │
     │ light < threshold → OK  │
     │ light ≥ threshold → ALARM │
     └─────────────┬──────────┘
                   │ Radio Group 7
                   ▼
     ┌─────────────────────────┐
     │   Microbit A (Timer)    │
     │   Displays countdown    │
     │ Freezes on ALARM signal │
     │ Resumes on OK signal    │
     └─────────────────────────┘

⚙️ Key Features

✔ Real-time distraction detection
✔ Event-driven programming
✔ Light-sensor-based phone detection
✔ Wireless radio messaging (Radio Group 7)
✔ Pomodoro-style study timer
✔ Loud alert + visual ❌ symbol
✔ 3D-printed lamp enclosure for accurate sensing
✔ Hardware–software integration

🛠️ Hardware Requirements

2×  Micro:bit (v1 or v2)

Micro USB cables

3D-printed lamp shade

3D-printed Microbit B sensor enclosure

💻 Software Requirements

MicroPython

Thonny or Mu Editor

MakeCode (for initial prototyping)

GitHub (for version control)

📁 Project Structure
Distraction-Free-Study-Lamp/
│
├── microbit_a.py        # Timer logic (Microbit A)
├── microbit_b.py        # Phone detection logic (Microbit B)
├── README.md            # Project documentation
├── LICENSE              # MIT License
└── .gitignore

▶️ How It Works
Microbit A (Timer Device)

Flash microbit_a.py

Press Button A → Start timer (25 mins)

Press Button B → Reset timer

If ALARM received → freeze timer + ❌ + alert sound

If OK received → resume timer

Microbit B (Phone Detector)

Flash microbit_b.py

Phone covering sensor → OK

Phone removed → ALARM

Sends radio messages continuously

Alerts user through LED + buzzer

🎨 3D-Printed Design Components

Custom lamp cover for consistent lighting

Custom sensor box for Microbit B

Designed to block external light interference

Clean, minimal aesthetic for study desk

Looks like a polished prototype, not loose wires

🧪 Engineering Process & Iteration

Calibrated light thresholds under different lighting

Debugged timer freeze & radio delay issues

Tested multiple LED timer layouts

Fixed buzzer looping behavior

Improved communication reliability

Purpose-driven iterations using real-world testing
