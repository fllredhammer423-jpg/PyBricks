from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

motorBaixo_E = Motor(Port.E, Direction.CLOCKWISE)         # Direita
motorBaixo_F = Motor(Port.F, Direction.COUNTERCLOCKWISE)  # Esquerda

diametro = 62.4 # Diâmetro da roda: 62mm
abertura = 70 # Distância entre as rodas: 90mm
robo = DriveBase(motorBaixo_E, motorBaixo_F, diametro, abertura)

#Padrão
robo.settings(200, 750, 150, 500)

# Robô utiliza giroscópio para andar agora
robo.use_gyro(True)

# Função de resetar ângulo
def reset_angle():
    hub.imu.reset_heading(0)

# Função de girar o robô
def girar(vel, alvo):
    reset_angle()

    # Pega o ângulo atual do robô (0)
    angle = robo.angle()

    if alvo < 0:
        # Inicia o giro com as duas rodas
        motorBaixo_F.run(-vel)
        motorBaixo_E.run(vel)

        while angle > alvo:
            angle = robo.angle()
            wait(5)
    else:
        # Inicia o giro com as duas rodas
        motorBaixo_F.run(vel)
        motorBaixo_E.run(-vel)

        while angle < alvo:
            angle = robo.angle()
            wait(5)
    
    print(angle)
    
    motorBaixo_F.stop()
    motorBaixo_E.stop()

girar(300, 90)
wait(100)
girar(300, -90)
