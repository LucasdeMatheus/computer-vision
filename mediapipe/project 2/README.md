# ✋ Contador de Dedos com MediaPipe Hands

![Demonstração do projeto](https://github.com/user-attachments/assets/95759941-85f4-451a-b040-475cda60003b)

Este projeto utiliza **Visão Computacional com Python** para detectar uma mão em tempo real e **contar automaticamente quantos dedos estão levantados**, usando o modelo **Hand Landmark** do **MediaPipe**.

A imagem acima mostra o sistema em funcionamento, identificando os pontos da mão (landmarks) e exibindo visualmente os dedos reconhecidos pela câmera.

---

## 🎯 Objetivo

* Detectar uma mão em tempo real pela câmera
* Identificar os landmarks da mão
* Determinar quais dedos estão levantados
* Exibir na tela a quantidade de dedos levantados

---

## 🧠 Tecnologias Utilizadas

* **Python 3**
* **OpenCV** – captura e exibição de vídeo
* **MediaPipe Hands** – detecção e rastreamento dos pontos da mão

---

## 🖐️ Lógica de Identificação dos Dedos

### Dedos Indicador, Médio, Anelar e Mindinho

Para esses dedos, a lógica compara a posição **vertical (eixo Y)** da ponta do dedo com a articulação inferior:

> Se a ponta do dedo estiver acima da articulação → dedo levantado

Isso funciona porque, na imagem, o eixo Y cresce de cima para baixo.

---

### 👍 Polegar (Tratamento Especial)

O polegar se move lateralmente, então a verificação depende de **qual mão foi detectada**:

* **Mão esquerda** → o polegar está levantado se o ponto 4 estiver à direita do ponto 2
* **Mão direita** → o polegar está levantado se o ponto 4 estiver à esquerda do ponto 2

Essa diferenciação é feita usando:

```
results.multi_handedness
```

---

## 📌 Exemplo de Lógica em Código

```python
if point:
    for x in finger:
        if pointsFinger[x][1] < pointsFinger[x-2][1]:
            count += 1

    if results.multi_handedness[0].classification[0].label == "Left":
        if pointsFinger[4][0] > pointsFinger[2][0]:
            count += 1
    else:
        if pointsFinger[4][0] < pointsFinger[2][0]:
            count += 1
```

---

## 🚀 Possíveis Melhorias

* Suporte a **duas mãos simultâneas**
* Reconhecimento de **gestos específicos**
* Integração com **interfaces gráficas**
* Uso em **automação e jogos**

---

## 📷 Resultado

O sistema identifica corretamente a mão, os dedos levantados e exibe o total em tempo real, como mostrado na imagem de apresentação do projeto.

---

✨ Projeto ideal para estudos de **Visão Computacional**, **IA aplicada** e **OpenCV + MediaPipe**.
