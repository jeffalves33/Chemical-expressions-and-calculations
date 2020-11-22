# -*- coding: utf-8 -*-
import os


def option4(option):
    answer = 0

    if(option == 2):
        while(1):
            print(':::::TEMPODE DE MEIA-VIDA:::::')
            print('1 - continuar')
            print('2 - sair')
            answer = int(input('=> '))
            os.system('clear') or None
            if(answer == 2):
                break
            valueK = float(input('Informe K: '))
            resultado = auxOption4(valueK)
            print('tempo de meia-vida: ' + str(resultado) + '\n')

    #caso for escolhido o uso de arquivo
    else:
        file = open('entrada.txt', 'r')
        valueK = float(file.readline())
        resultado = auxOption4(valueK)
        lines = file.readlines()
        file.close()

        lines.insert(4, resultado)

        file = open('saida.txt', 'w')
        file.writelines(lines)
        file.close()

def auxOption4(valueK):
    log2 = 0.69314718
    halfLife = str(round(log2/valueK,8))
    return halfLife

option4(1)