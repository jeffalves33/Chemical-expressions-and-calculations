# -*- coding: utf-8 -*-
import os

def option2(option):
    answer = 0

    if(option == 1):
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
            auxOption2(volumeSol, numMols)

def auxOption2(volumeSol,numMols):
    concentracao = str(round(numMols/volumeSol,4))
    print('concentracao molar: ' + concentracao + 'mol/L' + '\n')

option2(1)