from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

motorBaixo_E = Motor(Port.E, Direction.CLOCKWISE)         # Direita
motorBaixo_F = Motor(Port.F, Direction.COUNTERCLOCKWISE)  # Esquerda

diametro = 62 # Diâmetro da roda: 62mm
abertura = 90 # Distância entre as rodas: 90mm
robo = DriveBase(motorEsq, motorDir, diametro, abertura)

drive_base = DriveBase(motorBaixo_E, motorBaixo_F, wheel_diameter=62, axle_track=90) # Seleciona motores para mover (blocos rosa)

drive_base.settings(200, 750, 150, 750)

drive_base.use_gyro(True)
