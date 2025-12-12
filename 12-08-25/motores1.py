
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

motorCima_A = Motor(Port.A)  # Direita
motorCima_B = Motor(Port.B)  # Esquerda

motorBaixo_E = Motor(Port.E, Direction.CLOCKWISE)         # Direita
motorBaixo_F = Motor(Port.F, Direction.COUNTERCLOCKWISE)  # Esquerda

drive_base = DriveBase(motorBaixo_E, motorBaixo_F, wheel_diameter=62, axle_track=90) # Seleciona motores para mover (blocos rosa)

drive_base.settings(200, 750, 150, 750) # Padrão - (velocidade_mover, aceleração_mover, velocidade_girar, aceleração_girar)

drive_base.straight(200) # Pra frente -> 200mm ou 20cm
drive_base.arc(200, 90)  # Faz curva -> Raio: 200mm ou 20cm - Graus: 90°
drive_base.turn(90)      # Gira -> 90°
