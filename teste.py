
import speech_recognition as sr
import pyttsx3
import wikipedia 
import wolframalpha
import threading
import tkinter as tk 

# Speech engine 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
actvWord = ['jarvis','computer','tuesday']

def speak (text, rate = 170):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


def parseCommand():
    listener = sr.Recognizer()
    print('Escutando....')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        audio = listener.listen(source)

        try:
            print('Recognizing...')
            query = listener.recognize_google(audio, language='pt-BR')
            print(f'User said: {query}\n')
        except Exception as e:
            print('Não foi possível reconhecer a voz' )
            speak('Não foi possível reconhecer a voz ')
            print(e)
            return 'None'
        
        return query
    
# Main loop

if __name__ == '__main__':
    speak('Todos os sistemas ligados')
    while True:
        query = parseCommand().lower().split()
        if query[0] == actvWord:
            query.pop(0)

            #List commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Hello, I am Jarvis')
            else:
                query.pop(0)
                speech = ' '.join(query)
                speak(speech)





        