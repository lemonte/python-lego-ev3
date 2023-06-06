from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick
from pybricks.iodevices import LUMPDevice, DCMotor
import math


#!/usr/bin/env pybricks-micropython



class LegoImports:

  """INICIA A CLASSE MOTOR  MOTOR(PORT)  PORTA DO MOTOR """
  def __init__(self):
    print("#### IMPORTANDO CLASSES DO LEGO ####")

  def getMotor(self):
    return Motor
  
  def getPorta(self):
    return Port

  def getStop(self):
    return Stop
  
  def getColorSensor(self):
    return ColorSensor
  
  def getLUMPDevice(self):
    return LUMPDevice
  
  def getUltrasonicSensor(self):
    return UltrasonicSensor

  def getDCMotor(self):
    return DCMotor
  
  def getDirection(self):
    return Direction

  def getDriveBase(self):
    return DriveBase

  def getEv3Brick(self):
    return EV3Brick


class Uteis:
    __importar_lego = LegoImports()

    def definirPorta(self, Port: str):
        porta = None
        if(Port.upper() == "A"):
            porta = self.__importar_lego.getPorta().A
        elif(Port.upper() == "B"):
            porta = self.__importar_lego.getPorta().B
        elif(Port.upper() == "C"):
            porta = self.__importar_lego.getPorta().C
        elif(Port.upper() == "D"):
            porta = self.__importar_lego.getPorta().D
        elif(Port.upper() == "1"):
            porta = self.__importar_lego.getPorta().S1
        elif(Port.upper() == "2"):
            porta = self.__importar_lego.getPorta().S2
        elif(Port.upper() == "3"):
            porta = self.__importar_lego.getPorta().S3
        elif(Port.upper() == "4"):
            porta = self.__importar_lego.getPorta().S4
        return porta


class RoboMotor():

    __importar_lego = LegoImports()
    __velocidade = 200
    def_motor = None

    """INICIA A CLASSE MOTOR  MOTOR("A")  (LETRA)  DA PORTA DO MOTOR """

    def __init__(self, Port: str, velocidade: float):
        if(velocidade != None):
             self.__velocidade = velocidade
        porta = Uteis().definirPorta(Port)
        if(porta == None):
            print("Porta inválida para iniciar o motor")
        else:
            self.def_motor = self.__importar_lego.getMotor()(porta, positive_direction=Direction.COUNTERCLOCKWISE)

    
    def velocidadeAtual(self):
        """ PEGAR A VELOCIDADE ATUAL
            RETORNA O VALOR DA VELOCIDADE: FLOAT 
        """
        return self.__velocidade

    def alterarVelocidade(self, nova_velocidade: float):
        """  ALTERAR VELOCIDADE DO ROBO 
        PARAMETROS:
            nova_velocidade: float 
        """
        self.__velocidade = nova_velocidade

    def moverComPotencia(self, potencia:float):
        """ MOVER MOTOR COM POTENCIA 
        PARAMETROS:
            potencia: float
        """
        self.def_motor.dc(potencia)

    def pararMotor(self):
        """ PARA MOTOR 
        NAO RECEBE PARAMETROS
        """
        self.def_motor.hold()

    
    def moverComVelocidade(self, velocidade= __velocidade):
        """ MOVER MOTOR COM VELOCIDADE 
        PARAMETROS: 
            velocidade: FLOAT
        """
        self.def_motor.run(velocidade)

    def pegarVelocidadeDoMotor(self):
        """ PEGAR VELOCIDADE DO MOTOR 
        NAO RECEBE PARAMETROS
        """
        return self.def_motor.speed()

    def pegarSeOMotorEstaParado(self):
        """ PEGAR SE O MOTOR ESTA PARADO
        NAO RECEBE PARAMETROS
        """
        return self.def_motor.control.stalled()
    
    def pegarAnguloDoMotor(self):
        return self.def_motor.angle()

    def resetarAnguloMotor(self):
        return self.def_motor.reset_angle(0)

    def girarAngulo(self, angulo: float, velocidade=__velocidade, then=__importar_lego.getStop().HOLD, wait=True):
        """ GIRAR MOTOR DETERMINADO ANGULO 
        PARAMETROS:
            angulo: float,
            velocidade: float,
            then: Stop.HOLD (DEFAULT HOLD),
            wait: boolean (default true)
        """
        self.def_motor.run_angle(velocidade, angulo, then=then, wait=wait)




