from ultralytics import YOLO
import cv2
import os

# Load the trained model
model = YOLO("D:\\AASTMT (Bachelor CE)\\Semester 10\\Senior Project II\\Graduation_Project\\VR_Fitness_Trainer_Model\\runs\\pose\\pose_estimation_gpu5\\weights\\best.pt")

# Path to the input video
video_path = "C:\\Users\hp\Downloads\\20 MIN CARDIO HIIT WORKOUT - ALL STANDING - Full Body, No Equipment, No Repeats (online-video-cutter.com).mp4"
cap = cv2.VideoCapture(video_path)

# Check if the video file can be opened
if not cap.isOpened():
    print("Error: Unable to open video file.")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Create the 'predict' folder if it doesn't exist
output_folder = "predict"
os.makedirs(output_folder, exist_ok=True)

# Define the output video path in the 'predict' folder
output_path = os.path.join(output_folder, "detected_video.avi")

# Define the VideoWriter object
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))

# Process the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Finished processing video.")
        break

    # Perform pose estimation
    results = model.predict(source=frame, save=False, show=False, conf=0.5)

    # Annotate the frame
    annotated_frame = results[0].plot()

    # Write the annotated frame to the output video
    out.write(annotated_frame)

# Release resources
cap.release()
out.release()

print(f"Annotated video saved to the 'predict' folder: {output_path}")
