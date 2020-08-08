def som_cont():
    x=1+1
    return x

def faz_pesquis():
    from wikipedia import set_lang,summary
    wk.set_lang('pt')
    info=input('Oque desejas pesquisar mestre?\n')
    return wk.summary(info,sentences=2)

def abr_sit():
    from webbrowser import open
    site = input('Qual site você gostaria de abrir mestre:')
    return open(f"https://www.{site}.com",new=2)

def final_sistem():
    import sys
    return sys.exit()
    
def list_com():
    with open('listaDeHabilidades.txt','r') as arquivo:
        dic=arquivo.read()
        dic=eval(dic)

    for valores in dic.values():
        key=valores.index('-')
        print('comando:'+valores[:key].rstrip().strip()+"\n"+'funcao:'+valores[key+1:].rstrip().strip()+"\n")

