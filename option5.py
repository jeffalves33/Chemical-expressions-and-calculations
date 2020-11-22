# -*- coding: utf-8 -*-
import os


def option5(option):
    answer = 0

    #se for excolhido entrar com dados de usuário
    if(option == 2
    ):
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
            resultado = auxOption5(deltaH, deltaS, temperatura)
            print('Delta G: ' + str(resultado) + '\n')

    #caso for escolhido o uso de arquivo
    else:
        file = open('entrada.txt', 'r')
        deltaH = float(file.readline())
        deltaS = float(file.readline())
        temperatura = float(file.readline())
        resultado = 0
        resultado = auxOption5(deltaH, deltaS, temperatura)
        lines = file.readlines()
        file.close()
        lines.insert(4, resultado)

        file = open('saida.txt', 'w')
        file.writelines(lines)
        file.close()
            
            
            
def auxOption5(deltaH, deltaS, temperatura):
    resultado = str(round(deltaH - (temperatura*deltaS),5))
    return(resultado)

option5(1)