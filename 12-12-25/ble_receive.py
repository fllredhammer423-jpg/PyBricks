from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Inicializa sem broadcast, mas observa o canal 1
hub = PrimeHub(observe_channels=[1])

old = None

while True:
    message = hub.ble.observe(1)   # checa o canal 1
    if message is not None and message != old:
        print("Recebido:", message)
        old = message

    wait(100)
