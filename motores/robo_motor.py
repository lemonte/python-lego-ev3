from lego_imports.lego_imports import LegoImports
from compartilhados.uteis import Uteis

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
            self.def_motor = self.__importar_lego.getMotor()(porta)

    
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

    def girarAngulo(self, angulo: float, velocidade=__velocidade, then=__importar_lego.getStop().HOLD, wait=True):
        """ GIRAR MOTOR DETERMINADO ANGULO 
        PARAMETROS:
            angulo: float,
            velocidade: float,
            then: Stop.HOLD (DEFAULT HOLD),
            wait: boolean (default true)
        """
        self.def_motor.run_angle(velocidade, angulo, then=then, wait=wait)
