
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Sensor Direito - Colocando o sensor de cor C em uma variavel
sensor = ColorSensor(Port.C)

# HSV das cores: preto e branco
Color.BLACK = Color(h=240, s=15, v=7)
Color.WHITE = Color(h=206, s=11, v=69)

# Joga esses valores em uma lista
minhas_cores = [Color.BLACK, Color.WHITE]

# Joga a lista para o spike obter os novos valores
sensor.detectable_colors(minhas_cores)

while True:
    # 'cor' para detectar a cor
    cor = sensor.color()
    # 'hsv' para detectar a hsv
    hsv = sensor.hsv()

    # Condicional para a decisâo: preto ou branco
    if cor == Color.BLACK:
        print('Preto! \n', hsv)
    elif cor == Color.WHITE:
        print('Branco! \n', hsv)
    else:
        print('Tentando detectar...')

    wait(100)