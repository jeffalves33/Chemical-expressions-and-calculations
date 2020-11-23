# -*- coding: utf-8 -*-
import os

def option1(option):
    answer = 0

    if(option == 1):
        while(1):
            print(':::::NUMERO DE ATOMOS:::::')
            print('1 - continuar')
            print('2 - sair')
            answer = int(input('=> '))
            os.system('clear') or None
            if(answer == 2):
                break
            formula = str(input('Formula: '))
            numMols = int(input('Numero de mols: '))
            print('\n')
            resultado = auxOption1(formula, numMols, option)
            print(resultado + '\n')
    
    #caso for escolhido o uso de arquivo
    else:
        file = open('entrada.txt', 'r')
        formula = str(file.readline())
        numMols = int(file.readline())
        resultado = auxOption1(formula, numMols, option)
        lines = file.readlines()
        file.close()

        lines.insert(4, resultado)

        file = open('saida.txt', 'w')
        file.writelines(lines)
        file.close()

def auxOption1(formula, numMols, option):
    vetResult = []
    stringResult = (str(numMols) + ' mols de ' + formula + ' tem: ')
    stringResult_file = str(formula)
    
    #em python2('xrange'). em python3('range')
    for i in range(len(formula)):
            #se for elemento de 1 letra
            if(formula[i].isupper()):
                #se for elemento de 2 letras
                if(not(i+1 >= len(formula))):
                    if(formula[i + 1].islower()):
                        vetResult.append(formula[i]+formula[i+1])
                        i =+ 1
                        continue 
                vetResult.append(formula[i])
            
            #se for 1 número (consideramos no máx 3 digitos)
            if(formula[i].isdigit()):
                #sequencia de 2 números
                if(not(i+1 >= len(formula))): 
                    if(formula[i+1].isdigit()):
                    #sequência de 3 números
                        if(not(i+2 >= len(formula))):
                            if(formula[i+2].isdigit()):
                                vetResult.append(formula[i]+formula[i+1]+formula[i+2])
                                i =+ 2
                                continue
                        vetResult.append(formula[i]+formula[i+1])
                        i =+ 1
                        continue
                vetResult.append(formula[i])

    i = 0
    a = len(vetResult)

    #colocar condição p saber se precisa entrar aqui
    while(i < a):
        if(vetResult[i].isdigit()):
            x = (str(numMols * int(vetResult[i])))
            stringResult_file += ('\n' + vetResult[i - 1] + ': ' + (str((6.022*numMols) * int(vetResult[i]))) +
                                 '10^23')
            stringResult += ('\n' + x + ' mols de atomos de ' + vetResult[i - 1] + ' (' + x + 
                            'x6.022x10^23 = ' + (str((6.022*numMols) * int(vetResult[i]))) + 
                            '10^23)')
        
        #caso não tiver o 1. ou seja, for apenas 1 mol (só houver a letra no final)
        if((vetResult[i].isalpha()) and (i+1 == a) or ((vetResult[i].isalpha()) and (vetResult[i+1].isalpha()))):
            stringResult_file += ('\n' + vetResult[i] + ': ' + (str((6.022*numMols) * int(1))) + '10^23)')
            stringResult += ('\n' + '1 mol de atomo de ' + vetResult[i] + ' (' + str(numMols) +
                            'x6.022x10^23 = ' + (str((6.022*numMols) * int(1))) + '10^23)')
        i += 1
    
    if(option == 1):
        return stringResult
    if(option == 2):
        return stringResult_file

option1(1)