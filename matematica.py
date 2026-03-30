def somar(valor1, valor2):
    return valor1 + valor2

def subtrair(valor1, valor2):
    return valor1 - valor2

def multiplicar(valor1, valor2):
    return valor1 * valor2

def dividir(valor1, valor2):
    if valor2 != 0:
        return valor1 / valor2 #retorna inteiro
    else:
        print('Impossível divisão por zero')