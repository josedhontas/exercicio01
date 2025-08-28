import csv
import matplotlib.pyplot as plt
from statistics import mean, median, mode, StatisticsError

def analyze_and_plot(input_csv="ping_log.csv"):
    pings = []
    try:
        with open(input_csv, "r") as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                pings.append(float(linha["ping_ms"]))
    except FileNotFoundError:
        print(f"Erro: O arquivo '{input_csv}' não foi encontrado.")
        return
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return

    if not pings:
        print("Nenhum dado de ping encontrado no arquivo.")
        return

    media = mean(pings)
    mediana = median(pings)
    try:
        moda = mode(pings)
    except StatisticsError:
        moda = "Não existe moda única"

    print("\n--- Análise Estatística ---")
    print(f"Média: {media:.2f} ms")
    print(f"Mediana: {mediana:.2f} ms")
    print(f"Moda: {moda}")
    print("---------------------------\n")

    plt.figure(figsize=(10, 6))
    
    plt.hist(pings, bins=75, color='skyblue', edgecolor='black')
    
    plt.title("Histograma dos Pings")
    plt.xlabel("Tempo de ping (ms)")
    plt.ylabel("Frequência")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.axvline(media, color='red', linestyle='dashed', linewidth=1.5, label=f'Média: {media:.2f}')
    plt.axvline(mediana, color='green', linestyle='dashed', linewidth=1.5, label=f'Mediana: {mediana:.2f}')
    if isinstance(moda, float):
        plt.axvline(moda, color='orange', linestyle='dashed', linewidth=1.5, label=f'Moda: {moda:.2f}')

    plt.xlim(left=0, right=10)

    plt.legend()
    plt.show()