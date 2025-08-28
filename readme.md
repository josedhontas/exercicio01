# Análise de Latência de Rede (Ping RTT)

Scripts em Python para coletar e analisar o tempo de resposta (ping) do gateway de rede, conforme solicitado no "Exercício n. 1 de sumarização de dados de medição".

## 🚀 Como Executar

1.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Rode o script principal:**
    ```bash
    python main.py
    ```
    - O script coletará 100 amostras de ping (se o arquivo `ping_log.csv` não existir) e depois exibirá o gráfico da análise.

## 📊 Resultados e Análise

O script gera o histograma e as métricas de tendência central para responder às questões da atividade.

### Histograma dos Pings

![Histograma dos Pings](histograma_pings.png)

### Conclusões do Exercício

1.  **A distribuição é simétrica ou assimétrica?**
    É uma **distribuição assimétrica positiva** (ou à direita). A maioria dos dados se concentra em valores baixos, com uma cauda longa se estendendo para a direita devido a pings mais altos e menos frequentes (outliers).

2.  **Qual índice de tendência central é mais representativo?**
    A **Mediana** é o índice mais representativo. Diferente da Média, ela não é afetada pelos valores extremos (outliers) da cauda. Portanto, a Mediana descreve melhor o comportamento *típico* e a latência mais comum da rede.