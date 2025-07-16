# 🏋️‍♂️ Virtual Reality Fitness Trainer

An AI-powered, real-time fitness coaching platform integrating **YOLOv8 pose estimation**, **virtual reality (Unity 3D)**, and **wearable biometric sensors** for immersive, safe, and personalized home workouts.

---

## Overview

The Smart Virtual Fitness Coaching Assistive System is a full-stack project developed as a final year thesis by students at the **Arab Academy for Science, Technology and Maritime Transport**. It addresses key gaps in at-home fitness training—such as poor posture, lack of motivation, and injury risk—by combining cutting-edge **deep learning**, **virtual environments**, and **biomedical sensors** into a unified, real-time feedback system.

---

## Features

- 🎯 **Real-time posture detection** using YOLOv8x-pose on 7 custom-labeled fitness exercises.
    
- 🧠 **AI-driven feedback system** giving live corrective instructions.
    
- 🕶️ **Immersive VR interface** built in Unity simulating a gym environment.
    
- ❤️ **Biomedical sensor integration** (ECG and SpO2) for heart rate and oxygen tracking.
    
- 📱 **Flutter mobile app** with live dashboards, history logs, and user-specific recommendations.
    
- ☁️ **Cloud synchronization** via Firebase for real-time health data and app syncing.
    
- 🔐 **User authentication** and secure data handling.
    

---

## System Architecture

**Main Components:**

1. **Machine Learning Module**
    
    - Model: `YOLOv8x-pose`
        
    - Input: Live webcam feed
        
    - Output: 2D keypoint detection + feedback
        
2. **Unity 3D Environment**
    
    - Avatar-based coaching system
        
    - Real-time visual feedback via MQTT
        
    - Level unlocking, performance HUD, animations
        
3. **Wearable Sensor Kit**
    
    - `AD8232`: ECG-based heart rate
        
    - `MAX30102`: Optical HR and SpO2
        
    - `ESP32`: Data collection + Wi-Fi/Bluetooth transmission
        
4. **Flutter Mobile App**
    
    - User profile setup
        
    - Real-time physiological tracking
        
    - Historical performance logging
        

---

## Performance Summary

|Component|Metric|Result|
|---|---|---|
|YOLOv8x-pose|mAP@50 on 7-class dataset|~0.85|
|Unity Simulation|Real-time pose sync latency|< 100ms @ 28 FPS|
|Sensors|Heart rate & SpO2 error margin|±3 BPM / ±2% SpO2|
|Mobile App|Data display/update latency|< 100ms (Firebase sync)|

---

## Setup & Installation

### Prerequisites

- Python 3.8+
    
- Unity 2021+
    
- Flutter SDK
    
- ESP32 development board
    
- Firebase account
    
## 💡 Future Work

- VR headset integration (Oculus, Meta Quest)
    
- Haptic feedback and audio coaching
    
- Voice control & NLP instructions
    
- Multiplayer training with avatars
    
- AI-generated personalized training plans
    

---

## Authors

Developed by:

- Salaheldin Khaled Elshafey
    
- Youssef Mohamed Thabet
    
- Mohamed Sherif Ibrahim
    
- Mahmoud Mohamed Ibrahim
    
- Amr Mohamed Kamoun
    
- Hana Ashraf Mahmoud
    

**Supervisor:** Prof. Dr. Sherine M. Youssef  
**Date:** July 2025  
**Department:** Computer Engineering, AASTMT

---

##  License

This project is for academic and non-commercial use. For licensing inquiries, please contact the authors.
