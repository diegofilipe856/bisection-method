from math import *
from numpy import *


def funcao(x):
    fx = funcaozera.replace('x', str(x))
    fx = eval(funcaozera)
    return fx


def analise_A_e_B(fx):
    if fx >= 0:
        fx0 = fx
    else:
        fx0 = fx * (-1)
    return fx0


def calculobisec(fx, fx0, a, b, x, erro):
    soma = 0
    while b - a > erro:
        if funcao(a) * funcao(x) < 0:
            b = x
        else:
            a = x
        x = (a + b) / 2
        fx0 = analise_A_e_B(fx)
        soma += 1
        if funcao(a) == 0:
            break
    print(x)
    print(f'Foram necessárias {soma} interações.')


a = float(input('Set the init of the range (a): '))
b = float(input('Set the end o the range (b): '))
erro = float(input('What is the maximum error? '))
x = (a+b)/2
print("Function input example: (x**2)+3*x+2")
fx = input('Insert the function: ')
funcaozera = fx
fx = fx.replace('x', str(x))
fx = eval(fx)

fx0 = analise_A_e_B(fx)

calculobisec(fx, fx0, a, b, x, erro)
print(f'(Isso considerando um erro menor ou igual a {erro}. )')