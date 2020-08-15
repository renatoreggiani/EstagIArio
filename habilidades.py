import json
import os
import sys


def som_cont():
    '''Comando: Somar conta,
    Funcao: soma 1+1'''
    x = 1 + 1
    return x


def faz_pesquis():
    '''Comando: Fazer pesquisa,
    Funcao: Abre o wikipedia com pesquisa digitada no input'''
    from wikipedia import set_lang, summary
    set_lang('pt')
    info = input('Oque desejas pesquisar mestre?\n')
    return summary(info, sentences=2)


def abr_sit():
    '''Comando: Abir site,
    Funcao: Abre o site digitado no input'''
    from webbrowser import open
    site = input('Qual site você gostaria de abrir mestre:')
    return open(f"https://www.{site}.com", new=2)


def final_sistem():
    '''Comando: Finalizar sistema,
    Funcao: encerra a execucao do EstagIArio'''
    return sys.exit()


def abr_googl():
    '''Comando: Abir google,
    Funcao: Abre o google no nagevador padrao'''
    from webbrowser import open
    return open("https://www.google.com", new=2)


def list_com():
    with open('listaDeHabilidades.json', 'r') as arquivo:
        teste = json.load(arquivo)
        for valor in teste:
            print(f'Comando: {valor}\ndescrição:{teste[valor]}')
            print('--------------')


def abr_excel():
    '''Comando: Abir excel,
    Funcao: inicia o excel'''
    os.system('start excel.exe')


