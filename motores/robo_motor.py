from lego_imports.lego_imports import LegoImports
from compartilhados.uteis import Uteis

class RoboMotor():

    __importar_lego = LegoImports()
    __velocidade = 200
    def_motor = None

    """INICIA A CLASSE MOTOR  MOTOR("A")  (LETRA)  DA PORTA DO MOTOR """

    def __init__(self, Port: str):
        porta = Uteis().definirPorta(Port)
        if(porta == None):
            print("Porta inválida para iniciar o motor")
        else:
            self.def_motor = self.__importar_lego.getMotor()(porta)

    
    def velocidadeAtual(self):
        return self.__velocidade

    def alterarVelocidade(self, nova_velocidade: float):
        self.__velocidade = nova_velocidade

    def moverComPotencia(self, potencia:float):
        """ MOVER MOTOR COM POTENCIA """
        self.def_motor.dc(potencia)

    def pararMotor(self):
        """ PARA MOTOR """
        self.def_motor.hold()

    
    def moverComVelocidade(self, velocidade= __velocidade):
        """ MOVER MOTOR COM VELOCIDADE """
        self.def_motor.run(velocidade)

    def girarAngulo(self, angulo: float, velocidade=__velocidade, then=None, wait=True):
        """ GIRAR MOTOR DETERMINADO ANGULO """
        if(then == None):
            then = self.__importar_lego.getStop().HOLD
        self.def_motor.run_angle(velocidade, angulo, then=then, wait=wait)
