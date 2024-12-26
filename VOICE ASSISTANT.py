import pyttsx3

myName = 'Vishal'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  
print(voices)  


def speak(audio):
    engine.say(audio)  
    engine.runAndWait() 


speak(f"Hello, {myName}. Welcome to the text-to-speech program!")