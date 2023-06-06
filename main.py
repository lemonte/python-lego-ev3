#!/usr/bin/env pybricks-micropython

from biblioteca import Robo, RoboCor, RoboMotor, SeguidorLinha
import math
import time

cor_direita = RoboCor(Port=4, cor_branco=(198, 191, 187), cor_preto=(14, 22, 21))

cor_esquerda = RoboCor(Port=3, cor_branco=(176, 149, 86), cor_preto=(16, 28, 21))

motor_direita = RoboMotor(Port="d", velocidade=20)

motor_esquerda = RoboMotor(Port="a", velocidade=20)



robo = Robo(
    diametro_robo=125,
    diametro_roda=55,
    motor_direito=motor_direita,
    motor_esquerdo=motor_esquerda,
)


seguidor = SeguidorLinha()
verde = [19, 56, 36]
preto = [1, 1, 1]
branco = [100, 100, 100]


def calibrarCor():
    rgb_direito = cor_direita.rgb()
    rgb_esquerdo = cor_esquerda.rgb()
    print("cor dir => ", rgb_direito)
    print("cor esq => ", rgb_esquerdo)

# while True:
#     calibrarCor()
#     wait(1000)

def calcular_proximidade(referencia, entrada):
    if len(referencia) != len(entrada):
        raise ValueError("As tuplas devem ter o mesmo número de elementos.")

    diferenca_por_posicao = tuple(r - e for r, e in zip(referencia, entrada))
    return diferenca_por_posicao



def converter_para_porcentagem(sensor):
    entrada = sensor.rgb()
    valores_minimos = sensor.__valor_minimo
    valores_maximos = sensor.__valor_maximo
    if len(entrada) == 0:
        raise ValueError("A tupla de entrada deve conter pelo menos um elemento.")
    if len(entrada) != len(valores_minimos) or len(entrada) != len(valores_maximos):
        raise ValueError("As tuplas de valores mínimos e máximos devem ter o mesmo número de elementos.")

    porcentagens = []
    for e, min_val, max_val in zip(entrada, valores_minimos, valores_maximos):
        if min_val >= max_val:
            raise ValueError("Cada valor mínimo deve ser menor que o valor máximo correspondente.")
        faixa_valores = max_val - min_val
        porcentagem = (e - min_val) / faixa_valores * 100
        if(porcentagem < 0):
            porcentagem = 0
        porcentagens.append(round(porcentagem))

    return tuple(porcentagens)

def pegar_rgb_esq():
    return converter_para_porcentagem(cor_esquerda)

def pegar_rgb_dir():
    return converter_para_porcentagem(cor_direita)



def encontrouPreto(valor):
    prox = calcular_proximidade(preto, valor)
    for valor in prox:
        if valor >= 5 or valor <= -5:
            return False
    return True



def encontrouBranco(valor):
    prox = calcular_proximidade(branco, valor)
    for valor in prox:
        if valor >= 10 or valor <= -10:
            return False
    return True


def encontrouVerde(valor):
    # prox = calcular_proximidade(verde, valor)
    r, g, b = valor
    return (((g - 18) >= r) and (g > (r + b)) and (g > (2 * r)))
    # for valor in prox:
    #     if valor >= 5 or valor <= -5:
    #         return False
    # return True


def virarAteEncontrarLinha(lado):
    robo.paraMotores()
    motor_direita.moverComPotencia(-lado * 50)
    motor_esquerda.moverComPotencia(lado * 50)
    if(lado == -1):
        sensor = pegar_rgb_esq()
        while(not encontrouPreto(sensor)):
            sensor = pegar_rgb_esq()
        while(not encontrouBranco(sensor)):
            sensor = pegar_rgb_esq()
            continue
    else:
        sensor = pegar_rgb_dir()
        while(not encontrouPreto(sensor)):
            sensor = pegar_rgb_dir()
        while(not encontrouBranco(sensor)):
            sensor = pegar_rgb_dir()
            continue
    robo.paraMotores()

    
# while True:
#     rgb_dir = pegar_rgb_dir()
#     rgb_esq = pegar_rgb_esq()
#     print(rgb_esq, " ", rgb_dir)
#     print(encontrouBranco(rgb_esq), " ", encontrouBranco(rgb_dir))
#     time.sleep(1)


def encontrarLinha(angulo, lado):
    if(lado == 0):
        return
    if(angulo < 360):
        robo.moverParaTras(velocidade=300)
        while(not encontrouPreto(pegar_rgb_esq()) and not encontrouPreto(pegar_rgb_dir())):
            continue
        robo.paraMotores()
        virarAteEncontrarLinha(lado)
        


lado = 0
angulo = 0     

while True:
    rgb_dir = pegar_rgb_dir()
    rgb_esq = pegar_rgb_esq()

    if(encontrouVerde(rgb_dir)):
        print('sensor da direta')
        robo.paraMotores()
        motor_direita.resetarAnguloMotor()
        robo.moverParaFrente(velocidade=300)
        while(motor_direita.pegarAnguloDoMotor() < 180):
            rgb_dir = pegar_rgb_dir()
            rgb_esq = pegar_rgb_esq()
            if(encontrouVerde(rgb_esq)):
                print('sensor da esquerda')
                robo.virarAngulo(340)
                virarAteEncontrarLinha(1)
                break
            if(encontrouPreto(rgb_dir)):
                print('encontrou o preto')
                robo.virar90grausDireita()
                break
        robo.paraMotores()
        # break
    elif(encontrouVerde(rgb_esq)):
        print('sensor da esquerda')
        robo.paraMotores()
        motor_direita.resetarAnguloMotor()
        robo.moverParaFrente(velocidade=300)
        while(motor_direita.pegarAnguloDoMotor() < 180):
            rgb_dir = pegar_rgb_dir()
            rgb_esq = pegar_rgb_esq()
            print(rgb_dir)
            if(encontrouVerde(rgb_dir)):
                print('sensor da direita')
                robo.virarAngulo(340)
                virarAteEncontrarLinha(1)
                break
            if(encontrouPreto(rgb_esq)):
                print('encontrou o preto')
                robo.virar90grausEsquerda()
                break
        robo.paraMotores()

    # if(encontrouBranco(rgb_dir) and encontrouBranco(rgb_esq)):
    #     print(motor_direita.pegarAnguloDoMotor())
    #     encontrarLinha(motor_direita.pegarAnguloDoMotor(), lado)
    #     lado = 0
    #     angulo = 100000
    
    # elif(encontrouPreto(rgb_esq)):
    #     print("encontrou preto lado esquerdo")
    #     lado = -1
    #     angulo = motor_direita.resetarAnguloMotor()
    
    # elif(encontrouPreto(rgb_dir)):
    #     print("encontrou preto lado direito")
    #     lado = 1
    #     angulo = motor_direita.resetarAnguloMotor()

    seguidor.seguirLinhaPreta(
        cor_vermelha_direta=rgb_dir[0],
        cor_vermelha_esquerda=rgb_esq[0],
        kd=4, 
        kp=3,
        motor_direito=motor_direita,
        motor_esquerdo=motor_esquerda,
        potencia_motores=50
    )
    # wait(300)
        