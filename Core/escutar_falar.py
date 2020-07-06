import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from unicodedata import normalize


##
def cria_audio(texto):
    """Cria o audio utilizado TTS do google translator"""
    tts = gTTS(texto, lang='pt-br', lang_check=False)
    nome_arq = normalize('NFKD', frase).encode('ASCII', 'ignore').decode('utf-8')
    tts.save(f'audios/{nome_arq}.mp3')
    print("Estou aprendendo o que você disse...")
    # Da play ao audio
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
            print("Você disse: " + texto)
            return texto
    # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except sr.WaitTimeoutError:
        print("Não entendi")




##
frase = ouvir_microfone()
cria_audio(frase)

print(frase)

##
