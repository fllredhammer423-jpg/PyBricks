from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

motorDir = Motor(Port.E, Direction.CLOCKWISE)
motorEsq = Motor(Port.F, Direction.COUNTERCLOCKWISE)

# diametro = 62 # Diâmetro da roda: 62mm
# abertura = 90 # Distância entre as rodas: 90mm
# robo = DriveBase(motorEsq, motorDir, diametro, abertura)

# ---------------
# CONTROL PID
# ---------------

# NÃO MEXA - Constantes
kp = 0
ki = 0
kd = 0

# Váriavel Integral
integral = 0

motorDir.control.pid(kp, ki, kd, integral)
motorEsq.control.pid(kp, ki, kd, integral)

velocidade_desejada = 300  # deg/s

motorEsq.reset_angle(0)
motorDir.reset_angle(0)

while True:
    ang_esq = motorEsq.angle()
    ang_dir = motorDir.angle()

    erro = ang_esq - ang_dir

    motorEsq.run(velocidade_desejada - ajuste)
    motorDir.run(velocidade_desejada + ajuste)

    wait(10)
