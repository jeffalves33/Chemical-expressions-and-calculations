# -*- coding: utf-8 -*-
import os


def option4(option):
    answer = 0

    if(option == 1):
        while(1):
            print(':::::TEMPODE DE MEIA-VIDA:::::')
            print('1 - continuar')
            print('2 - sair')
            answer = int(input('=> '))
            os.system('clear') or None
            if(answer == 2):
                break
            valueK = float(input('Informe K: '))
            auxOption4(valueK)

def auxOption4(valueK):
    log2 = 0.69314718
    halfLife = str(round(log2/valueK,8))
    print('tempo de meia-vida: ' + halfLife + '\n')

option4(1)