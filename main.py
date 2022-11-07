#!/usr/bin/env pybricks-micropython

from motores.robo_motor import RoboMotor
from robo.robo import Robo
from sensores.robo_cor import RoboCor
from codigos.codigos_prontos import CodigosProntos
from compartilhados.uteis import Uteis

cor_direita = RoboCor(Port=1)
cor_esquerda = RoboCor(Port=2)
funcoes_uteis = Uteis()
motor_direita = RoboMotor(Port="d")
motor_esquerda = RoboMotor(Port="c")

robo = Robo(
    diametro_robo=125,
    diametro_roda=55,
    motor_direito=motor_direita,
    motor_esquerdo=motor_esquerda
)


codigos = CodigosProntos()


def ultimoLadoLinhaPreta(
    cor_vermelha_direita: float,
    cor_vermelha_esquerda: float
) -> int:
    if(cor_vermelha_esquerda < 15 or cor_vermelha_direita < 15):
        if(cor_vermelha_direita < 15):
            ultimo_lado = 1
        else:
            ultimo_lado = -1
    else:
        ultimo_lado = 0
    return ultimo_lado


def fimDaLinha(
    cor_vermelha_direita: float,
    cor_vermelha_esquerda: float,
    ultimo_lado_preto: int
) -> None:
    if(
        cor_vermelha_direita < 140
        and cor_vermelha_esquerda < 140
        and (ultimo_lado_preto == 1 or ultimo_lado_preto == -1)
    ):
        robo.andarDistancia(20)
        if(ultimo_lado_preto == 1):
            robo.virar90grausDireita()
        else:
            robo.virar90grausEsquerda()


def main() -> None:
    ultimo_lado_preto = 0
    while True:
        rgb_direito = cor_direita.rgb()
        rgb_esquerdo = cor_esquerda.rgb()
        # if(cor_direita.verdeEncontrado(rgb_direito) or cor_esquerda.verdeEncontrado(rgb_esquerdo)):
        #     # robo.paraMotores()
        #     print("achou verde")
        #     # robo.bipe()
        #     # break
        # if(cor_esquerda.brancoEncontrado(rgb_esquerdo) and cor_direita.brancoEncontrado(rgb_direito)):
        #     # robo.paraMotores()
        #     print("achou branco")
            # robo.bipe()
            # break
        # ultimo_lado_preto = ultimoLadoLinhaPreta(
        #     cor_vermelha_direita=rgb_direito[0],
        #     cor_vermelha_esquerda=rgb_esquerdo[0]
        # )

        fimDaLinha(
            cor_vermelha_direita=rgb_direito[0],
            cor_vermelha_esquerda=rgb_esquerdo[0],
            ultimo_lado_preto=ultimo_lado_preto
        )

        codigos.seguidorDeLinhaPreta(
            motor_direito=motor_direita,
            motor_esquerdo=motor_esquerda,
            kd=70,
            kp=13,
            rgb_cor_esquerdo=rgb_esquerdo,
            rgb_cor_direito=rgb_direito,
            potencia_motores=50
        )


main()

# def encontrarCor():
#     rgb_direito = cor_direita.rgb()
#     cor_direita.rgbParaCor(r=rgb_direito[0], g=rgb_direito[1], b=rgb_direito[2])
# while True:
#     encontrarCor()