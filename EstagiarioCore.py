# @autor Gustavo Moss /Renato Regianne
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import diretorio.habilidades as hab
from abc import ABCMeta, abstractmethod
from Interpretador import identifica_comando


##
class ComunicacaoEstagiario(object):

    def cria_audio(audio):
        tts = gTTS(audio, lang='pt-br')
        # Salva o arquivo de audio
        tts.save('/home/moss/IA/teste.mp3')  # corrigir
        print("sim mestre")
        # Da play ao audio
        playsound('/home/moss/IA/teste.mp3')  # corrigir

    @staticmethod
    def ouvir_microfone(texto_de_espera):
        """Funcao responsavel por ouvir e reconhecer a fala"""
        microfone = sr.Recognizer()  # Habilita o microfone para ouvir o usuario
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)  # Chama a funcao de reducao de ruido
            print(texto_de_espera, ' ' * 20, end='\r', flush=True)
            # microfone.pause_threshold = 0.8
            audio = microfone.listen(source, timeout=None)  # Armazena a informacao de audio na variavel
        try:
            texto = microfone.recognize_google(audio, language='pt-BR')  # Transforma audio em texto
            print("Você disse: " + texto, ' ' * 20, end='\r', flush=True)
            return texto.lower()
        # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
        except sr.UnknownValueError:
            return "Não entendi"


##
class ComandosEstagiario(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def _lista_de_comandos(self):
        pass

    def __seleciona_comando(self, comando):
        comandos = self.lista_de_comandos()
        if comando in comandos.keys():
            return True

    @staticmethod
    def __identifica_comando(frase):
        cmd = identifica_comando(frase)
        return cmd

    def _executa_comando(self, voz):
        comando = ComandosEstagiario.__identifica_comando(voz)
        try:
            comando = comando['acao_rad'] + '_' + comando['complem_rad']
            print(comando)
            if self.__seleciona_comando(comando):
                return eval(f'hab.{comando}()')
            else:
                # vai ter uma funcao pra ele falar(audio)
                print('desculpe mestre eu nao sei fazer isso,sei fazer apenas isso:\n')
                return hab.list_com()
        except KeyError:
            print(KeyError)


##
class Estagiario(ComandosEstagiario, ComunicacaoEstagiario):

    def __init__(self, microfone=True):
        self._lista_de_comandos = self._manipula_lista_de_comandos()
        self.microfone = microfone

    def interface(self):
        frase = self.ouvir_microfone('Chame o Estagiário para começar') if self.microfone\
                else input('\nChamar: ')
        if 'estagiário' in frase:
            frase = self.ouvir_microfone('Oque devo fazer?') if self.microfone\
                    else input('\nOque deve fazer: ')
            print(frase)
            print(self._executa_comando(frase))
            self.interface()
        else:
            print('estou dormindo', ' ' * 20, end='\r', flush=True)
            self.interface()

    def _manipula_lista_de_comandos(self):
        with open('listaDeHabilidades.txt', 'r') as arquivo:
            dic = arquivo.read()
            dic = eval(dic)
        return dic

    def lista_de_comandos(self):
        return self._lista_de_comandos


##
if __name__ == '__main__':
    print('Iniciando estagiário')
    e = Estagiario(microfone=False)
    e.interface()
