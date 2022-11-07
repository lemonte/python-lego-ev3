
from compartilhados.uteis import Uteis
from lego_imports.lego_imports import LegoImports

class RoboCor:
    """INICIA A CLASSE ROBO COR  RoboCOR(1)  (TIPO INTEIRO)  DA PORTA DO SENSOR DE COR """
    __importar_lego = LegoImports()
    __color_dict_HSV = {
            'PRETO': [[120, 70, 30], [90, 40, 0]],
            'BRANCO': [[350, 5, 70], [0, 0, 0]],
            # 'VEMELHO1': [[180, 255, 255], [159, 50, 70]],
            # 'VERMELHO2': [[9, 255, 255], [0, 50, 70]],
            'VERDE': [[180, 100, 50], [100, 50, 10]],
            'AZUL': [(210, 100, 70), [150, 50, 40]],
            # 'AMARELO': [[35, 255, 255], [25, 50, 70]],
            # 'ROXO': [[158, 255, 255], [129, 50, 70]],
            # 'LARANJA': [[24, 255, 255], [10, 50, 70]],
            # 'CINZA': [[180, 18, 230], [0, 0, 40]]
        }
    def_sensor_cor = None


    def __init__(self, Port: int):
      porta = Uteis().definirPorta(str(Port))
      if(porta == None):
          print("Porta inválida para iniciar o sensor de cor")
      else:
          self.def_sensor_cor = self.__importar_lego.getLUMPDevice()(porta)


    def reflexao(self):
      intensidade = self.def_sensor_cor.read(0)[0]
      return intensidade

    def rgb(self):
      return self.def_sensor_cor.read(4)
    
    def rgb_vermelho(self):
      return self.rgb()[0]
    
    def rgb_verde(self):
      return self.rgb()[1]

    def rgb_azul(self):
      return self.rgb()[2]

    def verdeEncontrado(self, rgb):
      r, g, b = rgb
      return self.__verificarSeCor("VERDE", r, g, b)
      
    def __verificarSeCor(self, cor: str, r, g, b):
      h, s, v = self.__rgb_para_hsv(r, g, b)
      lista = self.__color_dict_HSV[cor]
      return (self.__cor_encontrada([h,s,v], lista))

    def brancoEncontrado(self, rgb):
      r, g, b = rgb
      return self.__verificarSeCor("BRANCO", r, g, b)

    def rgbParaCor(self, r, g, b):
      h, s, v = self.__rgb_para_hsv(r, g, b)
      self.__distinctColor(h, s, v)

    def __rgb_para_hsv(self, r, g, b):
        r, g, b = r/255.0, g/255.0, b/255.0
        mx = max(r, g, b)
        mn = min(r, g, b)
        df = mx-mn
        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g-b)/df) + 360) % 360
        elif mx == g:
            h = (60 * ((b-r)/df) + 120) % 360
        elif mx == b:
            h = (60 * ((r-g)/df) + 240) % 360
        if mx == 0:
            s = 0
        else:
            s = (df/mx)*100
        v = mx*100
        return h, s, v

    def __cor_encontrada(self, lista_procurada: list, lista: list) -> bool:
        if(
            lista[0][0] >= lista_procurada[0] and
            lista[0][1] >= lista_procurada[1] and
            lista[0][2] >= lista_procurada[2] and
            lista[1][0] <= lista_procurada[0] and
            lista[1][1] <= lista_procurada[1] and
            lista[1][2] <= lista_procurada[2]
        ):
            return True
        return False

    def __distinctColor(self, h, s, v):
        print(h, s, v)
        for key in self.__color_dict_HSV:
            value = self.__color_dict_HSV[key]
            if(self.__cor_encontrada([h, s, v], value)):
                return print(key)
