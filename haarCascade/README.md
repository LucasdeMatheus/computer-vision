# Haar Cascade com OpenCV (Resumo)

Este projeto demonstra o uso de **Haar Cascade** no OpenCV para **captura de imagens**, **treinamento** e **detecção de objetos** em tempo real, utilizando Python.

---

## O que é Haar Cascade?

Haar Cascade é uma técnica clássica de visão computacional baseada em **features Haar** e **classificadores em cascata**. Ela analisa contrastes claros e escuros da imagem para identificar padrões específicos (como olhos, rostos ou objetos).

É uma abordagem leve, rápida e muito usada para estudos e aplicações simples em tempo real.

---

## Cascade Trainer (Treinamento)

O treinamento de um Haar Cascade **não é feito em Python**.

Ele utiliza o **Cascade Trainer**, que é o **software próprio do Haar Cascade no OpenCV**. Neste projeto, o treinamento é realizado utilizando a interface gráfica:

**CascadeTrainerGUI_3.3.1_x64_Setup.exe**

Essa ferramenta é uma GUI que encapsula os utilitários oficiais do OpenCV, como:

* `opencv_createsamples`
* `opencv_traincascade`

O Cascade Trainer recebe imagens **positivas** e **negativas** e gera o arquivo final:

```
cascade.xml
```

Esse arquivo é o classificador que será carregado nos scripts Python para detecção.

---

## Captura de Imagens Positivas

O código de captura utiliza a webcam para salvar imagens em **escala de cinza** ao pressionar a tecla **Q**. Essas imagens são usadas como dataset positivo no treinamento do cascade.

Pontos importantes:

* Conversão para grayscale
* Padronização de tamanho
* Salvamento automático

---

## Detecção com Cascade Treinado

Após o treinamento, o arquivo `cascade.xml` é carregado com `cv2.CascadeClassifier` e utilizado para detectar objetos em tempo real com `detectMultiScale`.

Os retângulos desenhados indicam as regiões detectadas pelo classificador.

---

## Uso de Cascades Prontos

O OpenCV também disponibiliza **cascades prontos**, como o `haarcascade_eye.xml`, que podem ser usados diretamente sem treinamento, servindo como base de estudo e testes.

---

## Observações Importantes

* A qualidade do cascade depende diretamente do dataset
* Iluminação e ângulo influenciam bastante o resultado
* Haar Cascade é sensível a rotações

---

## Finalidade do Projeto

Este material tem foco **educacional**, servindo como base para:

* Entender detecção de objetos clássica
* Aprender o funcionamento do Haar Cascade
* Preparar terreno para técnicas mais modernas (CNNs, YOLO, etc.)
