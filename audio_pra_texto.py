import speech_recognition as sr #importando o módulo de reconhecimento de voz como "sr"
import pyttsx3

reconhecedor = sr.Recognizer() #a variável que vai reconhecer voz

def grava_texto():

    while True:
        try:
        #try que vai ser oq nosso while vai executar se não houver nenhum erro 
            
            with sr.Microphone() as microfone:
            #with aqui usado pra usar o sr.Microphone e depois parar, ou seja, o sr.Microphone só vai ser aberto e usado dentro desse with, se não fosse usado o with o microphone seria usado durante todo o código.

                 
                reconhecedor.adjust_for_ambient_noise(microfone, duration=0.5)
                #adjust_for_ambient_noise serve para ajustar o reconhecimento de voz ao barulho ambiente. durante duration 0.5 o reconhecedor vai escutar os ruídos de fundo pra saber oq não é voz e aí ter uma percepção melhor.

                audio = reconhecedor.listen(microfone, phrase_time_limit=7)
                #aqui bem intuitivo. o nosso áudio vai ser oq o reconhecedor de voz escutar (listen) no nosso microfone

                texto_do_audio = reconhecedor.recognize_(audio, language="pt-BR")
                #outra parte intuitiva. o texto do áudio vai ser oq o transcritor da amazon reconhecer.

                return texto_do_audio
        except sr.RequestError as e:
            print(f"Não conseguimos fazer a requisição; {e}")
            return
        except sr.UnknownValueError:
            print(f'Erro desconhecido. ')
            return


def envia_texto(txt):

    arquivo = open("output.txt", 'a')
    #criando um arquivo txt pra salvar nossa transcrição - se não tiver nenhum arquivo "output.txt" ele cria. e o 'a' é pra append esse texto no arquivo, ou seja, que nem o append em uma array, o texto vai entrar no final do texto.

    arquivo.write(txt)
    arquivo.write(f", ")
    arquivo.close() 


while True:
    texto = grava_texto()
    if texto != None:
        envia_texto(texto)
        print("Texto Escrito!")
    else:
        print("Texto não foi capturado, tentando novamente...")
