import pyttsx3
import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
    except sr.RequestError:
        print("Sorry, speech recognition service is unavailable.")

# Call the function to recognize speech
recognized_text = recognize_speech()

# Print the recognized text
if recognized_text:
    print("Recognized Text:", recognized_text)

# Speak the recognized text
engine.say(recognized_text)
engine.runAndWait()
