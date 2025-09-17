# scripts/split_dataset.py
"""
Script para dividir o dataset em treino e validação (imagens + labels).
"""

import os
import random
import shutil
from pathlib import Path

def split_dataset(images_dir, labels_dir, output_dir, split_ratio=0.8, seed=42):
    random.seed(seed)
    images_dir = Path(images_dir)
    labels_dir = Path(labels_dir)
    output_dir = Path(output_dir)

    for split in ["train", "val"]:
        (output_dir / "images" / split).mkdir(parents=True, exist_ok=True)
        (output_dir / "labels" / split).mkdir(parents=True, exist_ok=True)

    image_files = [f for f in images_dir.glob("*.jpg")] + [f for f in images_dir.glob("*.png")]
    random.shuffle(image_files)

    split_index = int(len(image_files) * split_ratio)
    train_files = image_files[:split_index]
    val_files = image_files[split_index:]

    def move_files(file_list, split):
        for img_file in file_list:
            label_file = labels_dir / (img_file.stem + ".txt")
            if not label_file.exists():
                print(f"⚠️ Label não encontrado para {img_file.name}, pulando...")
                continue
            shutil.copy(img_file, output_dir / "images" / split / img_file.name)
            shutil.copy(label_file, output_dir / "labels" / split / label_file.name)

    move_files(train_files, "train")
    move_files(val_files, "val")

    print(f"✅ Dataset dividido com sucesso! Treino: {len(train_files)}, Validação: {len(val_files)}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Divide dataset em treino/validação.")
    parser.add_argument("--images_dir", type=str, required=True)
    parser.add_argument("--labels_dir", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)
    parser.add_argument("--split_ratio", type=float, default=0.8)
    parser.add_argument("--seed", type=int, default=42)

    args = parser.parse_args()
    split_dataset(args.images_dir, args.labels_dir, args.output_dir, args.split_ratio, args.seed)
