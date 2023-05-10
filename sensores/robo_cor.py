
from compartilhados.uteis import Uteis
from lego_imports.lego_imports import LegoImports

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
