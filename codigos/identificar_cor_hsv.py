

valor_maximo = (163, 156, 162)
valor_minimo = (16, 21, 22)
def coeficiente():
    max_r,max_g, max_b = valor_maximo
    min_r, min_g, min_b = valor_minimo
    coe_r = (max_r - min_r)/15
    coe_g = (max_g - min_g)/15
    coe_b = (max_b - min_b)/15
    return coe_r, coe_g, coe_b


def verificaSeEMenorMinimo(valor, valor_min):
    if(valor < valor_min):
        valor = valor_min
    return valor 

def verificaSeEMaiorMaximo(valor, valor_max):
    if(valor > valor_max):
        valor = valor_max
    return valor


def converterRGBde0A15CadaCor(cor, valor_max, valor_min, coeficiente):
    cor = verificaSeEMenorMinimo(cor, valor_min)
    cor = verificaSeEMaiorMaximo(cor, valor_max)
    cor = cor - valor_min
    cor = (cor+(coeficiente//2))//coeficiente
    return cor
    

def converterRGBde0A15(rgb: tuple):
    r, g, b =rgb
    max_r,max_g, max_b = valor_maximo
    min_r, min_g, min_b = valor_minimo
    coe_r, coe_g, coe_b = coeficiente()
    r = converterRGBde0A15CadaCor(r, max_r, min_r, coe_r)
    g = converterRGBde0A15CadaCor(g, max_g, min_g, coe_g)
    b = converterRGBde0A15CadaCor(b, max_b, min_b, coe_b)
    return r, g, b

def lerhsv(rgb: tuple):
    return converterRGBde0A15(rgb)