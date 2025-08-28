import os
from data_collector import collect_ping_data
from data_analyzer import analyze_and_plot

ROUTER_IP = "192.168.3.1"
CSV_FILE = "ping_log.csv"
NUM_LOOPS = 100
PINGS_PER_LOOP = 5
INTERVAL = 1

def main():
    if not os.path.exists(CSV_FILE):
        collect_ping_data(
            router_ip=ROUTER_IP,
            output_csv=CSV_FILE,
            num_loops=NUM_LOOPS,
            pings_por_loop=PINGS_PER_LOOP,
            intervalo=INTERVAL
        )
    else:
        print(f"O arquivo '{CSV_FILE}' já existe. Pulando a etapa de coleta de dados.")

    analyze_and_plot(input_csv=CSV_FILE)

if __name__ == "__main__":
    main()