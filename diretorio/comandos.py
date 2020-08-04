def som_cont():
    x=1+1
    return x

def subtra_cont():
    x=2-3 
    return x

def abr_sit():
    from webbrowser import open
    return open("https://www.google.com",new=2)

def final_sistem():
    import sys
    return sys.exit()
    
def list_com():
    with open('listaDeComandos.txt','r') as arquivo:
        dic=arquivo.read()
        dic=eval(dic)

    for valores in dic.values():
        key=valores.index('-')
        print('comando:'+valores[:key].rstrip().strip()+"\n"+'funcao:'+valores[key+1:].rstrip().strip()+"\n")

