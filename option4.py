# -*- coding: utf-8 -*-
import os

# função principal da quarta opção
def option(option):
    answer = 0

    # loop responsável para caso os usuários queirem repetir o processo quantas
    # vezes forem necessárias
    while(1):
        print(':::::TEMPODE DE MEIA-VIDA:::::')
        print('1 - continuar')
        print('2 - sair')

        answer = int(input('=> ')) ## entrada do usuário: 1 - faz novamente, 2 - volta ao menu anterior

        os.system('clear') or None # limpa a tela

        # caso em que o usuário queira sair (menu anterior)
        if(answer == 2):
            break #quebrar/voltar

        # aqui verifica se o usuário optou por usar arquivo como entrada (chegar o primeiro menu)
        # 1 - informações pelo terminal
        # 2 - informações por arquivo

        # informações pelo terminal (usuário)
        if(option == 1):
            valueK = float(input('Informe K: '))

            ## aqui usa a função auxiliar para retornar uma string (texto)
            ## que é imprimido no final
            # função que RETORNA uma string com o resultado
            resultado = auxOption4(valueK)
            print('tempo de meia-vida: ' + str(resultado) + '\n')

        # informação por arquivo
        if(option == 2):
            ## abre o arquivo para leitura (r) e passa o arquivo aberto
            ## para a variável 'file'
            file = open('entrada.txt', 'r')

            valueK = float(file.readline()) # lê a primeira linha
            
            # retorna uma string com o resultado
            resultado = auxOption4(valueK)

            ## responsável por ler todas as linhas o que faz com que o leitor
            ## fique no final do arquivo. assistir vídeo a baixo para entender melhor
            lines = file.readlines()

            file.close() # fecha

            lines.insert(4, resultado) # adiciona resultado no final DA STRING.

            ## abre o arquivo para escrita (w) e passa o arquivo aberto
            ## para a variável 'file'
            file = open('saida.txt', 'w')

            file.writelines(lines) # adiciona o resultado no final DO ARQUIVO

            file.close() # fecha
            print('cheque o arquivo de saida :)')
            

# função auxiliar da terceira opção
def auxOption4(valueK):
    log2 = 0.69314718

    halfLife = str(round(log2/valueK,8)) # calcula e transforma em string
    
    return halfLife

