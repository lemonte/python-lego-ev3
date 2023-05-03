from sensores.robo_cor import RoboCor
from motores.robo_motor import RoboMotor
from robo.robo import Robo


class SeguidorLinha:
    """" INICIA A CLASSE SEGUIDOR DE LINHA ex: SeguidorLinha() 
    (kp) é a constante proporcional.
    (Kd) é a constante derivativa
    """

    __kp = 10
    __kd = 10
    __motor_direito = None
    __motor_esquerdo = None
    __potencia_motores = 70
    __erro = 0
    __erroAnterior = 0

    def __calcularErro(self, leitura_sensor_esquerdo, leitura_sensor_direito):
        return (leitura_sensor_esquerdo[0] - leitura_sensor_direito[0])

    def __calcularPotencia(self, kp, kd, erro, erroAnterior):
        return ((erro * kp) + kd * (erro - erroAnterior))/10

    def seguirLinhaPreta(self, rgb_cor_esquerdo: tuple, rgb_cor_direito: tuple,  motor_direito: RoboMotor, motor_esquerdo: RoboMotor,  kp: int = 1, kd: int = 1, potencia_motores: int = 70):
        self.__kp = kp
        self.__kd = kd
        self.__motor_direito = motor_direito
        self.__motor_esquerdo = motor_esquerdo
        self.__potencia_motores = potencia_motores
        if(motor_direito == None or motor_esquerdo == None):
            print("#### Verifique se os motores foram passados corretamente #####")
        else:
          if(rgb_cor_esquerdo == None or rgb_cor_direito == None):
              print("#### Verifique se os rgb(s) de cor foram passados corretamente #####")
          else:
              leitura_sensor_esquerdo = rgb_cor_esquerdo
              leitura_sensor_direito = rgb_cor_direito
              self.__aux = self.__erro
              self.__erro = self.__calcularErro(
                  leitura_sensor_esquerdo, leitura_sensor_direito)
              self.__erroAnterior = self.__aux

              # calcula a potencia
              potencia = self.__calcularPotencia(
                  self.__kp, self.__kd, self.__erro, self.__erroAnterior)

              diferenca_potencia_maxima_e_erro = 0
              valor_maximo = self.__potencia_motores + abs(potencia)
              valor_minimo = self.__potencia_motores  -  abs(potencia)
              potencia_maxima_permitida = self.__potencia_motores
              if(valor_maximo > potencia_maxima_permitida):
                  diferenca_potencia_maxima_e_erro = valor_maximo - potencia_maxima_permitida
              if(valor_minimo < -potencia_maxima_permitida):
                  diferenca_potencia_maxima_e_erro = valor_minimo + potencia_maxima_permitida
              
              diferencaD = 0
              diferencaE = 0
              if(diferenca_potencia_maxima_e_erro < 0):
                  diferencaE = diferenca_potencia_maxima_e_erro
              else:
                  diferencaD = diferenca_potencia_maxima_e_erro
                  
              mover_potencia_motor_direito = self.__potencia_motores - \
                  (potencia) - diferencaE
              mover_potencia_motor_esquerdo = self.__potencia_motores + \
                  (potencia + diferencaD)

              # mover motores
              self.__motor_direito.moverComPotencia(
                  mover_potencia_motor_direito)
              self.__motor_esquerdo.moverComPotencia(
                  mover_potencia_motor_esquerdo)
