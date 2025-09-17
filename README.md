## Criação de Uma Base de Dados e Treinamento da Rede YOLO.

![bairesDev](https://github.com/user-attachments/assets/3613b0ea-8e0e-45c6-9e16-4165b2efc812)



**Bootcamp BairesDev - Machine Learning Training**


---

# Treina Rede YOLO

![GitHub repo size](https://img.shields.io/github/repo-size/Santosdevbjj/treinaRedeYolo)
![GitHub contributors](https://img.shields.io/github/contributors/Santosdevbjj/treinaRedeYolo)
![GitHub last commit](https://img.shields.io/github/last-commit/Santosdevbjj/treinaRedeYolo)
![Python Version](https://img.shields.io/badge/python-3.10-blue)

Repositório para **criação de base de dados e treinamento da rede YOLO**, incluindo:  
- Divisão automática do dataset em **treino e validação**  
- Cálculo e visualização de métricas de avaliação  
- Notebook pronto para análises e testes  

---

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

| Tecnologia | Uso no projeto |
|------------|----------------|
| **Python 3.10+** | Linguagem principal para scripts, notebook e módulos |
| **Jupyter / Colab** | Execução do notebook `treino_yolo.ipynb` |
| **OpenCV** | Leitura e manipulação de imagens para YOLO |
| **NumPy** | Manipulação de arrays e operações matemáticas |
| **Matplotlib / Seaborn** | Visualização de métricas e matriz de confusão |
| **Scikit-learn** | Cálculo de métricas de classificação (acurácia, precisão, recall, F1) |
| **LabelMe** | Rotulagem de imagens para gerar os arquivos `.txt` do YOLO |
| **YOLO (Darknet)** | Treinamento e detecção de objetos em imagens |

---

## 📂 Estrutura do repositório


<img width="974" height="1493" alt="Screenshot_20250917-004537" src="https://github.com/user-attachments/assets/bd1f58b0-a8b8-4bdf-88cf-284d83f15c04" />



---


## 📖 Descrição dos arquivos e pastas

### `data/`
- **raw/** → Arquivos originais do dataset:
  - `images/` → Imagens brutas
  - `labels/` → Labels correspondentes no formato YOLO (`.txt`)
- **processed/** → Dados processados após divisão em treino e validação:
  - `images/train/` e `images/val/`
  - `labels/train/` e `labels/val/`

### `notebooks/`
- **treino_yolo.ipynb** → Notebook principal:
  - Chama o script `split_dataset.py` para organizar dataset  
  - Calcula métricas de classificação usando `metrics.py`  
  - Gera matriz de confusão e relatório detalhado

### `scripts/`
- **split_dataset.py** → Script para dividir dataset em treino/validação, garantindo consistência entre imagens e labels.  

### `src/`
- **metrics.py** → Funções de métricas:
  - `calcular_metricas()`
  - `exibir_metricas()`
  - `plotar_matriz_confusao()`
  - `gerar_relatorio()`

### `requirements.txt`
- Bibliotecas necessárias para rodar o projeto:
```txt
numpy
matplotlib
seaborn
scikit-learn
opencv-python



---

.gitignore

Ignora arquivos temporários, logs, checkpoints de Jupyter, datasets grandes e ambientes virtuais.



---


---

⚙️ Como executar o projeto

1. Clonar o repositório

git clone https://github.com/Santosdevbjj/treinaRedeYolo.git
cd treinaRedeYolo


---


2. Instalar dependências

pip install -r requirements.txt

---


3. Preparar dataset

Coloque imagens em data/raw/images/

Coloque labels YOLO em data/raw/labels/


4. Dividir dataset em treino/validação

python scripts/split_dataset.py \
    --images_dir data/raw/images \
    --labels_dir data/raw/labels \
    --output_dir data/processed \
    --split_ratio 0.8


---

5. Abrir notebook


No Jupyter ou Colab, abra notebooks/treino_yolo.ipynb e execute as células.

O notebook já integra a divisão de dataset e o cálculo de métricas.



---



📊 Métricas incluídas

Acurácia

Precisão

Recall

F1-Score

Matriz de Confusão

Relatório detalhado por classe



---

📌 Notas

O projeto é modular e reutilizável em outros datasets YOLO.

Não subir arquivos de dataset grandes no GitHub.

Compatível com Python 3.10+




---


🛠️ Badges usados

GitHub repo size: 

GitHub contributors: 

Last commit: 

Python version: 



---










