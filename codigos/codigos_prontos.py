from codigos.seguidor_linha import SeguidorLinha
from motores.robo_motor import RoboMotor


class CodigosProntos:
    __seguidorLinha =  SeguidorLinha()

    def seguidorDeLinhaPreta(
        self,
        motor_direito: RoboMotor,
        motor_esquerdo: RoboMotor,
        kd: int ,
        kp: int,
        rgb_cor_esquerdo: tuple,
        rgb_cor_direito: tuple,
        potencia_motores: int,
    ):
        """ Codigo seguidor de linha preta 
      CodigosProntos(
          motor_direito: RoboMotor,
          motor_esquerdo: RoboMotor,
          kd: int,
          kp: int,
          rgb_cor_esquerdo: tuple,
          rgb_cor_direito: tuple,
          potencia_motores: int

      ) """
        self.__seguidorLinha.seguirLinhaPreta(
            rgb_cor_direito=rgb_cor_direito,
            rgb_cor_esquerdo=rgb_cor_esquerdo,
            kd=kd,
            kp=kp,
            motor_direito=motor_direito,
            motor_esquerdo=motor_esquerdo,
            potencia_motores=potencia_motores
        )
