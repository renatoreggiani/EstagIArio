import spacy
from nltk import RSLPStemmer
nlp = spacy.load('pt_core_news_sm')


##
def identifica_comando(frase):
    stemmer = RSLPStemmer()  # usado para pegar o radical da palavra
    doc = nlp(frase)
    dic_cmd = {'index_acao':[palavra.i for palavra in doc if palavra.dep_ == 'ROOT'][0]}
    dic_cmd['acao'] = doc[dic_cmd['index_acao']].orth_
    dic_cmd['comp_acao'] = [palavra.orth_ for palavra in doc[dic_cmd['index_acao']].rights][0]
    cmd = '_'.join([stemmer.stem(dic_cmd['acao']),
                    stemmer.stem(dic_cmd['comp_acao'])])
    return cmd