class Robo:
    """INICIA A CLASSE ROBO PASSANDO AS DIMENSOES ROBO(diamentro_robo: float, diamentro_roda: float, motor_direito: RoboMotor, motor_esquerdo: RoboMotor) """
    
    __importar_lego = LegoImports()
    __diametro_robo = 0
    __diametro_roda = 0
    __motor_direito = None
    __motor_esquerdo = None
    __ev3 = __importar_lego.getEv3Brick()()

    def __init__(self, diametro_robo: float, diametro_roda: float, motor_direito: RoboMotor, motor_esquerdo: RoboMotor):
        """Inicia o construturo da classe ROBO
        PARAMETROS:
            diametro_robo: float,
            diametro_roda: float,
            motor_direito: RoboMotor,
            motor_esquerdo: RoboMotor
        """
        self.__diametro_roda = diametro_roda
        self.__diametro_robo = diametro_robo
        self.__motor_direito = motor_direito
        self.__motor_esquerdo = motor_esquerdo

    def distanciaPorGiroRoda(self) -> float:
        """ RETORNA A DISTANCIA PERCORRIDA POR CADA GIRO DA RODA 
        RETORNA: FLOAT
        """
        return self.__diametro_roda * math.pi

    def andarDistancia(self, distancia: float):
        """ ANDAR DISTANCIA EM CM 
        PARAMETROS:
            distancia: float (em CM)
        """
        self.paraMotores()
        """ Distancia deve ser passada em milimetros """
        quantidade_giros = distancia / self.distanciaPorGiroRoda()

        self.__motor_direito.girarAngulo(
            angulo=(quantidade_giros * 360), wait=False)
        self.__motor_esquerdo.girarAngulo(
            angulo=(quantidade_giros * 360))

    def __virar90graus(self, direcao: int):
        """Direcao: 1 para direita, e -1 para esquerda """
        if(direcao != 1 and direcao != -1):
            return
        self.paraMotores()
        if(self.__motor_direito == None or self.__motor_esquerdo == None):
            print("### Impossivel realizar essa acao!! ###")
            print("### Motores nao cadastrados #####")
        else:
            distancia_mover_motor = (self.__diametro_robo * math.pi) / 4
            quantidade_giros = distancia_mover_motor / self.distanciaPorGiroRoda()
            self.__motor_direito.girarAngulo(
                angulo=(direcao * quantidade_giros * -360), wait=False)
            self.__motor_esquerdo.girarAngulo(
                angulo=(direcao * quantidade_giros * 360))

    def virarAngulo(self, angulo: int):
        distancia_mover_motor = (self.__diametro_robo * math.pi) / 4
        quantidade_giros = distancia_mover_motor / self.distanciaPorGiroRoda()
        self.__motor_direito.girarAngulo(
                angulo=(quantidade_giros * -angulo), wait=False)
        self.__motor_esquerdo.girarAngulo(
            angulo=( quantidade_giros * angulo))

    def virar90grausDireita(self):
        """ VIRAR 90 GRAUS PARA DIREITA """
        self.__virar90graus(1)

    def virar90grausEsquerda(self):
        """ VIRAR 90 GRAUS PARA ESQUERDA """
        self.__virar90graus(-1)

    def paraMotores(self):
        """ PARAR MOTORES """
        if(self.__motor_direito == None or self.__motor_esquerdo == None):
            print("### Impossivel realizar essa acao!! ###")
            print("### Motores nao cadastrados #####")
        else:
            self.__motor_direito.pararMotor()
            self.__motor_esquerdo.pararMotor()

    def bipe(self, frequencia=500, duracao=100):
        """ EXECUTAR SOM DE BEEP 
        PARAMETROS OPCIONAIS:
            frequencia: inteiro
            duracao: inteiro
        """
        self.__ev3.speaker.beep(frequency=frequencia, duration=duracao)

    def moverParaFrente(self, velocidade: None):
        """ MOVER O ROBO PARA FRENTE 
        PARAMETROS OBRIGATORIOS:
            velocidade: float
        """
        if(self.__motor_direito == None or self.__motor_esquerdo == None):
            print("### Impossivel realizar essa acao!! ###")
            print("### Motores nao cadastrados #####")
        else:
            self.paraMotores()
            self.__motor_direito.moverComVelocidade(velocidade=velocidade)
            self.__motor_esquerdo.moverComVelocidade(velocidade=velocidade)

    def moverParaTras(self, velocidade:None):
        """ MOVER O ROBO PARA TRAS 
        PARAMETROS OBRIGATORIOS:
            velocidade: float
        """
        if(self.__motor_direito == None or self.__motor_esquerdo == None):
            print("### Impossivel realizar essa acao!! ###")
            print("### Motores nao cadastrados #####")
        else:
            self.paraMotores()
            if(velocidade == None):
                velocidade = 1000
            self.__motor_direito.moverComVelocidade(velocidade=-velocidade)
            self.__motor_esquerdo.moverComVelocidade(velocidade=-velocidade)
        


