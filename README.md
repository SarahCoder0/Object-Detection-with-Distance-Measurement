# Object-Detection-with-Distance-Measurement
A real-time object detection and proximity warning system that combines Python (for computer vision and display) and Arduino (for ultrasonic distance sensing). The system detects when an object is closer than a predefined threshold and displays a visual warning box on the video feed.

---

## Table of Contents
- [Features](#Features)
- [Hardware Requirements](#Hardware Requirements)
- [Circuit Diagram (Arduino Connections)](#Circuit Diagram (Arduino Connections))
- [Code Overview](#Code Overview)
- [Customization](#Customization)
- [License](#License)

---

##  Features
· Real-time Distance Measurement: Uses an HC-SR04 ultrasonic sensor with Arduino to accurately measure distance to an object.
· Visual Feedback: Displays a live video stream with an overlaid bounding box and text alert when an object is too close.
· Configurable Threshold: Easily adjust the minimum safe distance (threshold_distance) in the Python code.
· Serial Communication: Seamless data exchange between Arduino and Python via the pyserial library.
· Simple & Effective: Provides a clear and intuitive visual warning system.

---

## 
🛠️ Hardware Requirements

1. Arduino Board (Uno, Nano, etc.)
2. HC-SR04 Ultrasonic Distance Sensor
3. LED (Optional, for on-board visual indicator)
4. Jumper Wires
5. Webcam (Integrated or USB)
6. Breadboard (Optional, for easier wiring)

---

## Circuit Diagram (Arduino Connections)

Connect your components as follows:

HC-SR04 Sensor Arduino Pin
VCC 5V
Trig Digital 9
Echo Digital 10
GND GND

LED (Optional) Arduino Pin
Anode (Long leg) Digital 13
Cathode (Short leg) GND (via resistor)

---

## Code Overview

Arduino Code:
The Arduino code continuously reads data from the HC-SR04 sensor, turns on an LED if an object is too close, and sends the distance value over the serial port.

Python Code:
The Python code captures video from the webcam, reads the distance data from the serial port, and uses OpenCV to draw an overlay on the video frame if the distance is below the threshold.

---

## Customization

· Change Threshold: Modify the threshold_distance variable in the Python script.
· Adjust Overlay: Change the size, position, color, and text of the bounding box by editing the cv2.rectangle and cv2.putText functions.
· Sensor Settings: Adjust the THRESHOLD_DISTANCE in the Arduino code for the LED indicator.

---

## 📜 License
This project is for **showcase purposes only**. Reproduction, modification, or commercial use without explicit permission is prohibited.
