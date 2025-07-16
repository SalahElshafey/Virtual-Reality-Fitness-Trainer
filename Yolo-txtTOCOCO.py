import os
import json
from glob import glob
from tqdm import tqdm
import cv2

# === SETTINGS ===
dataset_dir = r""
splits = ["train", "val", "test"]
 # Make sure these folders exist under dataset_dir

# === KEYPOINT DEFINITIONS ===
keypoints = [
    "Head", "Neck", "Shoulders", "Elbows", "Hands",
    "Core", "Glutes", "Knee", "Foot"
]
num_keypoints = len(keypoints)
skeleton = []  # Add edges between keypoints here if needed

categories = [{
    "supercategory": "person",
    "id": 1,
    "name": "person",
    "keypoints": keypoints,
    "skeleton": skeleton
}]

# === BBOX CONVERSION ===
def yolo_to_coco_bbox(x, y, w, h, img_w, img_h):
    x_min = (x - w / 2) * img_w
    y_min = (y - h / 2) * img_h
    width = w * img_w
    height = h * img_h
    return [x_min, y_min, width, height]

# === MAIN LOOP FOR EACH SPLIT ===
for split in splits:
    print(f"\n🔁 Processing {split} set...")

    img_dir = os.path.join(dataset_dir, split, "images")
    label_dir = os.path.join(dataset_dir, split, "labels")
    output_json = os.path.join(dataset_dir, f"{split}_coco_keypoints.json")

    coco_dict = {
        "info": {"description": f"Converted from YOLO format: {split} set"},
        "licenses": [],
        "images": [],
        "annotations": [],
        "categories": categories
    }

    annotation_id = 1
    image_id = 1
    total_anns = 0

    image_paths = glob(os.path.join(img_dir, "*.jpg")) + glob(os.path.join(img_dir, "*.png"))

    for img_path in tqdm(image_paths, desc=f"Processing {split} set"):
        img = cv2.imread(img_path)
        if img is None:
            continue
        h, w = img.shape[:2]
        file_name = os.path.basename(img_path)

        coco_dict["images"].append({
            "id": image_id,
            "width": w,
            "height": h,
            "file_name": file_name
        })

        label_path = os.path.join(label_dir, os.path.splitext(file_name)[0] + ".txt")
        if not os.path.exists(label_path):
            image_id += 1
            continue

        with open(label_path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            parts = list(map(float, line.strip().split()))
            if len(parts) < 5 + num_keypoints * 3:
                continue  # Skip incomplete annotations

            class_id = int(parts[0])
            bbox_yolo = parts[1:5]
            kpts_raw = parts[5:]

            keypoints_coco = []
            num_visible = 0
            for i in range(num_keypoints):
                x = kpts_raw[i * 3] * w
                y = kpts_raw[i * 3 + 1] * h
                v = int(kpts_raw[i * 3 + 2])
                keypoints_coco.extend([x, y, v])
                if v > 0:
                    num_visible += 1

            bbox_coco = yolo_to_coco_bbox(*bbox_yolo, w, h)

            coco_dict["annotations"].append({
                "id": annotation_id,
                "image_id": image_id,
                "category_id": 1,
                "bbox": bbox_coco,
                "area": bbox_coco[2] * bbox_coco[3],
                "iscrowd": 0,
                "num_keypoints": num_visible,
                "keypoints": keypoints_coco
            })
            annotation_id += 1
            total_anns += 1

        image_id += 1

    # === SAVE JSON ===
    with open(output_json, 'w') as f:
        json.dump(coco_dict, f, indent=2)

    print(f"✅ Saved {split} annotations to: {output_json}")
    print(f"🖼️  Total images: {len(coco_dict['images'])}")
    print(f"🔖  Total annotations: {total_anns}")
