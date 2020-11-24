# -*- coding: utf-8 -*-
## a linha acima elimina alguns erros de type, etc

import os #para limpar a tela deixando o terminal menos poluído

# aqui iremos fazer a importação das funções separadas para n 
# poluir o código
import option1
import option2
import option3
import option4
import option5


## essa é a função principal, na qual o programa deve ser chamado
## assim que iniciado. ele dá o ponta-pé inicial já q inicia o primeiro
## menu de inicialização

# função principal
def principal():

    resposta = 0 

    # laço responsável por pegar a resposta do usuário e realizar
    # as devidas ações
    while(1): #1 = veradeiro

        print('1 - pelo usuario')
        print('2 - por arquivo')
        print('3 - sair')

        resposta = int(input('=> ')) ## pega resposta do usuário

        os.system('clear') or None # limpa a tela

        ## caso a entrada de dados seja feita pelo usuário
        # entrada por usuário
        if(resposta == 1):
            principal2(1)
        ## caso a entrada de dados seja feita por arquivo
        # entrada por arquivo
        if(resposta == 2):
            principal2(2)
        # saida
        if(resposta == 3):
            exit(0)

## repare que nesse código, primeiro é realizado a requisição de 
## qual opção de menu o usuário quer fazer independente se for por
## arquivo ou não. PRIMEIRO ELE ESCOLHE QUAL CÁLCULO QUER FAZER PARA
## SÓ ENTÃO, DECIDIR SE VAI SER POR ENTRADA DE DADOS COM ARQUIVO OU NÃO

# função auxiliar (segundo menu de usuário)
def principal2(opcao):

    resposta = 0
    ## laço responsavel por saber qual opção de cálculo o usuário 
    ## deseja fazer (independente de entrada de arquivo ou não)
    # laço responsavel por saber qual opção de cálculo o usuário
    # deseja realizar
    while(1): # 1 = verdadeido

        print(':::::MENU:::::')
        print('1 - Determinacao do numero de atomos de cada elemento de uma formula a partir donumero de mols')
        print('2 - Calculo concentracao molar de uma solucao')
        print('3 - Calculo da quantidade de um gas produzido')
        print('4 - Calculo do tempo de meia vida para uma reacao com cinetica de primeira ordem')
        print('5 - Calculo da energia livre de Gibbs')
        print('6 - menu anterior')
        print('7 - sair')

        resposta = int(input('=> ')) ## escolha q deseja

        os.system('clear') or None # limpa o terminal

        # numero de atomos
        if(resposta == 1):
            option1.option(opcao)

        # concentração molar
        if(resposta == 2):
            option2.option(opcao)

        # gás produzido
        if(resposta == 3):
            option3.option(opcao)

        # meia vida
        if(resposta == 4):
            option4.option(opcao)

        # energia livre 
        if(resposta == 5):
            option5.option(opcao)

        # voltar ao menu anterior
        if(resposta == 6):
            principal()
            break
        
        # sair
        if(resposta == 7):
            exit(0)




principal()