# Virtual Mouse using OpenCV, MediaPipe, and PyAutoGUI

## Overview

This project implements a virtual mouse using OpenCV for image processing, MediaPipe for hand tracking, and PyAutoGUI for controlling mouse actions. By detecting hand landmarks through the webcam feed, this virtual mouse allows you to move the cursor and perform click actions using hand gestures.

## Features

- Real-time hand tracking and landmark detection using MediaPipe.
- Cursor movement based on the index finger's position.
- Click actions triggered by the distance between the thumb and the index finger.

## Requirements

- Python 3.6 or higher
- OpenCV
- MediaPipe
- PyAutoGUI

## Installation

1. Clone this repository:

   in bash
   git clone https://github.com/your-username/virtual-mouse.git
   cd virtual-mouse

2. Install the required packages:

   in bash
   pip install opencv-python mediapipe pyautogui

## Usage

1. Ensure your webcam is connected and properly set up.

2. Run the virtual mouse script:

   in bash
   python virtual_mouse.py

3. A window will open displaying the webcam feed with hand landmarks tracked in real-time. Use your index finger to move the cursor. Move the thumb close to the index finger to click.

## Troubleshooting

- If the webcam feed is not displaying or the landmarks are not detected properly, ensure your webcam is working and is accessible by OpenCV.
- Adjust the thresholds for the click action distance if you experience unintentional clicks.

## Contributing

Feel free to fork this repository and contribute via pull requests. Any enhancements or bug fixes are welcome.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
