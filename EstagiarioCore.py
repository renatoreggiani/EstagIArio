#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 00:54:31 2020

@author: Gustavo Moss /Renato Regianne
"""

# %%
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import habilidades as hab
from abc import ABCMeta, abstractmethod
from Interpretador import identifica_comando
import json


#%%

class ComunicacaoEstagiario(object):

    def cria_audio(audio):
        tts = gTTS(audio, lang='pt-br')
        # Salva o arquivo de audio
        tts.save('/home/moss/IA/teste.mp3')  # corrigir
        print("sim mestre")
        # Da play ao audio
        playsound('/home/moss/IA/teste.mp3')  # corrigir

    def ouvir_microfone(self, texto_de_espera:str)-> str:
        """Funcao responsavel por ouvir e reconhecer a fala"""
        microfone = sr.Recognizer()  # Habilita o microfone para ouvir o usuario
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)  # Chama a funcao de reducao de ruido
            print(texto_de_espera, ' ' * 20, end='\r', flush=True)
            microfone.pause_threshold = 2.5
            audio = microfone.listen(source, timeout=None)  # Armazena a informacao de audio na variavel
        try:
            texto = microfone.recognize_google(audio, language='pt-BR')  # Transforma audio em texto
            print("Você disse: " + texto, ' ' * 20, end='\r', flush=True)
            return texto.lower()
        # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
        except sr.UnknownValueError:
            return "Não entendi"


#%%

class ComandosEstagiario(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def _lista_de_comandos(self)-> None:
        pass

    def __seleciona_comando(self, comando:str)-> bool:
        comandos = self.lista_de_comandos
        if comando in comandos.keys():
            return True

    @staticmethod
    def __identifica_comando(frase:str)->str:
        cmd = identifica_comando(frase)
        return cmd

    def _executa_comando(self, voz:str):
        comando = ComandosEstagiario.__identifica_comando(voz)
        try:
            comando = comando['acao_rad'] + '_' + comando['complem_rad']
            if self.__seleciona_comando(comando):
                return eval(f'hab.{comando}()')
            else:
                # vai ter uma funcao pra ele falar(audio)
                print('desculpe mestre eu nao sei fazer isso,sei fazer apenas isso:\n')
                return hab.list_com()
        except KeyError:
            print(KeyError)


#%%

class Estagiario(ComandosEstagiario, ComunicacaoEstagiario):

    def __init__(self, microfone=True):
        self._lista_de_comandos:dict = self.__manipula_lista_de_comandos()
        self._microfone:bool = microfone

    @property
    def lista_de_comandos(self)-> dict:
        return self._lista_de_comandos

    def interface(self)-> None:
        frase = self.ouvir_microfone('Chame o Estagiário para começar') if self._microfone \
            else input('\nChamar: ')
        if 'estagiário' in frase:
            frase = self.ouvir_microfone('Oque devo fazer?') if self._microfone \
                else input('\nOque deve fazer: ')
            print(frase)
            print(self._executa_comando(frase))
            self.interface()
        else:
            print('estou dormindo', ' ' * 20, end='\r', flush=True)
            self.interface()

    def __manipula_lista_de_comandos(self)-> dict:
        with open('listaDeHabilidades.json','r') as arquivo:
            dic= json.load(arquivo)
        return dic

    def treino(self):
        frase = self.ouvir_microfone('Falar comando')
        dic_comando = identifica_comando(frase)
        return frase, dic_comando


#%%

if __name__ == '__main__':
    print('Iniciando estagiário')
    e = Estagiario(microfone=False)
    # e.interface()
    frase, dic = e.treino()
#%%
def Cri