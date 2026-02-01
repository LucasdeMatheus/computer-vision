# 🏃‍♂️ Contador de Polichinelos com MediaPipe

Este projeto utiliza **Visão Computacional com Python** para detectar e contar automaticamente **polichinelos** em um vídeo, usando o modelo **Pose Landmark** do **MediaPipe**.

A ideia central é analisar a distância entre **mãos** e **pés** ao longo do tempo e identificar o ciclo **abrir → fechar**, contabilizando cada repetição completa como **1 polichinelo**.

---

## 🎯 Objetivo

* Detectar pontos do corpo humano em tempo real
* Calcular a distância entre mãos e pés
* Identificar movimentos de abertura e fechamento
* Contar automaticamente o número de polichinelos executados

---

## 🧠 Tecnologias Utilizadas

* **Python 3**
* **OpenCV** – captura e exibição de vídeo
* **MediaPipe** – detecção de pose corporal
* **Math** – cálculo de distâncias euclidianas

---

## 🧍 Pose Landmark Model (MediaPipe)

O MediaPipe Pose fornece **33 landmarks corporais**, cada um com coordenadas normalizadas `(x, y, z)`.

Esses pontos representam articulações e extremidades do corpo, como:

* Mãos
* Pés
* Joelhos
* Ombros
* Quadris

Eles permitem entender o movimento corporal com alta precisão.

### 📌 Modelo de Landmarks

<img width="572" height="389" alt="Pose Landmarks" src="https://github.com/user-attachments/assets/0d2eff56-0f9a-4d01-be6f-ca4779ba5848" />

📖 Documentação oficial do MediaPipe Pose:
👉 [https://chuoling.github.io/mediapipe/solutions/pose.html](https://chuoling.github.io/mediapipe/solutions/pose.html)

---

## 🧮 Lógica do Contador

O contador funciona com base em **estados de movimento**:

### 1️⃣ Abertura

* Mãos afastadas
* Pés afastados

### 2️⃣ Fechamento

* Mãos próximas
* Pés próximos

🔁 Um **polichinelo completo** ocorre quando o corpo passa de **aberto → fechado**.

Para evitar contagens duplicadas, o sistema usa uma variável de controle que garante que apenas ciclos completos sejam contabilizados.

---

## 📏 Cálculo das Distâncias

As coordenadas fornecidas pelo MediaPipe são **normalizadas (0 a 1)**, então são convertidas para pixels:

```
x_pixel = landmark.x * largura
 y_pixel = landmark.y * altura
```

As distâncias são calculadas usando a **distância euclidiana**:

```
distancia = sqrt((x1 - x2)² + (y1 - y2)²)
```

---

## 📸 Projeto em Execução

A imagem abaixo mostra o sistema rodando, com:

* Landmarks do corpo desenhados
* Contador de polichinelos exibido na tela

<img width="1365" height="767" alt="Execução do Projeto" src="https://github.com/user-attachments/assets/bc1a1606-5e0a-4576-9fbc-a04414b40de0" />

---
## Conclusão
Projeto desenvolvido para estudos de **Visão Computacional**, **OpenCV** e **MediaPipe**, com foco em análise de movimento humano.

Sinta-se à vontade para evoluir, adaptar ou integrar este projeto a outras aplicações 🚀
