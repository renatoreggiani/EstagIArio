#!/usr/bin/env python
# coding: utf-8

# In[1]:


#@autor Gustavo Moss /Renato Regianne
import speech_recognition as sr
from gtts import gTTS
from unicodedata import normalize
from playsound import playsound
import os
import sys
from diretorio.comandos import *
import spacy
from nltk import RSLPStemmer
from abc import ABCMeta, abstractmethod
nlp = spacy.load('pt_core_news_sm')
from Interpretador import *


# In[2]:


class ComunicacaoEstagiario(object):
    
    def cria_audio(audio):
        tts = gTTS(audio,lang='pt-br')
        #Salva o arquivo de audio
        tts.save('/home/moss/IA/teste.mp3')
        print("sim mestre")
        #Da play ao audio
        playsound('/home/moss/IA/teste.mp3')

    
    def ouvir_microfone():
        """Funcao responsavel por ouvir e reconhecer a fala"""
        microfone = sr.Recognizer()  # Habilita o microfone para ouvir o usuario
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)  # Chama a funcao de reducao de ruido
            print("Diga alguma coisa: ")
            #microfone.pause_threshold = 0.8
            audio = microfone.listen(source,timeout=None)  # Armazena a informacao de audio na variavel
            
        try:
            texto = microfone.recognize_google(audio, language='pt-BR')  # Transforma audio em texto
            print("Você disse: " + texto)
            return texto.lower()
        # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
        except sr.WaitTimeoutError:
            print("Não entendi")
            
    


# In[3]:


class ComandosEstagiario(object):
        
        __metaclass__=ABCMeta
        
        @abstractmethod
        def _listaDeComandos():
            pass
        
        
        def __selecionaComando(self,comando):
            comandos=self.listaDeComandos()
            if comando in comandos.keys():
                return True
    
        @staticmethod
        def __identificaComando(frase):
            cmd=identifica_comando(frase)
            return cmd
            
            
        def _executaComando(self,voz):
            comando=ComandosEstagiario.__identificaComando(voz)
            comando=comando['acao_rad']+'_'+comando['complem_rad']
            print(comando)
            if self.__selecionaComando(comando):
                return eval(f'{comando}()')     
            else:
                #vai ter uma funcao pra ele falar(audio)
                print('desculpe mestre eu nao sei fazer isso,sei fazer apenas isso:\n')
                return list_com()
            

                    
    


# In[8]:


class Estagiario(ComandosEstagiario,ComunicacaoEstagiario):
    
    def __init__(self):
        self._listaDeComandos=self._manipulaListaDeComandos()
        self._status='DISABLED'
    
    def activatedEstagiario(self,frase):
        frase =frase.capitalize().strip()
        if frase =='Estagiario':
            self._status="ACTIVATED"
        elif self._status == 'DISABLED':
            print('estou dormindo')
            #frase=self.ouvir_microfone()
            frase=input('comando:')
            self.activatedEstagiario(frase)       
         
    
    def _manipulaListaDeComandos(self):
            with open('listaDeComandos.txt','r') as arquivo:
                dic=arquivo.read()
                dic=eval(dic)
            return dic
        
    def listaDeComandos(self):
        return self._listaDeComandos
        
    def interface(self):
        #frase=self.ouvir_microfone() #automatizado 
        frase=input('comando:')#manual para testes
        self.activatedEstagiario(frase)
        #frase=self.ouvir_microfone() #automatizado 
        frase=input('comando:')#manual para testes
        print(self._executaComando(frase))
        self.interface()


# In[9]:


if __name__ == '__main__':
    e=Estagiario()

    e.interface()

