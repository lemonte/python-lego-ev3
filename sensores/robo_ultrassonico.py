from compartilhados.uteis import Uteis
from lego_imports.lego_imports import LegoImports
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