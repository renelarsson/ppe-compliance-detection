import os
import shutil
import argparse

# Define paths to the dataset directories
data_dir = '/workspaces/ppe-compliance-detection/data'
images_dir = os.path.join(data_dir, 'images')
labels_dir = os.path.join(data_dir, 'labels')
default_output_dir = os.path.join(data_dir, 'image_label_mapping')

def find_image_path(base_dir: str, stem: str):
    exts = [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]
    for ext in exts:
        path = os.path.join(base_dir, f"{stem}{ext}")
        if os.path.exists(path):
            return path
    return None


def preprocess_dataset(output_dir: str):
    """
    Organize images into subdirectories based on their labels, preserving
    train/val/test splits:
      output_dir/
        train/<class_id>/image*.jpg
        val/<class_id>/image*.jpg
        test/<class_id>/image*.jpg
    """
    os.makedirs(output_dir, exist_ok=True)

    totals = {"train": 0, "val": 0, "test": 0}
    missing_images = 0

    for subset in ["train", "val", "test"]:
        subset_images_dir = os.path.join(images_dir, subset)
        subset_labels_dir = os.path.join(labels_dir, subset)

        if not os.path.isdir(subset_images_dir) or not os.path.isdir(subset_labels_dir):
            print(f"Skipping {subset}: missing images or labels directory")
            continue

        label_files = [f for f in os.listdir(subset_labels_dir) if f.endswith('.txt')]
        for label_file in label_files:
            stem = label_file[:-4]
            label_path = os.path.join(subset_labels_dir, label_file)

            # Parse class ids from YOLO label file (first token per line)
            class_ids = set()
            with open(label_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split()
                    if not parts:
                        continue
                    class_ids.add(parts[0])

            img_path = find_image_path(subset_images_dir, stem)
            if not img_path:
                missing_images += 1
                continue

            for cid in class_ids:
                class_dir = os.path.join(output_dir, subset, str(cid))
                os.makedirs(class_dir, exist_ok=True)
                shutil.copy(img_path, os.path.join(class_dir, os.path.basename(img_path)))
                totals[subset] += 1

    print("Copy summary (copies, not unique images):")
    for k, v in totals.items():
        print(f"  {k}: {v}")
    if missing_images:
        print(f"Missing images for {missing_images} label files (different extensions?)")


def main():
    parser = argparse.ArgumentParser(description="Map images into class folders using YOLO label files, preserving splits.")
    parser.add_argument("--output-dir", default=default_output_dir, help="Output directory for mapped dataset")
    args = parser.parse_args()

    preprocess_dataset(args.output_dir)
    print(f"Dataset preprocessing complete. Processed images are saved in: {args.output_dir}")


if __name__ == "__main__":
    main()