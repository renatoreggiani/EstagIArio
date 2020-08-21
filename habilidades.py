import json
import os
import sys
# import wolframalpha
# import wikipedia
import requests
from bs4 import BeautifulSoup


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


# def list_com():
#     with open('listaDeHabilidades.json', 'r') as arquivo:
#         teste = json.load(arquivo)
#         for valor in teste:
#             print(f'Comando: {valor}\ndescrição:{teste[valor]}')
#             print('--------------')


def abr_excel():
    '''Comando: Abir excel,
    Funcao: inicia o excel'''
    os.system('start excel.exe')

class AppsIA():
    
    def google(frase):
        frase = frase.replace('+', 'mais')
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        r = requests.get('https://www.google.com/search?&q='+frase, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        classes_google = ['vk_c card-section',
                          'webanswers-webanswers_table__webanswers-table',
                          'aviV4d']
        resp = [(classe, soup.find('div', class_=classe)) for classe in classes_google
                if soup.find('div', class_=classe) is not None]
        if resp:
            if resp[0][1].text.strip().startswith('Resultado da calculadora'):
                return resp[0][1].text[resp[0][1].text.find('='):].split()[1]

    # def wolfram(frase):
    #     client = wolframalpha.Client('Your_App_ID')
    #     try:
    #         res = client.query(frase)
    #         results = next(res.results).text
    #         print('WOLFRAM-ALPHA says - ')
    #         return results
    #     except:
    #         return False
    #
    # def wikipedia(frase):
    #     results = wikipedia.summary(frase, sentences=2)
    #     print('WIKIPEDIA says - ')
    #     return results




#%%

