from calculadora import *
import pytest

def test_somar_valores_10_e_20():
    assert somar(10, 20) == 35
    
def test_cumprimentar_aluno_com_boas_vindas():
    assert dar_boas_vindas_ao_aluno("Alexandre") \
        == "Olá, Alexandre!"
        
def test_divir_valor_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)