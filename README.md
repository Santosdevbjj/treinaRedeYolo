## Criação de Uma Base de Dados e Treinamento da Rede YOLO.


Bootcamp 

---


# Projeto de Criação de Base de Dados e Treinamento da Rede YOLO

Este projeto visa desenvolver um pipeline completo para detecção de objetos utilizando a rede YOLO. Inclui as etapas de coleta e rotulagem de imagens, formatação do dataset, treinamento com transfer learning e avaliação do modelo.

## Estrutura do Repositório

* `data/`: Contém as imagens e o dataset final.
    * `raw_images/`: Imagens originais a serem rotuladas.
    * `labeled_images/`: Imagens após processamento inicial.
    * `yolo_dataset/`: Dataset formatado para o YOLO (train/val/test).
* `labels/`: Arquivos de anotação gerados pelo LabelMe.
* `models/`: Modelos treinados (pesos).
* `scripts/`: Scripts auxiliares (conversão de formato, etc.).
* `configs/`: Arquivos de configuração do YOLO.
* `notebooks/`: Notebooks para experimentação (ex: Google Colab).
* `README.md`: Descrição detalhada do projeto.
* `requirements.txt`: Dependências do Python.

## Tecnologias Utilizadas

* **LabelMe:** Ferramenta para rotulagem de imagens.
* **YOLO (You Only Look Once):** Rede neural para detecção de objetos.
* **Google Colab:** Ambiente para treinamento com GPUs.
* **Python:** Linguagem de programação principal.
* **Darknet:** Framework para YOLO (ou alternativas como PyTorch/TensorFlow).

## Próximos Passos

1.  Coleta de Imagens.
2.  Rotulagem com LabelMe.
3.  Conversão de Anotações.
4.  Configuração do Treinamento no Colab.
5.  Treinamento e Avaliação.


