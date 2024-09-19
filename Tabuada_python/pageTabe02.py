def calc_2(numero):
    contador = 1
    while contador <= 10:
        print(f'2 X {contador} = {numero*contador}')
        contador += 1

def calc_3(numero):
    contador = 3
    while(contador <= 10):
        print(f'3 X {contador} = {numero*contador}')
        contador += 1



numero = int(input("Informe "))
print(calc_2(numero))