
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Sensor da Direita
sensor = ColorSensor(Port.C)

while True:
    
    # Lê o hsv
    hsv = sensor.hsv(surface=False)
    
    # Lê a cor
    color = sensor.color(surface=False)

    # Lê a luz ambiente
    ambient = sensor.ambient()

    print(hsv, color, ambient)

    wait(100)