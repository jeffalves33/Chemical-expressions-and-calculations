# -*- coding: utf-8 -*-
import os

# função principal da primeira opção
def option(opcao_inicial):
    answer = 0

    # loop responsável para caso os usuários queirem repetir o processo quantas
    # vezes forem necessárias
    while(1):
        print(':::::NUMERO DE ATOMOS:::::')
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
        if(opcao_inicial == 1):
            formula = str(input('Formula: '))
            numMols = int(input('Numero de mols: '))

            print('\n')
            ## aqui usa a função auxiliar para retornar uma string (texto)
            ## que é imprimido no final
            # função que RETORNA uma string com o resultado
            resultado = auxOption1(formula, numMols, opcao_inicial)
            print(resultado + '\n')

        # informações por arquivo
        if(opcao_inicial == 2):
    
            ## abre o arquivo para leitura (r) e passa o arquivo aberto
            ## para a variável 'file'
            file = open('entrada.txt', 'r') # abre arquivo

            formula = str(file.readline()) # lê a primeira linha
            numMols = int(file.readline()) # lê a segunda linha

            # retorna uma string com o resultado
            resultado = auxOption1(formula, numMols, opcao_inicial)

            ## responsável por ler todas as linhas o que faz com que o leitor
            ## fique no final do arquivo. assistir vídeo a baixo para entender melhor
            ## https://www.youtube.com/watch?v=UCOJWSnKCT0&t=993s&ab_channel=Ot%C3%A1vioMiranda
            lines = file.readlines() # deixa o leitor no final do arquivo
            
            file.close() # fecha o arquivo

            ## como o leitor está no final do arquivo, aqui usamos a função 'insert'
            ## de arquivos para que o resultado, seja adicionado no FINAL já que o leitor
            ## já se encontra no final, seguindo a linha ''lines = file.readlines()'
            ## o primeiro argumento('4') significa q vai ser adicionado na linha 4
            lines.insert(4, resultado) # adiciona resultado no final DA STRING.

            ## abre o arquivo para escrita (w) e passa o arquivo aberto
            ## para a variável 'file'
            file = open('saida.txt', 'w')

            file.writelines(lines) # adiciona o resultado no final DO ARQUIVO

            file.close() # fecha arquivo

# função auxiliar da primeira opção
def auxOption1(formula, numMols, opcao_inicial):
    vetResult = [] ## usada para separar cada elemento = ['H','2','O']
    stringResult = (str(numMols) + ' mols de ' + formula + ' tem: ')
    stringResult_file = str(formula)
    
    ## laço 'for' responsável por avaliar cada forma de inserção da formula:
    ## caso em que tenha 1 letra = H2O
    ## caso em que tenha 2 letras = H2O2Nm
    ## se for um número com 2 ou mais dígitos = H33O2Nm

    # em python2('xrange'). em python3('range')
    # pega o tamanho da string 
    for i in range(len(formula)):
            # usamos no máximo uma sequencia de 3 numeros (ex.:H200O100)

            # caso em que tenha 1 letra (ex.: H2O)
            if(formula[i].isupper()): # verifica se a letra é maiúscula

                ## se entrar aqui é pq a letra é maiúscula, então vai verificar
                ## se a próxima é uma letra minuscula, sendo um elemento de 2 letras
                # caso em que tenha 2 letras (ex.: H2ONm)
                if(not(i+1 >= len(formula))):

                    if(formula[i + 1].islower()): # verifica se a letra é maiúscula
                        
                        ## adiciona esse elemento de 2 letras no final de um vetor de string
                        # adiciona o elemento de 2 letras no final da string do tipo:
                        # ['H','2','O','N','m']
                        vetResult.append(formula[i]+formula[i+1])
                        i =+ 1
                        continue

                ## apenas adiciona o elemento de 1 letras no final da string
                # caso seja elemento apenas de 1 letras e n entre na condição anterior
                vetResult.append(formula[i])
            
            # caso a letra seja seguida por 1 numero (ex.: H2O)
            if(formula[i].isdigit()): # verifica se o elemento atual é um numero (digito)
                
                # caso a letra seja seguida por 2 numero
                ## verifica se o numero é o ultimo da string ou tem algo após ele
                if(not(i+1 >= len(formula))): # verifica se i+1 é do tamanho da string
                    
                    # só entra aqui se existir mais elementos após o atual.
                    if(formula[i+1].isdigit()): # verifica se o próximo é um numero
                    
                        # caso a letra seja seguida por 3 numero
                        if(not(i+2 >= len(formula))): # verifica se i+1 é do tamanho da string
                            
                            # só entra aqui se existir mais elementos após o elemento (i + 1), ou seja, 3 digitos
                            if(formula[i+2].isdigit()):
                                # adiciona os 3 dígitos juntos ao final (ex.: H222O111 = ['H', '222', ...])
                                vetResult.append(formula[i]+formula[i+1]+formula[i+2])
                                i =+ 2 # incrementa 2, já q usou os 2 elementos após o atual
                                continue # continua o código

                        # caso não entre na condição anterior (caso não tenha 3 digitos)
                        vetResult.append(formula[i]+formula[i+1])
                        i =+ 1 # incrementa 1, já q usou apenas 1 elementos após o atual
                        continue # continua o código
                
                # caso não entre na condição anterior (caso tenha APENAS 1 dígido)
                vetResult.append(formula[i])
                ## não incrementa o i, porque não usamos os próximos elementos

    i = 0
    ## pega o tamanho do vetor q estavamos criando acima 
    a = len(vetResult) # pega o tamanho do vetor criado

    ## esse laço faz o cálculo e cria uma string com o resultado
    # cria a string do resultado
    while(i < a):

        # caso em que o elemento atual é um numero (dígito)
        if(vetResult[i].isdigit()): # verifica se é um dígito

            ## calcula e transforma em uma string para adicionar à string de resultado
            x = (str(numMols * int(vetResult[i]))) # calculo 

            # criando a string de arquivo e do terminal
            stringResult_file += ('\n' + vetResult[i - 1] + ': ' + (str((6.022*numMols) * int(vetResult[i]))) +
                                 '10^23')
            stringResult += ('\n' + x + ' mols de atomos de ' + vetResult[i - 1] + ' (' + x + 
                            'x6.022x10^23 = ' + (str((6.022*numMols) * int(vetResult[i]))) + 
                            '10^23)')
        
        # caso não tiver numero no final. ou seja, for apenas 1 mol (ex.: H2O)
        if((vetResult[i].isalpha()) and (i+1 == a) or ((vetResult[i].isalpha()) and (vetResult[i+1].isalpha()))):
            stringResult_file += ('\n' + vetResult[i] + ': ' + (str((6.022*numMols) * int(1))) + '10^23)')
            stringResult += ('\n' + '1 mol de atomo de ' + vetResult[i] + ' (' + str(numMols) +
                            'x6.022x10^23 = ' + (str((6.022*numMols) * int(1))) + '10^23)')
        i += 1
    
    # caso o usuário tenha optado por usar o terminal
    if(opcao_inicial == 1):
        return stringResult

    # caso o usuário tenha optado por usar arquivo
    if(opcao_inicial == 2):
        return stringResult_file
