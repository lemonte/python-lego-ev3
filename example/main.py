#!/usr/bin/env pybricks-micropython

from motores.robo_motor import RoboMotor
from robo.robo import Robo
from sensores.robo_cor import RoboCor
from codigos.codigos_prontos import CodigosProntos
# import time


cor_direita = RoboCor(Port=1, cor_branco=(154, 147, 150), cor_preto=(15, 21, 21))

cor_esquerda = RoboCor(Port=2, cor_branco=(129, 112, 69), cor_preto=(15, 16, 12))


motor_direita = RoboMotor(Port="d")

motor_esquerda = RoboMotor(Port="c")



robo = Robo(
    diametro_robo=125,
    diametro_roda=55,
    motor_direito=motor_direita,
    motor_esquerdo=motor_esquerda,
)


codigos = CodigosProntos()

verde = (0.0, 3.0, 0.0)


def funcaoTeste():
    while True:
        rgb_direito = cor_direita.rgb()
        rgb_esquerdo = cor_esquerda.rgb()
        hsv_dir = cor_direita.converterRGBde0A15(rgb_direito)
        hsv_esq = cor_esquerda.converterRGBde0A15(rgb_esquerdo)
        if(hsv_dir == verde or hsv_esq == verde):
            robo.paraMotores()
            contador = 0
            verde_encontrado_dir = (hsv_dir == verde)
            verde_encontrado_esq = (hsv_esq == verde)
            if(hsv_dir == verde):
                robo.moverParaFrente(velocidade=100)
                while contador < 80 and (hsv_esq != verde):
                    rgb_direito = cor_direita.rgb()
                    rgb_esquerdo = cor_esquerda.rgb()
                    hsv_dir = cor_direita.converterRGBde0A15(rgb_direito)
                    hsv_esq = cor_esquerda.converterRGBde0A15(rgb_esquerdo)
                    contador = contador+1
                robo.paraMotores()
                robo.moverParaTras(velocidade=100)
                contador = 0
                while contador > -100 and (hsv_esq != verde):
                    rgb_direito = cor_direita.rgb()
                    rgb_esquerdo = cor_esquerda.rgb()
                    hsv_dir = cor_direita.converterRGBde0A15(rgb_direito)
                    hsv_esq = cor_esquerda.converterRGBde0A15(rgb_esquerdo)
                    contador = contador-1
                robo.paraMotores()
                verde_encontrado_esq = (hsv_esq == verde)
            else:
                robo.moverParaFrente(velocidade=100)
                while contador < 80 and (hsv_dir != verde):
                    rgb_direito = cor_direita.rgb()
                    rgb_esquerdo = cor_esquerda.rgb()
                    hsv_dir = cor_direita.converterRGBde0A15(rgb_direito)
                    hsv_esq = cor_esquerda.converterRGBde0A15(rgb_esquerdo)
                    contador = contador+1
                robo.paraMotores()
                robo.moverParaTras(velocidade=100)
                contador = 0
                while contador > -100 and (hsv_dir != verde):
                    rgb_direito = cor_direita.rgb()
                    rgb_esquerdo = cor_esquerda.rgb()
                    hsv_dir = cor_direita.converterRGBde0A15(rgb_direito)
                    hsv_esq = cor_esquerda.converterRGBde0A15(rgb_esquerdo)
                    contador = contador-1
                robo.paraMotores()
                verde_encontrado_dir = (hsv_dir == verde)
            

            robo.paraMotores()
            if(verde_encontrado_dir and verde_encontrado_esq):
                robo.virar90grausDireita()
                robo.virar90grausDireita()
            elif(verde_encontrado_dir):
                robo.virar90grausDireita()
            else:
                robo.virar90grausEsquerda()
            robo.bipe()
            break
        codigos.seguidorDeLinhaPreta(
                    motor_direito=motor_direita,
                    motor_esquerdo=motor_esquerda,
                    kd=80,
                    kp=12,
                    rgb_cor_esquerdo=rgb_esquerdo,
                    rgb_cor_direito=rgb_direito,
                    potencia_motores=70,
                )


funcaoTeste()
