#!/usr/bin/env python
# coding: utf-8

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import sys
#import comandos


# In[8]:


class ComunicacaoEstagiario(object):

    def cria_audio(audio):
        tts = gTTS(audio, lang='pt-br')
        # Salva o arquivo de audio
        tts.save('/home/moss/IA/teste.mp3')
        print("sim mestre")
        # Da play ao audio
        playsound('/home/moss/IA/teste.mp3')

    def ouvir_microfone():
        """Funcao responsavel por ouvir e reconhecer a fala"""
        microfone = sr.Recognizer()  # Habilita o microfone para ouvir o usuario
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)  # Chama a funcao de reducao de ruido
            print("Diga alguma coisa: ")
            audio = microfone.listen(source)  # Armazena a informacao de audio na variavel
        try:
            texto = microfone.recognize_google(audio, language='pt-BR')  # Transforma audio em texto
            if 'estagiário' in texto.lower():
                print("Você disse: " + texto)
                return texto
        # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
        except sr.WaitTimeoutError:
            print("Não entendi")


# In[9]:


class ComandosEstagiario(object):

    #         transforma a primeira linha do arquivo em lista,
    #         a lista de comandos para poder ser manipulada,
    #         funcao privada
    def __manipulaListaDeComandos():
        with open('comandos.py', 'r') as arquivo:
            linhas = arquivo.readlines()
        lista = eval(linhas[0])
        return lista

    def __selecionaComando(comando):
        comandos = ComandosEstagiario.__manipulaListaDeComandos()
        if comando in comandos:
            return True

    def __identificaComando(frase):
        # so exemplo , vou mudar dps,aqui q vai entrar a lematizacao nlp
        frase = nlp(frase)
        acao = [palavra.lemma_ for palavra in frase if palavra.is_alpha and palavra.dep_ =='ROOT']
        if len(acao) == 1:
            comp_acao = [t.text for t in doc[1].rights]
            if nlp(comp_acao).
        return '_'.join(comando)

    def executaComando(voz):
        comando = ComandosEstagiario.__identificaComando(voz)
        if ComandosEstagiario.__selecionaComando(comando):
            eval(f'Estagiario.{comando}()')
        else:
            # vai ter uma funcao pra ele falar(audio)
            print('desculpe mestre eu nao sei fazer isso, sou apenas um estagiario')


# In[ ]:


class Estagiario(ComandosEstagiario, ComunicacaoEstagiario):
    def interface():
        frase = Estagiario.ouvir_microfone()
        Estagiario.executaComando(frase)
        if not (frase):
            sys.exit()

        interface()
##
e = Estagiario()
e.interface()

