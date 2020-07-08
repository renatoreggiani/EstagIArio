import json
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from unicodedata import normalize
import os


##
def cria_audio(texto):
    """Cria o audio utilizado TTS do google translator"""
    nome_arq = normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')  # Remove acentos das frases
    if not os.path.isfile(f'audios/{nome_arq}.mp3'):
        print("Estou aprendendo o que você disse...")
        tts = gTTS(texto, lang='pt-br', lang_check=False)
        tts.save(f'audios/{nome_arq}.mp3')
    playsound(f'audios/{nome_arq}.mp3')


##
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
            texto = texto.replace('estagiário', '').strip()
            print("Você disse: " + texto)
            return texto
    # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except sr.WaitTimeoutError:
        print("Não entendi")


##
if __name__ == '__main__':
    dados = json.load(open('tarefas/dict_tarefas.json', encoding='utf8'))
    frase = ouvir_microfone()
    cria_audio(frase)
    print(frase)


