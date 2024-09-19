def calc_2(numero):
    contador = 1
    while contador <= 10:
        print(f'2 X {contador} = {numero*contador}')
        contador += 1

def calc_3(numero):
    contador = 1
    while(contador <= 10):
        print(f'3 X {contador} = {numero*contador}')
        contador += 1

def calc_4(numero):
    contador = 1
    while(contador <= 10):
        print(f'4 X {contador} = {numero*contador}')
        contador += 1

def calc_5(numero):
    contador = 1
    while(contador <= 10):
        print(f'5 X {contador} = {numero*contador}')
        contador += 1

def calc_6(numero):
    contador = 1
    while(contador <= 10):
        print(f'6 X {contador} = {numero*contador}')
        contador += 1

def calc_7(numero):
    contador = 1
    while(contador <= 10):
        print(f'7 X {contador} = {numero*contador}')
        contador += 1

def calc_8(numero):
    contador = 1
    while(contador <= 10):
        print(f'8 X {contador} = {numero*contador}')
        contador += 1

def calc_9(numero):
    contador = 1
    while(contador <= 10):
        print(f'9 X {contador} = {numero*contador}')
        contador += 1

def calc_10(numero):
    contador = 1
    while(contador <= 10):
        print(f'10 X {contador} = {numero*contador}')
        contador += 1


numero = int(input("Informe "))

if numero == 2:
    receive = calc_2(numero)
elif numero == 3:
    receive = calc_3(numero)
elif numero == 4:
    receive = calc_4(numero)
elif numero == 5:
    receive = calc_5(numero)
elif numero == 6:
    receive = calc_6(numero)
elif numero == 7:
    receive = calc_7(numero)
elif numero == 8:
    receive = calc_8(numero)
elif numero == 9:
    receive = calc_9(numero)
elif numero == 10:
    receive = calc_10(numero)
else:
    print("Opção Inválida")

# projeto novo: o que fazer? colocar 2 arquivos para essa tabuada, o front end vai ficar com o que o usuario vai ver e o back end vai fornecer o resultado. as funçoes que esta 
# na parte 2 do projeto, fica nessa parte e as condicionais, tenho que remove-las para a parte do front end -- é a ideia em mente.