# -*- coding: utf-8 -*-
import os


def option(option):
    answer = 0

    
    while(1):
        print(':::::ENERGIA LIVRE DE GIBBS:::::')
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
            deltaH = float(input('Delta H: '))
            deltaS = float(input('Delta S: '))
            temperatura = float(input('Temperatura: '))

            ## aqui usa a função auxiliar para retornar uma string (texto)
            ## que é imprimido no final
            # função que RETORNA uma string com o resultado
            resultado = auxOption5(deltaH, deltaS, temperatura)
            print('Delta G: ' + str(resultado) + '\n')

        # informação por arquivo
        if(option == 2):
            ## abre o arquivo para leitura (r) e passa o arquivo aberto
            ## para a variável 'file'
            file = open('entrada.txt', 'r')

            deltaH = float(file.readline()) # lê a primeira linha
            deltaS = float(file.readline()) # lê a segunda linha
            temperatura = float(file.readline()) # lê a terceira linha

            # retorna uma string com o resultado
            resultado = auxOption5(deltaH, deltaS, temperatura)

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
            

# função auxiliar da quarta opção
def auxOption5(deltaH, deltaS, temperatura):
    # calcula e transforma em string
    resultado = str(round(deltaH - (temperatura*deltaS),5))

    return(resultado) # retorna resultado

