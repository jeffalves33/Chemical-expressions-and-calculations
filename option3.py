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
            resultado = auxOption3(pressao, volume, temperatura)
            print('concentração molar: '  + str(resultado) + '\n')
    
    #caso for escolhido o uso de arquivo
    else:
        file = open('entrada.txt', 'r')
        pressao = float(file.readline())
        volume = float(file.readline())
        temperatura = float(file.readline())
        resultado = auxOption3(pressao, volume, temperatura)
        lines = file.readlines()
        file.close()

        lines.insert(4, resultado)

        file = open('saida.txt', 'w')
        file.writelines(lines)
        file.close()


def auxOption3(pressao, volume, temperatura):
    divisor = (0.082 * temperatura)
    expressao = pressao * volume
    num_mols = str(round(expressao/divisor, 4))
    return num_mols

option3(1)