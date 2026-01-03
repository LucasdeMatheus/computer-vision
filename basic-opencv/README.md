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

Esta pasta tem como objetivo servir como base para estudos iniciais em visão computacional com OpenCV.
