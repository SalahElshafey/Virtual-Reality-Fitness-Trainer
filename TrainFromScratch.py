from ultralytics import YOLO
import torch
import os

def main():
    # Select GPU if available
    device = 0 if torch.cuda.is_available() else "cpu"
    print(f"✅ Using device: {'CUDA' if device == 0 else 'CPU'}")

    # Load best YOLOv8 pose model for training
    model = YOLO("yolov8x-pose.pt")

    # Path to config.yaml (with raw string to handle backslashes)
    config_path = r"F:\AASTMT (Bachelor CE)\Semester 10\Senior Project II\Graduation_Project\VR_Fitness_Trainer_Model\config.yaml"

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"❌ Dataset config not found at: {config_path}")

    # Train with best available settings for accuracy
    model.train(
        data=config_path,
        epochs=570,
        imgsz=640,
        batch=16,                  # 4060 can handle this
        device=device,
        name="pose_estimation_yolov8x",
        patience=30,
        save_period=50,
        degrees=15,
        scale=0.5,
        shear=3,
        flipud=0.5,
        translate=0.1,
        cos_lr=True,              # Better convergence curve
        auto_augment="randaugment",  # Boost diversity
        warmup_epochs=5.0
    )

if __name__ == "__main__":
    main()