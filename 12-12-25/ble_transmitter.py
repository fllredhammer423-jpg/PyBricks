from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Inicializa o hub e configura o canal de broadcast
hub = PrimeHub(broadcast_channel=1)

count = 0

while True:
    data = ("A", count)      # qualquer dado pequeno
    hub.ble.broadcast(data)  # envia no canal
    count += 1
    wait(200)                # não precisa enviar sempre
