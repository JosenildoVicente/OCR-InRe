# OCR-InRe
Um detector, extrator e minerador de textos de imagens de faturas
##  Visão Geral

Uma aplicação OCR para detecção e extração de dados, seleção de atributos, estruturação de dados e descoberta de conhecimento usando técnicas de aprendizado de máquina para gerar insights úteis para tomadas de decisões empresarias

[Link da Apresentação do Projeto](https://drive.google.com/file/d/1FG7Ndkb7madwut61d_A4NNmf8GSbLpF4/view?usp=sharing)

##  Problema
Criação de modelos Optical Character Recognition (OCR) para diferentes layouts consomem muito tempo, problemas na identificação de expressões regulares complexas, baixa acurácia, alto tempo de processamento e deficiência   de manter uma precisão após pequenas alterações de layout. Leitura  de cópia de faturas de fornecedores e redes de suprimentos

## Proposta de solução

Para solução do problema as seguintes etapas são necessárias 
1. Desenvolvimento de um aplicação para detecção e extração de dados de faturas digitalizadas.
2. Geração das features principais (.json) afim de criar uma estruturação dos dados.
3. Processo de preparação, mineração e pós-processamento de dados visando extrair padrões interessantes, relevantes e inéditos e eventualmente ocultos (desenvolvimento futuro).
4. Suporte a novos templates (desenvolvimento futuro)
5. Implementação de outras técnicas de OCR em estado da arte (desenvolvimento futuro)

# Informações Técnicas
## Gráfico explicativo
![Captura de Tela 2021-10-28 às 21 38 15](https://user-images.githubusercontent.com/7680448/139354598-5a928b18-4f08-4024-9e76-2a566677320f.png)

## Pré-requisitos

  - Sistema Operacional
    - Ubuntu 20.04
  - Linguagem Utilizada
    - Python 3.1
  - Ambiente virtual
    - Virtualenv (organização de requisitos)
  - Bibliotecas
    - Google Tesseract (pytesseract)
    - pdf2image
    - Opencv
    - Pandas
    - Numpy
    - Json
    - Pill

### Processo de instalação e execução

  - Todas as bibliotecas utilizadas estão no arquivo [requirements.txt](https://github.com/JosenildoVicente/OCR-InRe/blob/main/requirements.txt)
      ```
      pip install -r requirements.txt
      ```
  - Execução
    - Para executar o programa digite o seguinte código
      ```
      python invoicereader.py
      ```
    - Coloque o caminho do arquivo PDF para começa a execução (arquivo pdf fornecido pela organização do hackaton /seu_path/nome_arquivo)
    - exemplo: 
      - /seu_path/MXO0492981.pdf 
      - /seu_path/MXO0493210.pdf 
      - /seu_path/MXO0497759.pdf 
      - /seu_path/MXO0500211.pdf
      - /seu_path/MXO0505702.pdf
    - Será gerado um arquivo JSON no mesmo diretório do arquivo PDF fornecido

# Time 

| [<img src="https://user-images.githubusercontent.com/7680448/139342517-45bdbefc-5032-432a-9ffb-c17e36937fe8.jpg" width="115"><br><sub>@Ailton3112</sub>](https://github.com/Ailton3112) | [<img src="https://avatars.githubusercontent.com/u/22326734?v=4" width="115"><br><sub>@JosenildoVicente</sub>](https://github.com/JosenildoVicente) |
| :---: | :---: |
