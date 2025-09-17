# scripts/split_dataset.py

"""
Script para dividir o dataset em treino e teste.
Os arquivos gerados serão salvos em data/processed/train.csv e data/processed/test.csv.
"""

import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split


def split_dataset(input_path: str, output_dir: str, test_size: float = 0.2, random_state: int = 42):
    """
    Divide o dataset em treino e teste e salva os arquivos.
    
    Args:
        input_path (str): Caminho do dataset de entrada (CSV).
        output_dir (str): Diretório onde os arquivos processados serão salvos.
        test_size (float): Proporção do dataset para teste. Default = 0.2.
        random_state (int): Semente para reprodutibilidade. Default = 42.
    """
    # Verifica se o arquivo existe
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {input_path}")
    
    # Cria diretório de saída, se não existir
    os.makedirs(output_dir, exist_ok=True)
    
    # Lê o dataset
    df = pd.read_csv(input_path)
    print(f"Dataset carregado com {df.shape[0]} linhas e {df.shape[1]} colunas.")
    
    # Divide em treino e teste
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)
    
    # Salva arquivos
    train_path = os.path.join(output_dir, "train.csv")
    test_path = os.path.join(output_dir, "test.csv")
    
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)
    
    print(f"Arquivos gerados:")
    print(f" - Treino: {train_path} ({train_df.shape[0]} linhas)")
    print(f" - Teste: {test_path} ({test_df.shape[0]} linhas)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dividir dataset em treino e teste.")
    parser.add_argument("--input", type=str, required=True, help="Caminho do dataset de entrada (CSV).")
    parser.add_argument("--output", type=str, default="data/processed", help="Diretório de saída.")
    parser.add_argument("--test_size", type=float, default=0.2, help="Proporção para teste (default: 0.2).")
    parser.add_argument("--random_state", type=int, default=42, help="Semente para reprodutibilidade.")
    
    args = parser.parse_args()
    
    split_dataset(args.input, args.output, args.test_size, args.random_state)
