import csv
import os
import time
from datetime import datetime

ARQUIVO_CRITICO = "confidencial.txt"
LOG_FILE = "security_logs.csv"

def registrar_evento(evento, status):
    """Registra eventos no arquivo CSV"""
    timestamp = datetime.now().isoformat()
    
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if os.stat(LOG_FILE).st_size == 0:  # Se arquivo vazio
            writer.writerow(["timestamp", "evento", "status"])
        writer.writerow([timestamp, evento, status])

def verificar_modificacao():
    """Monitora alterações no arquivo crítico"""
    if not os.path.exists(ARQUIVO_CRITICO):
        registrar_evento(f"Arquivo '{ARQUIVO_CRITICO}' não encontrado", "ERRO")
        print(f"Arquivo '{ARQUIVO_CRITICO}' não encontrado")
        return

    ultima_mod = os.path.getmtime(ARQUIVO_CRITICO)
    registrar_evento("Monitoramento iniciado", "INFO")
    print("Monitorando alterações em arquivo crítico...")

    try:
        while True:
            time.sleep(2)
            nova_mod = os.path.getmtime(ARQUIVO_CRITICO)
            if nova_mod != ultima_mod:
                msg = f"Modificação detectada em '{ARQUIVO_CRITICO}'"
                registrar_evento(msg, "ALERTA")
                print(msg)
                ultima_mod = nova_mod
    except KeyboardInterrupt:
        registrar_evento("Monitoramento interrompido", "INFO")
        print("Monitoramento interrompido")

if __name__ == "__main__":
    verificar_modificacao()
