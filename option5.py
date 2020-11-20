# -*- coding: utf-8 -*-
import os


def option5(option):
    answer = 0

    if(option == 1):
        while(1):
            print(':::::ENERGIA LIVRE DE GIBBS:::::')
            print('1 - continuar')
            print('2 - sair')
            answer = int(input('=> '))
            os.system('clear') or None
            if(answer == 2):
                break
            deltaH = float(input('Delta H: '))
            deltaS = float(input('Delta S: '))
            temperatura = float(input('Temperatura: '))
            auxOption5(deltaH, deltaS, temperatura)

def auxOption5(deltaH, deltaS, temperatura):
    
    deltaG = str(round(deltaH - (temperatura*deltaS),5))
    print('Delta G: ' + deltaG + '\n')

option5(1)