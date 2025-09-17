"""
Script para dividir o dataset em treino e validação
Mantém a consistência entre imagens e labels no formato YOLO.
"""

import os
import random
import shutil
from pathlib import Path

def split_dataset(
    images_dir: str,
    labels_dir: str,
    output_dir: str,
    split_ratio: float = 0.8,
    seed: int = 42
):
    """
    Divide o dataset em treino e validação.

    Args:
        images_dir (str): Caminho para as imagens originais.
        labels_dir (str): Caminho para os labels YOLO correspondentes.
        output_dir (str): Diretório base para salvar train/val.
        split_ratio (float): Proporção de treino (default 0.8).
        seed (int): Semente aleatória para reprodutibilidade.
    """

    random.seed(seed)

    # Converte para Path
    images_dir = Path(images_dir)
    labels_dir = Path(labels_dir)
    output_dir = Path(output_dir)

    # Cria pastas
    for split in ["train", "val"]:
        (output_dir / "images" / split).mkdir(parents=True, exist_ok=True)
        (output_dir / "labels" / split).mkdir(parents=True, exist_ok=True)

    # Lista de arquivos de imagem
    image_files = [f for f in images_dir.glob("*.jpg")] + [f for f in images_dir.glob("*.png")]
    random.shuffle(image_files)

    # Split
    split_index = int(len(image_files) * split_ratio)
    train_files = image_files[:split_index]
    val_files = image_files[split_index:]

    def move_files(file_list, split):
        for img_file in file_list:
            label_file = labels_dir / (img_file.stem + ".txt")
            if not label_file.exists():
                print(f"⚠️ Label não encontrado para {img_file.name}, pulando...")
                continue

            # Copia imagem e label
            shutil.copy(img_file, output_dir / "images" / split / img_file.name)
            shutil.copy(label_file, output_dir / "labels" / split / label_file.name)

    move_files(train_files, "train")
    move_files(val_files, "val")

    print(f"✅ Dataset dividido com sucesso!")
    print(f"Treino: {len(train_files)} imagens")
    print(f"Validação: {len(val_files)} imagens")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Divide dataset em treino e validação.")
    parser.add_argument("--images_dir", type=str, required=True, help="Diretório com imagens")
    parser.add_argument("--labels_dir", type=str, required=True, help="Diretório com labels YOLO")
    parser.add_argument("--output_dir", type=str, required=True, help="Diretório de saída")
    parser.add_argument("--split_ratio", type=float, default=0.8, help="Proporção de treino")
    parser.add_argument("--seed", type=int, default=42, help="Semente aleatória")

    args = parser.parse_args()

    split_dataset(
        args.images_dir,
        args.labels_dir,
        args.output_dir,
        args.split_ratio,
        args.seed
    )
