# src/metrics.py
"""
Módulo para cálculo e exibição de métricas de avaliação em Machine Learning.
"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

def calcular_metricas(y_true, y_pred):
    """
    Calcula métricas principais: Acurácia, Precisão, Recall e F1.
    """
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "f1_score": f1_score(y_true, y_pred)
    }
    return metrics


def exibir_metricas(metrics: dict):
    """
    Exibe as métricas formatadas no console.
    """
    print("📊 Resultados das Métricas:")
    for k, v in metrics.items():
        print(f"{k.capitalize()}: {v:.4f}")


def plotar_matriz_confusao(y_true, y_pred, labels=None):
    """
    Plota a matriz de confusão usando seaborn.
    """
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=labels, yticklabels=labels)
    plt.xlabel("Previsto")
    plt.ylabel("Real")
    plt.title("Matriz de Confusão")
    plt.show()


def gerar_relatorio(y_true, y_pred, target_names=None):
    """
    Gera um relatório detalhado com precisão, recall e F1 por classe.
    """
    print("📑 Relatório de Classificação:")
    print(classification_report(y_true, y_pred, target_names=target_names))
