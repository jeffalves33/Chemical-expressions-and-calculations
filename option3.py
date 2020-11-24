# -*- coding: utf-8 -*-
import os

# função principal da terceira opção
def option(option):
    answer = 0
    
    # loop responsável para caso os usuários queirem repetir o processo quantas
    # vezes forem necessárias
    while(1):
        print(':::::QUANTIDADE DE UM GÁS PRODUZIDO:::::')
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
            pressao = float(input('Pressao: '))
            volume = float(input('Volume: '))
            temperatura = float(input('Temperatura: '))
            
            ## aqui usa a função auxiliar para retornar uma string (texto)
            ## que é imprimido no final
            # função que RETORNA uma string com o resultado
            resultado = auxOption3(pressao, volume, temperatura)
            print('concentração molar: '  + str(resultado) + '\n')
    
        # informações por arquivo
        if(option == 2):
            ## abre o arquivo para leitura (r) e passa o arquivo aberto
            ## para a variável 'file'
            file = open('entrada.txt', 'r')

            pressao = float(file.readline()) # lê a primeira linha
            volume = float(file.readline()) # lê a segunda linha
            temperatura = float(file.readline()) # lê a terceira linha
            
            # retorna uma string com o resultado
            resultado = auxOption3(pressao, volume, temperatura)
            
            ## responsável por ler todas as linhas o que faz com que o leitor
            ## fique no final do arquivo. assistir vídeo a baixo para entender melhor
            lines = file.readlines() # deixa o leitor no final do arquivo
            
            file.close() # fecha

            lines.insert(4, resultado) # adiciona resultado no final DA STRING.

            ## abre o arquivo para escrita (w) e passa o arquivo aberto
            ## para a variável 'file'
            file = open('saida.txt', 'w')

            file.writelines(lines) # adiciona o resultado no final DO ARQUIVO

            file.close() # fecha arquivo

            print('cheque o arquivo de saida :)')


# função auxiliar da terceira opção
def auxOption3(pressao, volume, temperatura):
    divisor = (0.082 * temperatura)
    expressao = pressao * volume

    num_mols = str(round(expressao/divisor, 4)) # transforma em string com 4 digitos de um float

    return num_mols
