
from motores.robo_motor import RoboMotor
from lego_imports.lego_imports import LegoImports
import math


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
        