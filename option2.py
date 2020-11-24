# -*- coding: utf-8 -*-
import os

# função principal da segunda opção
def option(option):
    answer = 0

    # loop responsável para caso os usuários queirem repetir o processo quantas
    # vezes forem necessárias
    while(1):
        print(':::::CONCENTRACAO MOLAR:::::')
        print('1 - continuar')
        print('2 - sair')

        answer = int(input('=> ')) ## entrada do usuário: 1 - faz novamente, 2 - volta ao menu anterior

        os.system('clear') or None # limpa a tela

        # caso em que o usuário queira sair (menu anterior)
        if(answer == 2):
            break #quebrar/voltar

        ## aqui verifica se o usuário optou por usar arquivo como entrada (chegar o primeiro menu)
        ## 1 - informações pelo terminal
        ## 2 - informações por arquivo

        # informações pelo terminal (usuário) 
        if(option == 1):
            numMols = float(input('Numero de mols(g): '))
            volumeSol = float(input('Volume da solucao(L): '))

            ## aqui usa a função auxiliar para retornar uma string (texto)
            ## que é imprimido no final
            # função que RETORNA uma string com o resultado
            resultado = auxOption2(volumeSol, numMols)
            print('concentracao molar: ' + resultado + 'mol/L' + '\n')

        # informações por arquivo
        if(option == 2):
            ## abre o arquivo para leitura (r) e passa o arquivo aberto
            ## para a variável 'file'
            file = open('entrada.txt', 'r') # abre arquivo

            numMols = float(file.readline()) # lê a primeira linha
            volumeSol = float(file.readline()) # lê a segunda linha

            # retorna uma string com o resultado
            resultado = auxOption2(volumeSol, numMols)

            ## responsável por ler todas as linhas o que faz com que o leitor
            ## fique no final do arquivo. assistir vídeo a baixo para entender melhor
            lines = file.readlines() # deixa o leitor no final do arquivo
            
            file.close() # fecha o arquivo

            lines.insert(4, resultado) # adiciona resultado no final DA STRING.

            ## abre o arquivo para escrita (w) e passa o arquivo aberto
            ## para a variável 'file'
            file = open('saida.txt', 'w')

            file.writelines(lines) # adiciona o resultado no final DO ARQUIVO

            file.close() # fecha arquivo
        

# função auxiliar da segunda opção
def auxOption2(volumeSol,numMols):
    # calcula e transforma em string
    concentracao = str(round(numMols/volumeSol,4))

    return concentracao #returna resultado
