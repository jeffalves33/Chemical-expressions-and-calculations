# -*- coding: utf-8 -*-
import os

def option3(option):
    answer = 0

    if(option == 1):
        while(1):
            print(':::::QUANTIDADE DE UM GÁS PRODUZIDO:::::')
            print('1 - continuar')
            print('2 - sair')
            answer = int(input('=> '))
            os.system('clear') or None
            if(answer == 2):
                break
            pressao = float(input('Pressao: '))
            volume = float(input('Volume: '))
            temperatura = float(input('Temperatura: '))
            auxOption3(pressao, volume, temperatura)

def auxOption3(pressao, volume, temperatura):
    divisor = (0.082 * temperatura)
    expressao = pressao * volume
    print(divisor)
    print(expressao)
    num_mols = round(expressao/divisor, 4)
    print('concentração molar: '  + str(num_mols) + '\n')

option3(1)