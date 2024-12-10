from ultralytics import YOLO

model=YOLO('yolov8m-pose.pt')


model.train(

    data='D:/AASTMT (Bachelor CE)/Semester 9/Senior Project I/Graduation_Project/VR_Fitness_Trainer_Model/config.yaml',
    epochs=500,
    name='pose_estimation',
    save_period=100
)
