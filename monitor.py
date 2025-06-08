import os
import time
from datetime import datetime

ARQUIVO_CRITICO = "confidencial.txt"
LOG_FILE = "security_log.txt"


def registrar_evento(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")


def verificar_modificacao():
    if not os.path.exists(ARQUIVO_CRITICO):
        registrar_evento(f"Arquivo '{ARQUIVO_CRITICO}' não encontrado.")
        print(f"Arquivo '{ARQUIVO_CRITICO}' não encontrado.")
        return

    ultima_mod = os.path.getmtime(ARQUIVO_CRITICO)
    registrar_evento("Monitoramento iniciado.")
    print("Monitorando alterações em arquivo crítico...")

    try:
        while True:
            time.sleep(2)
            nova_mod = os.path.getmtime(ARQUIVO_CRITICO)
            if nova_mod != ultima_mod:
                registrar_evento(f"Arquivo '{ARQUIVO_CRITICO}' foi modificado.")
                print(f"Arquivo '{ARQUIVO_CRITICO}' foi modificado.")
                ultima_mod = nova_mod
    except KeyboardInterrupt:
        registrar_evento("Monitoramento interrompido pelo usuário.")
        print("Monitoramento interrompido.")


if __name__ == "__main__":
    verificar_modificacao()
