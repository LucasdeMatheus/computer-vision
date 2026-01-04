# OpenCV Básico com Python

---

## Estrutura de Pastas

```text
basic-opencv/
├── media/        # Imagens e vídeos usados nos exemplos
├── clippings/    # Recortes de imagens salvos pelo programa
└── *.py          # Scripts de estudo
```

---

## Leitura e Exibição de Imagem

Exemplo básico de leitura de uma imagem e exibição em uma janela.

O `cv2.imread` carrega a imagem e o `cv2.imshow` exibe o conteúdo. A função `cv2.waitKey(0)` mantém a janela aberta até uma tecla ser pressionada.

```python
img = cv2.imread("basic-opencv/media/BAH.jpg")
cv2.imshow("image", img)
cv2.waitKey(0)
```

---

## Conversão de Cores

O OpenCV trabalha nativamente com o formato **BGR**. A conversão para escala de cinza é feita com `cv2.cvtColor`.

```python
greyImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
```

A função `shape` mostra as dimensões da imagem:

```python
print(img.shape)  # (altura, largura, canais)
```

---

## Seleção e Recorte de Região (ROI)

O `cv2.selectROI` permite selecionar uma área da imagem com o mouse. Ele retorna:

```
(x, y, largura, altura)
```

Com esses valores, é possível recortar a imagem usando slicing do NumPy.

```python
cut = img[y:y+h, x:x+w]
```

---

## Salvando Imagens

Para salvar uma imagem no disco, utilize `cv2.imwrite`. O diretório deve existir antes da execução.

```python
cv2.imwrite("basic-opencv/clippings/cut.jpg", cut)
```

A função retorna `True` se a imagem foi salva com sucesso.

---

## Captura de Webcam

A webcam é acessada com `cv2.VideoCapture(0)`. O loop lê frames continuamente até que o usuário pressione a tecla **q**.

```python
cam = cv2.VideoCapture(0)

while True:
    check, img = cam.read()
    cv2.imshow("web cam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

Também é possível ajustar propriedades como resolução e brilho usando `cam.set`.

---

## Leitura de Vídeo

Vídeos podem ser lidos da mesma forma que a webcam, passando o caminho do arquivo.

```python
video = cv2.VideoCapture("basic-opencv/media/BAH.mp4")
```

Cada frame pode ser redimensionado com `cv2.resize` antes da exibição.

---

## Debuggers úteis

* Sempre verifique se `cv2.imread` ou `VideoCapture.read` retornaram dados válidos.
* Se um recorte não for salvo, verifique se a ROI possui largura e altura maiores que zero.
* Caminhos relativos dependem do diretório onde o script é executado.

---

## Separação de Objetos em Imagens (Contornos)

Este exemplo faz parte de um **projeto de separação de objetos**, cujo objetivo é identificar múltiplos objetos em uma imagem e salvá-los individualmente.

O fluxo utiliza técnicas clássicas de visão computacional:

* Conversão para escala de cinza
* Detecção de bordas com Canny
* Fechamento morfológico para unir contornos
* Detecção de contornos externos
* Enquadramento e recorte de cada objeto

Exemplo de referência:

```python
contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
```

Cada contorno representa um objeto detectado na imagem.

---

---

## Threshold (Binarização de Imagens)

O threshold é utilizado para converter uma imagem em escala de cinza em uma imagem binária (preto e branco).

O OpenCV oferece dois tipos principais abordados neste estudo:

* **Threshold simples**: utiliza um valor fixo de limiar, indicado para imagens com iluminação uniforme.

```python
_, th = cv2.threshold(greyImg, 80, 255, cv2.THRESH_BINARY)
```

* **Threshold adaptativo**: calcula o limiar localmente, sendo mais eficaz em imagens com sombras.

```python
th = cv2.adaptiveThreshold(greyImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 47, 10)
```

Essas técnicas são muito utilizadas em segmentação de texto e OCR.

---

---

## Operações Morfológicas

As operações morfológicas modificam estruturas binárias da imagem e são usadas para limpeza de ruído e reforço de objetos.

Principais operações estudadas:

* **Dilatação**: expande regiões brancas

```python
dilate = cv2.dilate(img, (5,5), iterations=5)
```

* **Erosão**: reduz regiões brancas

```python
erode = cv2.erode(img, (5,5), iterations=2)
```

* **Abertura (Open)**: remove ruído fino
* **Fechamento (Close)**: fecha falhas nos objetos

Essas operações são frequentemente combinadas com Canny e threshold.

---

---

## Desenho de Formas e Texto

O OpenCV permite desenhar elementos gráficos diretamente sobre imagens para visualização e depuração.

Recursos utilizados:

* **Retângulos** (delimitação de regiões)

```python
cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
```

* **Círculos**, **linhas** e **texto**, úteis para marcação visual de informações.

Esses recursos são amplamente usados para exibir resultados de algoritmos de visão computacional.

---

---

Esta pasta tem como objetivo servir como base para estudos iniciais em visão computacional com OpenCV.
