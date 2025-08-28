# Análise de Latência de Rede (Ping RTT)
## Aluno: José Dhonatas Alves Sales

 Exercício n. 1 de sumarização de dados de medição

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


### Histograma dos Pings
<img width="922" height="569" alt="image" src="https://github.com/user-attachments/assets/134d2a27-7276-49a5-8425-78da6280943a" />


### Conclusões do Exercício

1.  **A distribuição é simétrica ou assimétrica?**
    É uma distribuição assimétrica. A maioria dos dados se concentra em valores baixos, tem poucos outliers. 
2.  **Qual índice de tendência central é mais representativo?**
    Nesse caso ai seria a mediana o índice mais representativo. A média é afetava por outras coisas, como os valores outliers. Desse modo, a mediana descreve o comportamento mais normal da minha rede.
