from lego_imports.lego_imports import LegoImports


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
