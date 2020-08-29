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
from random import randint


# %%

class ComunicacaoEstagiario(object):
    def __init__(self):
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Silencio, ajustando ruido do ambiente!!!')
            self.r.adjust_for_ambient_noise(source, 4)
        self.threshold = self.r.energy_threshold * 1.2
        self.r.dynamic_energy_threshold = False

    def tocar_audio(self, audios):
        if type(audios) == list:
            print("lista")
            audio = audios[randint(0, len(audios) - 1)]
        else:
            audio = audios
        try:
            playsound(audio)
        except:
            return f'audio não localizado: {audio}'

    def ouvir_microfone(self, texto_de_espera: str) -> str:
        """Funcao responsavel por ouvir e reconhecer a fala"""
        with sr.Microphone() as source:
            self.r.energy_threshold = self.threshold
            self.r.pause_threshold = 1
            print(texto_de_espera, ' ' * 20, end=' ', flush=True)
            audio = self.r.listen(source, timeout=None)  # Armazena a informacao de audio na variavel
        try:
            texto = self.r.recognize_google(audio, language='pt-BR')  # Transforma audio em texto
            print("\rVocê disse: " + texto, ' ' * 20, end='\n', flush=True)
            return texto.lower()
        # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
        except sr.UnknownValueError:
            return "Não entendi"


# %%

class ComandosEstagiario(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def _lista_de_comandos(self) -> None:
        pass

    def __seleciona_comando(self, comando: str) -> bool:
        comandos = self.lista_de_comandos
        if comando in comandos.keys():
            return True

    @staticmethod
    def __identifica_comando(frase: str) -> str:
        cmd = identifica_comando(frase)
        return cmd

    def _executa_comando(self, voz):
        comando = ComandosEstagiario.__identifica_comando(voz)
        try:
            comando = comando['acao_rad'] + '_' + comando['complem_rad']
            if comando in dir(hab):
                eval(f'hab.{comando}()')
                return comando
            else:
                resposta_app_IA = hab.AppsIA.google(voz)
                if resposta_app_IA:
                    return resposta_app_IA
                # vai ter uma funcao pra ele falar(audio)
                print('desculpe mestre eu nao sei fazer isso,sei fazer apenas isso:\n')
                return help(hab)
        except KeyError:
            resposta_app_IA = hab.AppsIA.google(voz)
            return resposta_app_IA if resposta_app_IA else print('Nao sei fazer isso :(  !!!!')


# %%

class Estagiario(ComandosEstagiario, ComunicacaoEstagiario):

    def __init__(self, microfone=True):
        super().__init__()
        self._lista_de_comandos = self.__manipula_lista_de_comandos
        self._microfone = microfone
        self.tocar_audio(self.audio_resposta('inicialização'))

    @property
    def __manipula_lista_de_comandos(self) -> dict:
        with open('listaDeHabilidades.json', 'r') as arquivo:
            dic = json.load(arquivo)
        return dic

    def audio_resposta(self, cmd):
        try:
            return self._lista_de_comandos[cmd]['audio']
        except KeyError:
            return None

    def interface(self):
        frase = self.ouvir_microfone('\rChame o Estagiário') if self._microfone else input('\nChamar: ')

        if 'estagiário' in frase:
            if self._microfone:
                self.tocar_audio(self.audio_resposta('oque fazer?'))
                frase = self.ouvir_microfone('\rOque devo fazer?')
            else:
                input('\nOque deve fazer: ')

            cmd = self._executa_comando(frase)
            print(cmd)
            if self._microfone: self.tocar_audio(cmd)
            self.interface()
        else:
            print('\restou dormindo', ' ' * 40, end=' ', flush=True)
            self.interface()

    def treino(self):
        frase = self.ouvir_microfone('Falar comando')
        dic_comando = identifica_comando(frase)
        return frase, dic_comando


# %%

if __name__ == '__main__':
    print('Iniciando estagiário')
    e = Estagiario(microfone=True)
    e.interface()
    # frase, dic = e.treino()

# %%
