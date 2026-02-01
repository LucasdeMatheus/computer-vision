# 👁️ Detecção de Olhos Abertos e Fechados com MediaPipe

Este projeto demonstra como detectar, em tempo real, se uma pessoa está com os **olhos abertos ou fechados** usando **Python**, **OpenCV** e **MediaPipe Face Mesh**.

A lógica é baseada na relação entre a **altura** e a **largura** do olho (EAR – *Eye Aspect Ratio*). Quando o olho fecha, a distância vertical entre as pálpebras diminui drasticamente.

---

## 🧠 Lógica Utilizada (na prática)

Para cada olho:

1. Capturamos dois pontos verticais (pálpebra superior e inferior)
2. Capturamos dois pontos horizontais (cantos do olho)
3. Calculamos:

```
EAR = altura_do_olho / largura_do_olho
```

* EAR **alto** → olho aberto
* EAR **baixo** → olho fechado

Os olhos são considerados fechados **apenas quando ambos** estão abaixo do limiar.

---

## 📍 Pontos do Face Mesh Usados

### Olho esquerdo

* 159 → pálpebra superior
* 145 → pálpebra inferior
* 33  → canto esquerdo
* 133 → canto direito

### Olho direito

* 386 → pálpebra superior
* 374 → pálpebra inferior
* 362 → canto esquerdo
* 263 → canto direito

Esses pontos fazem parte do **MediaPipe Face Mesh (468 landmarks)**.

---

## 🧪 Parâmetro Importante

```python
EAR_THRESHOLD = 0.18
```

Esse valor pode variar conforme:

* Distância da câmera
* Iluminação
* Formato do olho da pessoa

🔧 Ajuste esse número até obter um resultado estável.

---

## 🎨 Feedback Visual

* 🟢 Texto verde → olhos abertos
* 🔴 Texto vermelho → olhos fechados

O texto é desenhado em tempo real sobre o vídeo usando OpenCV.

---

## 📚 Tecnologias Utilizadas

* OpenCV
* MediaPipe Face Mesh
* Python

---

## 🧠 Observação Final

Esse projeto é uma excelente base para estudos de:

* Visão Computacional
* Biometria
* Detecção de fadiga
* Interação humano–computador

Se quiser evoluir isso pra algo mais profissional (tipo Drowsiness Detection), é só continuar expandindo a lógica 🚀
