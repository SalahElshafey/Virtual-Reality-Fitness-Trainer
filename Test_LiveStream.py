from ultralytics import YOLO
import cv2
import torch
import os
import paho.mqtt.client as mqtt
import ssl

# === Device Setup ===
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"🚀 Using device: {device.upper()}")

# === Load Trained Pose Classification Model ===
model_path = r"D:\AASTMT (Bachelor CE)\Semester 10\Senior Project II\Graduation_Project\VR_Fitness_Trainer_Model\runs\pose\pose_estimation_yolov8x2\weights\best.pt"

if not os.path.exists(model_path):
    raise FileNotFoundError(f"❌ Model not found at: {model_path}")

model = YOLO(model_path).to(device)

# === MQTT Setup ===
broker = "3c6ba859a3d04ec78f1577025c33b279.s1.eu.hivemq.cloud"
port = 8883
username = "youssef"
password = "Youssef2001"
topic = "vr"

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(username, password)
mqtt_client.tls_set(tls_version=ssl.PROTOCOL_TLS)
mqtt_client.connect(broker, port)
print("📡 Connected to HiveMQ broker.")

# === Webcam Setup ===
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Error: Unable to access webcam.")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
print("📹 Webcam started. Press 'q' to quit.")

last_sent_class = ""

# === Main Loop ===
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Frame capture failed.")
        break

    # Run inference
    results = model.predict(source=frame, conf=0.3, save=False, show=False, device=device)

    # Draw annotations
    annotated_frame = results[0].plot()

    # === Extract predicted class ===
    boxes = results[0].boxes
    if boxes and boxes.cls.numel() > 0:
        class_id = int(boxes.cls[0].item())
        class_name = results[0].names[class_id]

        if class_name != last_sent_class:
            result = mqtt_client.publish(topic, class_name)
            status = result[0]
            if status == 0:
                print(f"📤 Sent '{class_name}' to topic '{topic}'")
            else:
                print(f"❌ Failed to send message to topic '{topic}'")

            print(f"📤 Sent: {class_name}")
            last_sent_class = class_name
    else:
        print("👀 No class detected in frame.")

    # Show the frame
    cv2.imshow("🧍 YOLOv8 Pose Estimation", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🛑 Exiting.")
        break

# === Cleanup ===
cap.release()
cv2.destroyAllWindows()
mqtt_client.disconnect()
print("✅ MQTT Disconnected. Program ended.")
