import spacy
from nltk import RSLPStemmer
from spacy.tokens import Doc
from spacy.matcher import Matcher
from datetime import date, timedelta


nlp = spacy.load('pt_core_news_sm')


##
def remove_stopwords(doc, manter=[]):
    """Remove stopwords da sentenca, stopwords podem ser consultadas com spacy.lang.pt.stop_words.STOP_WORDS
    Parametros:
    manter: mantem as palavras passadas mesmo que esta seja stopword
    """
    doc_sem_stopwords = [p.orth_ for p in doc if (not any([p.is_stop,p.is_punct]) or p.orth_ in manter)]
    doc_sem_stopwords = nlp(' '.join(doc_sem_stopwords))
    return doc_sem_stopwords


## dbt tec transformar numeros por extenso em numero antes de remover stopwords
def date_getter(doc):
    """Transforma data no texto em obj datetime.date,"""
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
             "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    palav_chave = ['dia', 'mês', 'ano']
    d_ref = ['amanhã', 'hoje', 'ontem', 'anteontem']
    doc = remove_stopwords(doc, manter=meses+palav_chave+d_ref)
    matcher_mes = Matcher(nlp.vocab)
    pattern_meses = [{"ORTH": {"IN": meses}}]
    matcher_mes.add('MESES_PATTERN', None, pattern_meses)

    matcher_palav_chave = Matcher(nlp.vocab)
    matcher_palav_chave.add('PALAVRAS_PATTERN', None, [{"ORTH": {"IN": palav_chave}}])

    matcher_d_ref = Matcher(nlp.vocab)
    matcher_d_ref.add('HOJE_PATTERN', None, [{"ORTH": {"IN": d_ref}}])

    matches = {'mes': matcher_mes(doc),
               'palav_chave': matcher_palav_chave(doc),
               'd_ref': matcher_d_ref(doc)
               }

    if any(matches.values()):
        print('frase possui data')

        if matches['mes']:
            for match_id, start, end in matches['mes']:
                mes_nome = doc[start:end].orth_
                mes_num = meses.index(mes_nome) + 1
                index_mes = [p.orth_ for p in doc].index(mes_nome)
                dia = next(iter([int(p.orth_) for p in doc[index_mes].lefts if p.is_digit]), False)
                print(dia)
                ano = next(iter([int(p.orth_) for p in doc[index_mes].rights if p.is_digit]), False)
                dt = date(ano if ano else date.today().year,
                          mes_num,
                          dia if dia else 1)
                return dt

        if matches['d_ref']:
            for match_id, start, end in matches['d_ref']:
                match = doc[start:end].orth_
                d_ref_num = d_ref.index(match)
                dt = date.today() - timedelta(days=d_ref_num -1)
                return dt

    else:
        print('frase não possui data')

##
Doc.set_extension("get_date", getter=date_getter, force=True)


##
def identifica_comando(frase):
    # stemmer = RSLPStemmer()  # usado para pegar o radical da palavra
    doc = nlp(frase)
    dic_cmd = {}
    # dic_cmd = {'index_acao':[palavra.i for palavra in doc if palavra.dep_ == 'ROOT']}
    # dic_cmd['acao'] = doc[dic_cmd['index_acao']].orth_
    # dic_cmd['comp_acao'] = [palavra.orth_ for palavra in doc[dic_cmd['index_acao']].rights]
    # cmd = '_'.join([stemmer.stem(dic_cmd['acao']),
    #                 stemmer.stem(dic_cmd['comp_acao'])])

    dt = doc._.get_date
    if type(dt) == date:
        dic_cmd['date'] = dt

    return dic_cmd

## teste

# identifica_comando('amanhã vou no cinema')


##

