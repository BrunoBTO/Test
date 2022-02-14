'''
codigo para lancamento de dado com possibolidade de repeticao
com uso do comando import random para a geracao de numeros pseudoaleatorios
'''

# -*- coding: UTF-8 -*-

import random

print('Olá\nSeja bem vindo ao Simulador de dado feito por @BrunoBTO\n')
print('Qual o maior número do dado desejado? Responda com um numero de 1 a 100')

Dsize= int(input()) + 1
play = 's'

while play=='sim' or play=='s':
    result = random.randint(1,Dsize)
    print('O seu dado caiu no número:' + str(result))
    print('Gostaria de lançar o dado novamente? (S/N)')
    play=input().lower()