class RoboUltrassonico:
    """INICIA A CLASSE ROBO Ultrassonico  RoboUltrassonico(1)  (TIPO INTEIRO)  DA PORTA DO SENSOR ULTRASSONICO """
    __importar_lego = LegoImports()
    def_sensor_ultrassonico = None

    def __init__(self, Port: int):
      porta = Uteis().definirPorta(str(Port))
      if(porta == None):
          print("Porta inválida para iniciar o sensor ultrassonico")
      else:
          self.def_sensor_ultrassonico = self.__importar_lego.getLUMPDevice()(porta)


    def distancia_cm(self):
      return self.def_sensor_ultrassonico.read(0)



class RoboCor:
    """INICIA A CLASSE ROBO COR  RoboCOR(1)  (TIPO INTEIRO)  DA PORTA DO SENSOR DE COR """
    __importar_lego = LegoImports()
    def_sensor_cor = None
    __valor_maximo = (163, 156, 162)
    __valor_minimo = (16, 21, 22)

    def __init__(self, Port: int, cor_branco: tuple =(163, 156, 162), cor_preto: tuple = (16, 21, 22)):
      porta = Uteis().definirPorta(str(Port))
      if(porta == None):
          print("Porta inválida para iniciar o sensor de cor")
      else:
          self.def_sensor_cor = self.__importar_lego.getLUMPDevice()(porta)
          self.__valor_maximo = cor_branco
          self.__valor_minimo = cor_preto


    def reflexao(self):
      intensidade = self.def_sensor_cor.read(0)[0]
      return intensidade

    def retornaCor(self):
       return self.def_sensor_cor.read(2)

    def rgb(self):
      return self.def_sensor_cor.read(4)
        

    def rgb_vermelho(self):
      return self.rgb()[0]
    
    def rgb_verde(self):
      return self.rgb()[1]

    def rgb_azul(self):
      return self.rgb()[2]

    def __coeficiente(self):
      max_r,max_g, max_b = self.__valor_maximo
      min_r, min_g, min_b = self.__valor_minimo
      coe_r = (max_r - min_r)/15
      coe_g = (max_g - min_g)/15
      coe_b = (max_b - min_b)/15
      return coe_r, coe_g, coe_b


    def __verificaSeEMenorMinimo(self, valor, valor_min):
        if(valor < valor_min):
            valor = valor_min
        return valor 

    def __verificaSeEMaiorMaximo(self, valor, valor_max):
        if(valor > valor_max):
            valor = valor_max
        return valor


    def __converterRGBde0A15CadaCor(self, cor, valor_max, valor_min, coeficiente):
        cor = self.__verificaSeEMenorMinimo(cor, valor_min)
        cor = self.__verificaSeEMaiorMaximo(cor, valor_max)
        cor = cor - valor_min
        cor = (cor+(coeficiente//2))//coeficiente
        return cor
        

    def converterRGBde0A15(self, rgb: tuple):
        r, g, b =rgb
        max_r,max_g, max_b = self.__valor_maximo
        min_r, min_g, min_b = self.__valor_minimo
        coe_r, coe_g, coe_b = self.__coeficiente()
        r = self.__converterRGBde0A15CadaCor(r, max_r, min_r, coe_r)
        g = self.__converterRGBde0A15CadaCor(g, max_g, min_g, coe_g)
        b = self.__converterRGBde0A15CadaCor(b, max_b, min_b, coe_b)
        return r, g, b




class SeguidorLinha:
    """" INICIA A CLASSE SEGUIDOR DE LINHA ex: SeguidorLinha() 
    (kp) é a constante proporcional.
    (Kd) é a constante derivativa
    """

    __kp = 10
    __kd = 10
    __erro = 0
    __erroAnterior = 0        
    __potencia_maxima = 70

    def __calcularErro(self, leitura_sensor_esquerdo, leitura_sensor_direito):
        return (leitura_sensor_esquerdo - leitura_sensor_direito)

    def __calcularPotencia(self, kp, kd, erro, erroAnterior):
        return ((erro * kp) + kd * (erro - erroAnterior))

    def ___excedenteMotores(self, potenciaCalculada):
        if(abs(potenciaCalculada) < self.__potencia_maxima):
            return 0
        if(potenciaCalculada < 0):
            return (self.__potencia_maxima - potenciaCalculada)
        return (potenciaCalculada - self.__potencia_maxima)

    def seguirLinhaPreta(self, cor_vermelha_esquerda: int, cor_vermelha_direta: int,  motor_direito: RoboMotor, motor_esquerdo: RoboMotor,  kp: int = 1, kd: int = 1, potencia_motores: int = 70):
        self.__kp = kp
        self.__kd = kd

        if(motor_direito == None or motor_esquerdo == None):
            print("#### Verifique se os motores foram passados corretamente #####")
        else:
          if(cor_vermelha_esquerda == None or cor_vermelha_direta == None):
              print("#### Verifique se os rgb(s) de cor foram passados corretamente #####")
          else:
              leitura_sensor_esquerdo = cor_vermelha_esquerda
              leitura_sensor_direito = cor_vermelha_direta
              self.__aux = self.__erro
              self.__erro = self.__calcularErro(
                  leitura_sensor_esquerdo, leitura_sensor_direito)
              self.__erroAnterior = self.__aux

              # calcula a potencia
              potencia = self.__calcularPotencia(
                  self.__kp, self.__kd, self.__erro, self.__erroAnterior)
              
              potencia_esquerdo = potencia_motores + potencia
              potencia_direito = potencia_motores - potencia

            #   print("potencia ", potencia)


              diferenca_d = self.___excedenteMotores(potencia_direito)
              diferenca_e = self.___excedenteMotores(potencia_esquerdo)


            #   print("excedente esquerda ", diferenca_e)
            #   print("excedente direita ", diferenca_d)


              potencia_direito = potencia_direito - diferenca_d
              potencia_esquerdo = potencia_esquerdo  - diferenca_e

              potencia_esquerdo = max(-self.__potencia_maxima, min(potencia_esquerdo, self.__potencia_maxima))
              potencia_direito = max(-self.__potencia_maxima, min(potencia_direito, self.__potencia_maxima))
            #   print("potencia esquerda ", potencia_esquerdo)
            #   print("potencia direita ", potencia_direito)

              # mover motores
              motor_direito.moverComPotencia(potencia_direito)
              motor_esquerdo.moverComPotencia(potencia_esquerdo)