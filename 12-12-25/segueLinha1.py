
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Sensor Direito - Colocando o sensor de cor C em uma variavel
sensor = ColorSensor(Port.C)

motorBaixo_E = Motor(Port.E, Direction.CLOCKWISE)         # Direita
motorBaixo_F = Motor(Port.F, Direction.COUNTERCLOCKWISE)  # Esquerda

diametro = 62.4 # Diâmetro da roda: 62mm
abertura = 70 # Distância entre as rodas: 90mm
robo = DriveBase(motorBaixo_E, motorBaixo_F, diametro, abertura)

#Padrão
robo.settings(200, 750, 150, 500)

# Robô utiliza giroscópio para andar agora
robo.use_gyro(True)

# HSV das cores: preto e branco
Color.BLACK = Color(h=180, s=20, v=13)
Color.WHITE = Color(h=200, s=7, v=60)
Color.GRAY = Color(h=240, s=5, v=36)
Color.BLUE = Color(h=205, s=89, v=40)

# Joga esses valores em uma lista
minhas_cores = [Color.BLACK, Color.WHITE, Color.GRAY, Color.BLUE]

# Joga a lista para o spike obter os novos valores
sensor.detectable_colors(minhas_cores)

# Função de resetar ângulo
def reset_angle():
    hub.imu.reset_heading(0)

# Função de girar o robô
def girar(velocidade, alvo):
    reset_angle()

    # Pega o ângulo atual do robô (0)
    angle = robo.angle()

    if alvo < 0:
        # Inicia o giro com as duas rodas
        motorBaixo_F.run(-velocidade)
        motorBaixo_E.run(velocidade)

        while angle > alvo:
            angle = robo.angle()
            wait(5)
    else:
        # Inicia o giro com as duas rodas
        motorBaixo_F.run(velocidade)
        motorBaixo_E.run(-velocidade)

        while angle < alvo:
            angle = robo.angle()
            wait(5)
    
    print(angle)
    
    motorBaixo_F.stop()
    motorBaixo_E.stop()

def leituraHSV(delay):
    hsv = sensor.hsv()
    print(hsv)
    wait(delay)

def leituraCores(delay):
    cor = sensor.color()
    hsv = sensor.hsv()

    # Condicional para a decisâo: preto ou branco
    if cor == Color.BLACK:
        print('Preto!', hsv)

    elif cor == Color.WHITE:
        print('Branco!', hsv)

    elif cor == Color.GRAY:
        print('Cinza!', hsv)

    # Condicional para o azul
    elif cor == Color.BLUE:
        print('Azul!', hsv)

    wait(delay)

def segueLinha(velocidade):
    # 'cor' para detectar a cor
    cor = sensor.color()
    # 'hsv' para detectar a hsv
    hsv = sensor.hsv()

    # Condicional para a decisâo: preto ou branco
    if cor == Color.BLACK:
        motorBaixo_F.run(velocidade/10)
        motorBaixo_E.run(velocidade)

    elif cor == Color.WHITE:
        motorBaixo_F.run(velocidade)
        motorBaixo_E.run(velocidade/10)

    # Condicional para o azul
    elif cor == Color.BLUE:
        print('Azul')
        girar(300, 90)

    wait(1)

while True:
    segueLinha(300)