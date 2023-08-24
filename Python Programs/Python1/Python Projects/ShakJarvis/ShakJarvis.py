import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print(voices[0].id) -> David voice
# print(voices[1].id) -> Zara voice
engine.setProperty('voice', voices[0].id)

def wishMe():
    currentHour = int(datetime.datetime.now().hour)
    
    if currentHour >= 0 and currentHour <12:
        speak("Good Morning!")
    elif currentHour >= 12 and currentHour < 18:
        speak("Good After Noon!")
    else:
        speak("Good Evening!")
        
    speak("I am Jarvis Sir. Please tell me how may I help you")

def speak(audioText):
    print(audioText)
    engine.say(audioText) #Prepares the audioText to be spoken by the text-to-speech engine
    engine.runAndWait() #Triggers the text-to-speech engine to speak out the provided audioText

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source: #no need to stop microphone manually(using with statement)
        speak("\nListening...")
        r.pause_threshold = 1 #The amount of silence in seconds that the recognizer will allow before considering a phrase to be complete
        audio = r.listen(source)

    try:
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        speak(f"You said: {query}")
    except Exception as e:
        speak("I didn't get you, Say that again please...")
        return "None" #return "None" string if exception arise(Note: it is not a None object)
    return query
        




if __name__ == "__main__":
    # wishMe()
    while True:
        query = takeCommand().lower()
        
        #Logic for executing tasks based on query
        
        if "how are you" in query or "hi" in query:
            hayAnswer = [
                "I'm just a computer program, so I don't have feelings or emotions, but I'm here and ready to assist you! How can I help you today?",
                "I'm just a computer program, so I don't have feelings or emotions, but I'm here and ready to assist you! How can I help you today?",
                "I appreciate your inquiry, but as a machine learning model, I don't have feelings or emotions. However, I'm here and ready to assist you with any questions or tasks you might have. How can I be of service today?",
                "I'm an AI language model, so I don't have emotions or feelings, but I'm here and ready to help you with any questions or tasks you have. How can I assist you today?",
                "I'm a computer program, so I don't experience emotions, but I'm here and ready to assist you! How can I be of help today?",
                "Hello! How can I assist you today?",
                "Hello! How can I help you today? If you have any questions or need assistance, feel free to ask.",
                "I'm just a machine, so I don't have feelings, but I'm here and ready to assist you with any questions or tasks you have. How can I help you today?"
            ]
            speak(random.choice(hayAnswer))
            
        elif "who are you" in query:
            whoAnswers = [
                "I am your virtual assistant, Jarvis, designed to help and assist you.",
                "I'm an AI-powered assistant, Jarvis, here to make your tasks easier.",
                "I'm an AI-powered assistant, Jarvis, here to make your tasks easier.",
                "I'm an artificial intelligence, Jarvis, at your service.",
                "I go by the name Jarvis, ready to assist you in any way I can.",
                "I'm your personal AI assistant, Jarvis, always here to help.",
                "You can call me Jarvis, your AI helper and companion.",
                "I'm your digital buddy, known as Jarvis, here to provide support.",
                "I'm an AI entity designed to make your life more convenient, Jarvis.",
                "I'm the AI creation known as Jarvis, here to lend a hand.",
                "Hi there, I'm Jarvis, your dedicated AI assistant, ready to assist you.",
                "Hi there, I'm Jarvis, your dedicated AI assistant, ready to assist you.",
            ]
            speak(random.choice(whoAnswers))
        
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            
                    
        elif any(keyword in query for keyword in ["play music", "play the music", "play a music"]):
            saySomething = [
                "I've got some music for you.",
                "Presenting a piece of music just for you.",
                "Here's a tune I think you'll enjoy.",
                "Enjoy this music that I've selected for you.",
                "I've picked out a song for your listening pleasure.",
                "Delight in this musical selection I've prepared.",
                "I'm sharing a track with you right now.",
                "Take a moment to enjoy the following musical piece.",
                "I've brought a musical experience your way.",
                "Tune in to this melody I've chosen for you."
            ]
            speak(random.choice(saySomething))
            musicDir = "F:\\Naat"
            songs = os.listdir(musicDir)
            randomSong = random.randint(0, len(songs)-1)
            os.startfile(os.path.join(musicDir, songs[randomSong]))
            
            
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif "open" in query and "code" in query:
            os.system("code")


        elif "open" in query and "notepad" in query:
            os.system("notepad")


        elif "open" in query:
            wordsList = query.split()
            openIndex = wordsList.index("open")
            webSearch = 'google'
            if openIndex == len(wordsList) - 1: #open arrives at last index so its an incomplete sentence
                speak("What do you wanted to open, Please complete your sentence..!")
            elif wordsList[openIndex + 1] == "the":
                theIndex = openIndex + 1
                if theIndex == len(wordsList) - 1: #the arrives at last index so its an incomplete sentence
                    speak("What do you wanted to open, Please complete your sentence..!")
                else:
                    webSearch = wordsList[theIndex + 1]
                    webbrowser.open(webSearch+".com")
            else:
                webSearch = wordsList[openIndex + 1]
                webbrowser.open(webSearch+".com")
                
                
        elif any(keyword in query for keyword in ["stop jarvis", "quit jarvis", "exit jarvis", "jarvis stop", "jarvis quit", "jarvis exit", ]):
            stop = [
                "Jarvis, enter standby mode and accompany me with your digital prowess, making this journey a delightful one.",
                "Putting Jarvis on hold, may your voyage be enriched by the company of my AI counterpart.",
                "Temporarily pausing Jarvis, I send you off with the company of our AI comrade to enhance your journey.",
                "Suspending Jarvis momentarily, may your travels be graced by the presence of my AI companion.",
                "Switching Jarvis to idle mode, may your adventure be enlivened by the wisdom of our digital ally",
                "Pausing Jarvis temporarily, I entrust my AI companion to be your guide on this expedition.",
                "Activating standby for Jarvis, may your path be enlightened by the insights of our AI friend.",
                "Activating standby for Jarvis, may your path be enlightened by the insights of our AI friend.",
                "Temporarily halting Jarvis, I bestow upon you the insights and companionship of our AI ally.",
                "Putting Jarvis in standby mode, I wish you a captivating journey accompanied by my knowledgeable AI comrade.",
            ]
            speak(random.choice(stop))
            break