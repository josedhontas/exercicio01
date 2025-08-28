from pythonping import ping
import time
import csv
from datetime import datetime

def collect_ping_data(router_ip="192.168.3.1", output_csv="ping_log.csv", num_loops=100, pings_por_loop=5, intervalo=1):
    print(f"Iniciando a coleta de dados de ping para {router_ip}...")
    with open(output_csv, "w", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(["timestamp", "ping_ms"])

    for i in range(num_loops):
        try:
            resultado = ping(router_ip, count=pings_por_loop)
            tempo_medio = resultado.rtt_avg_ms

            print(f"[{i+1}/{num_loops}] Ping médio: {tempo_medio:.2f} ms")

            timestamp = datetime.utcnow().isoformat()
            with open(output_csv, "a", newline="") as f:
                escritor = csv.writer(f)
                escritor.writerow([timestamp, tempo_medio])

        except Exception as e:
            print(f"Erro ao pingar: {e}")

        time.sleep(intervalo)
    print(f"Ping concluído e dados salvos em {output_csv}!")