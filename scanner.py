import socket
from datetime import datetime

alvo = input("IP ou host para escanear: ")
ip = socket.gethostbyname(alvo)

print(f"\nEscaneando o IP: {ip}")
print(f"Início: {datetime.now()}\n" + "-"*40)

portas = [21, 22, 23, 25, 53, 80, 110, 135, 443, 445, 3306, 8080]

try:
    for porta in portas:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        
        if s.connect_ex((ip, porta)) == 0:
            print(f"Porta {porta} -> ABERTA")
        s.close()

except KeyboardInterrupt:
    print("\nCancelado pelo usuário.")
except socket.gaierror:
    print("\nErro: Host não resolvido.")

print("-"*40 + "\nFim do scan.")