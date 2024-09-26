from translate import Translator
import speech_recognition as sr
import pyttsx3
a=str(input("Do you want to SPEAK or WRITE     "))
if a.lower() == "speak":
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source)   

    try:
        print("Checking:")
        text=r.recognize_google(audio)
        print("You said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
else:
    text=str(input("What is the text?     "))
print("")
la=str(input("What language do you want to translate it in?     "))
translator= Translator(to_lang=la)
translation = translator.translate(text)
print(translation)
engine=pyttsx3.init()
engine.say(translation)
engine.runAndWait()
