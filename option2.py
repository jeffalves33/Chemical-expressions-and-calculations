# -*- coding: utf-8 -*-
import os

def option2(option):
    answer = 0

    if(option == 2):
        while(1):
            print(':::::CONCENTRACAO MOLAR:::::')
            print('1 - continuar')
            print('2 - sair')
            answer = int(input('=> '))
            os.system('clear') or None
            if(answer == 2):
                break
            numMols = float(input('Numero de mols(g): '))
            volumeSol = float(input('Volume da solucao(L): '))
            resultado = auxOption2(volumeSol, numMols)
            print('concentracao molar: ' + resultado + 'mol/L' + '\n')

    #caso for escolhido o uso de arquivo
    else:
        file = open('entrada.txt', 'r')
        numMols = float(file.readline())
        volumeSol = float(file.readline())
        resultado = auxOption2(volumeSol, numMols)
        lines = file.readlines()
        file.close()

        lines.insert(4, resultado)

        file = open('saida.txt', 'w')
        file.writelines(lines)
        file.close()

def auxOption2(volumeSol,numMols):
    concentracao = str(round(numMols/volumeSol,4))
    return concentracao

option2(1)