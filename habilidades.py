def som_cont():
    x=1+1
    return x

def faz_pesquis():
    from wikipedia import set_lang,summary
    set_lang('pt')
    info=input('Oque desejas pesquisar mestre?\n')
    return summary(info,sentences=2)

def abr_sit():
    from webbrowser import open
    site = input('Qual site você gostaria de abrir mestre:')
    return open(f"https://www.{site}.com",new=2)

def final_sistem():
    import sys
    return sys.exit()
 
def list_com():
    import json
    with open('listaDeHabilidades.json','r') as arquivo:
        teste= json.load(arquivo)
        for valor in teste:
            print(f'Comando: {valor}\ndescrição:{teste[valor]}')
            print('--------------')
            
