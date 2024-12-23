from ultralytics import YOLO
import cv2

# Load the YOLO model
model = YOLO("D:\\AASTMT (Bachelor CE)\\Semester 9\Senior Project I\\Graduation_Project\VR_Fitness_Trainer_Model\\Virtual-Reality-Fitness-Trainer\\runs\\pose\\pose_estimation3\\weights\\best.pt")

# Open the camera
video_source = 0  # 0 for the laptop camera
cap = cv2.VideoCapture(video_source)

# Check if the camera is accessible
if not cap.isOpened():
    print("Error: Unable to open video source.")
    exit()

# Set resolution (optional, adjust as needed)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Press 'q' to quit the stream.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to fetch frame.")
        break

    # Perform pose estimation
    results = model.predict(source=frame, save=False, show=False, conf=0.3)


    # Annotate the frame
    annotated_frame = results[0].plot()

    # Display the frame
    cv2.imshow("YOLO Pose Estimation - Live Stream", annotated_frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
