import subprocess
from matematica import *

while (continuar.lower() == 's'):
    subprocess.run('cls', shell=True)
    
    print(f'Programa calculadora em Python')

    continuar = input("Deseja fazer um cálculo? [S/N]")
    
    if (continuar.upper() != 'S'):
        break

    print(f'Informe os dois valores a serem calculados')
    
    valorA = float(input("Valor 1: "))
    valorB = float(input("Valor 2: "))

    print('Escolha a operação')
    print(f'1 - Somar')
    print(f'2 - Subtrair')
    print(f'3 - Multiplicar')
    print(f'4 - Dividir')

    operacao = input("Digite a operação: ")
    resultado = None # Valor nulo

    if operacao == '1' or operacao == 'Somar':
        resultado = somar(valorA, valorB)
    elif operacao == '2' or operacao == 'Subtrair':
        resultado = subtrair(valorA, valorB)
    elif operacao == '3' or operacao == 'Multiplicar':
        resultado = multiplicar(valorA, valorB)
    elif operacao == '4' or operacao == 'Dividir':
        resultado = dividir(valorA, valorB)
        
    print(f'O resultado é {resultado:.2f}')
    
    input()