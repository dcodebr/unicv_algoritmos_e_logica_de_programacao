from calculadora import *

def test_somar_valores_10_e_12():
    assert somar(10, 20) ==30
    
def test_subtrair_valor_negativos():
    assert subtrair(-1, -1) == 0