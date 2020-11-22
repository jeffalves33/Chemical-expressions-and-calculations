# -*- coding: utf-8 -*-
##a linha acima elimina alguns erros de type, etc
import os #para limpar a tela deixando o terminal menos poluído
def main():
    answer = 0
    while(1):
        print('1 - pelo usuario')
        print('2 - por arquivo')
        print('3 - sair')
        answer = int(input('=> '))
        os.system('clear') or None
        if(answer == 1):
            main2(1)
        if(answer == 2):
            main2(2)
        if(answer == 3):
            exit()


def main2(option):
    answer = 0
    while(1):
        print(':::::MENU:::::')
        print('1 - Determinacao do numero de atomos de cada elemento de uma formula a partir donumero de mols')
        print('2 - Calculo concentracao molar de uma solucao')
        print('3 - Calculo da quantidade de um gas produzido')
        print('4 - Calculo do tempo de meia vida para uma reacao com cinetica de primeira ordem')
        print('5 - Calculo da energia livre de Gibbs')
        print('6 - menu anterior')
        print('7 - sair')
        answer = int(input('=> '))
        os.system('clear') or None
        if(answer == 1):
            #option1(option)
            continue
        if(answer == 2):
            #option2(option)
            continue
        if(answer == 3):
            option3(option)
            continue
        if(answer == 4):
            #option4(option)
            continue
        if(answer == 5):
            #option5(option)
            continue
        if(answer == 6):
            #main()
            break
        if(answer == 7):
            exit()




    
    






def archive():
    with open('abc.txt', 'r') as f:
        primeira_linha = f.readline()
        
    a = int(primeira_linha)
    print(a)






main()

#teste