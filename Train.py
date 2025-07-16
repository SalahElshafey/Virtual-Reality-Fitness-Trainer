from ultralytics import YOLO
import torch
import os

def main():
    # Select GPU if available
    device = 0 if torch.cuda.is_available() else "cpu"
    print(f"✅ Using device: {'CUDA' if device == 0 else 'CPU'}")

    # Path to dataset config and model
    config_path = r"F:\AASTMT (Bachelor CE)\Semester 10\Senior Project II\Graduation_Project\VR_Fitness_Trainer_Model\config.yaml"
    model_path = r"F:\AASTMT (Bachelor CE)\Semester 10\Senior Project II\Graduation_Project\VR_Fitness_Trainer_Model\runs\pose\pose_estimation_yolov8x2\weights\last.pt"

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"❌ Dataset config not found at: {config_path}")

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"❌ Model checkpoint not found at: {model_path}")

    # Load the model from last.pt
    model = YOLO(model_path)

    # Resume training
    model.train(
        data=config_path,
        resume=True,                 # ✅ This is the key change
        device=device,
    )

if __name__ == "__main__":
    main()
