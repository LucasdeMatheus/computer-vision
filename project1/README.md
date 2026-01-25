# 🚗 Sistema de Detecção de Vagas de Estacionamento com OpenCV

## 📌 Visão Geral do Projeto

Este projeto tem como objetivo identificar automaticamente quais vagas de um estacionamento estão **livres** ou **ocupadas** utilizando **Visão Computacional**.

A ideia central é simples e eficiente:

1. **Mapear manualmente as vagas** em uma imagem estática
2. **Salvar esse mapeamento** para reutilização
3. **Processar o vídeo em tempo real**
4. **Analisar cada vaga individualmente**
5. **Classificar as vagas como livres ou ocupadas** com base na quantidade de pixels detectados

Esse tipo de solução é muito utilizada em:

* Estacionamentos inteligentes
* Cidades inteligentes (Smart Cities)
* Monitoramento automatizado
* Projetos acadêmicos de visão computacional

---

## 🧠 Ideia do Funcionamento

O projeto funciona em **duas etapas principais**:

### 1️⃣ Mapeamento das Vagas

* O usuário seleciona manualmente cada vaga na imagem
* Cada vaga é representada por um retângulo `(x, y, largura, altura)`
* As coordenadas são salvas em um arquivo para uso posterior

### 2️⃣ Análise do Vídeo

* O vídeo é processado frame a frame
* A imagem passa por diversos filtros
* Cada vaga mapeada é analisada separadamente
* A quantidade de pixels brancos indica se a vaga está ocupada ou livre

---

## 🗺️ Etapa 1 – Mapeamento das Vagas

Nesta etapa, uma imagem fixa do estacionamento é utilizada para definir manualmente onde estão as vagas.

### 🔹 Processo:

* A imagem é carregada
* O usuário seleciona cada vaga usando o mouse
* As coordenadas são armazenadas em uma lista
* O mapeamento é salvo em um arquivo `.pkl`

📂 Arquivo gerado:

```
spaces.pkl
```

Este arquivo contém todas as posições das vagas e será reutilizado na etapa de análise do vídeo.

---

## 🎥 Etapa 2 – Processamento do Vídeo

Com as vagas já mapeadas, o sistema começa a analisar o vídeo do estacionamento.

### 🔹 Tratamento da Imagem

Cada frame do vídeo passa pelos seguintes passos:

1. Conversão para tons de cinza
2. Limiarização adaptativa (Threshold)
3. Remoção de ruído com Median Blur
4. Dilatação para reforçar os objetos detectados

Esses filtros facilitam a identificação de veículos nas vagas.

---

## 📊 Análise das Vagas

Para cada vaga mapeada:

* Um recorte da imagem é feito
* Conta-se a quantidade de pixels brancos
* Se o valor ultrapassar um limite, a vaga é considerada **ocupada**
* Caso contrário, é considerada **livre**

### 🔹 Critério de Classificação

* 🔴 **Vaga Ocupada** → muitos pixels brancos
* 🟢 **Vaga Livre** → poucos pixels brancos

O valor limite pode ser ajustado conforme:

* Iluminação
* Qualidade do vídeo
* Tamanho das vagas

---

## 📈 Contagem de Vagas Livres

O sistema exibe em tempo real:

* Quantidade de vagas livres
* Total de vagas

Exemplo:

```
15/69 vagas livres
```

---

## 🖼️ Demonstração

### 🎥 Resultado do Projeto em Execução

A imagem abaixo mostra o sistema em funcionamento, com:

* 🔴 **Retângulos vermelhos** indicando vagas **ocupadas**
* 🟢 **Retângulos verdes** indicando vagas **livres**
* 🔢 **Contagem de pixels** usada para a decisão em cada vaga
* 📊 **Contador geral de vagas livres** no canto da tela

<img width="1365" height="767" alt="Resultado do sistema de detecção de vagas" src="https://github.com/user-attachments/assets/7387a93d-0bd2-44cb-a67b-24af1929cb56" />

Essa visualização facilita a validação do algoritmo, permitindo observar em tempo real como cada vaga está sendo classificada.

---

## 🛠️ Tecnologias Utilizadas

* Python
* OpenCV
* NumPy
* Pickle

---

## 🚀 Possíveis Melhorias

* Ajuste automático do limiar de pixels
* Uso de aprendizado de máquina
* Detecção noturna
* Interface gráfica
* Integração com sistemas web ou mobile

---

## 📚 Conclusão

Este projeto demonstra como é possível resolver um problema real utilizando **visão computacional tradicional**, sem necessidade de redes neurais.

Ele serve como uma excelente base para projetos mais avançados envolvendo:

* Inteligência Artificial
* Automação
* Sistemas inteligentes

---

✍️ Desenvolvido para fins educacionais e estudo em Visão Computacional.
