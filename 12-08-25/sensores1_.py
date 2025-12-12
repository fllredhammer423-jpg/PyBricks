
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Portas:
# A - Motor_Cima Direito
# B - Motor_Cima Esquerdo
# C - Sensor Direito
# D - Sensor Esquerdo
# E - Motor_Baixo Direito
# F - Motor_Baixo Esquerdo

sensorDir = ColorSensor(Port.C)
sensorEsq = ColorSensor(Port.D)

detectable_colors(Color.WHITE, Color.BLACK) # Essas são as cores que podem ser detectadas

while True:

    corD = sensorEsq.color()
    corC = sensorDir.reflection()

    print(corD, corC)

    wait(200)