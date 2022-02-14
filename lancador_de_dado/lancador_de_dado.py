# -*- coding: UTF-8 -*-

"""
Código para lançamento de dado com possibilidade de repetiçao

Uso da biblioteca random para a geração de números pseudoaleatórios
"""

import random

print('Olá\nSeja bem vindo ao Simulador de dado feito por @BrunoBTO\n')
print('Qual o maior número do dado desejado? Responda com um numero de 1 a 100')

Dsize = int(input())
play = 's'

while play == 'sim' or play == 's':
    result = random.randint(1, Dsize)
    print('O seu dado caiu no número:' + str(result))
    print('Gostaria de lançar o dado novamente? (S/N)')
    play = input().lower()
