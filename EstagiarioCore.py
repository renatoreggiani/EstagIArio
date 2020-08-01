#!/usr/bin/env python
# coding: utf-8

# In[1]:


#@autor Gustavo Moss /Renato Regianne

import speech_recognition as sr #reconhecimento de voz
from gtts import gTTS #voz do estagiario
from unicodedata import normalize #voz do estagiario
from playsound import playsound #voz do estagiario
import os
import sys
from comandos import * #comandos do estagiario
import spacy
from nltk import RSLPStemmer
from abc import ABCMeta, abstractmethod
nlp = spacy.load('pt_core_news_sm')
from Interpretador import *


# In[2]:


class ComunicacaoEstagiario(object):
    
    def falar(audio):
        tts = gTTS(audio,lang='pt-br')
        #Salva o arquivo de audio
        tts.save('/home/moss/IA/teste.mp3')
        print("sim mestre")
        #Da play ao audio
        #playsound('/home/moss/IA/teste.mp3')

    
    def ouvir(self):
        """Funcao responsavel por ouvir e reconhecer a fala"""
        microfone = sr.Recognizer()  # Habilita o microfone para ouvir o usuario
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)  # Chama a funcao de reducao de ruido
            print("Diga alguma coisa: ")
            #microfone.pause_threshold = 0.8
            audio = microfone.listen(source)  # Armazena a informacao de audio na variavel
#             if audio == None:
#                 self.ouvir()
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
            if self.__selecionaComando(comando):
                return eval(f'{comando}()')     
            else:
                #vai ter uma funcao pra ele falar(audio)
                print('desculpe mestre eu nao sei fazer isso,sei fazer apenas isso:\n')
                return list_com()
            

                    
    


# In[4]:


class Estagiario(ComandosEstagiario,ComunicacaoEstagiario):
    
    def __init__(self):
        self._listaDeComandos=self._manipulaListaDeComandos()
        self._status='DISABLED'
    
    def activatedEstagiario(self,frase):
        frase =frase.capitalize().strip()
        if frase =='Estagiario':
            self._status="ACTIVATED"
        else:
            print('estou dormindo')
            frase=self.ouvir_microfone()
            #frase=input('comando:')
            self.activatedEstagiario(frase)
     #funcao de fala
        print('Olá mestre...')
         
    
    def _manipulaListaDeComandos(self):
            with open('listaDeComandos.txt','r') as arquivo:
                dic=arquivo.read()
                dic=eval(dic)
            return dic
        
    def listaDeComandos(self):
        return self._listaDeComandos
        
    def interface(self):
        frase=self.ouvir() #automatizado 
        #frase=input('comando:')#manual para testes
        self.activatedEstagiario(frase)
        frase=self.ouvir() #automatizado 
        #frase=input('comando:')#manual para testes
        print(self._executaComando(frase))
        self._status='DISABLED'
        self.interface()


# In[5]:


if __name__ == '__main__':
    e=Estagiario()

    e.interface()


# In[ ]:




