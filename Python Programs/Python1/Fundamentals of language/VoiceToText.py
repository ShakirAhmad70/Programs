import speech_recognition as sr

def convert_speech_to_text():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise for better accuracy
        r.adjust_for_ambient_noise(source)

        # Listen for user input
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Call the function to start converting voice to text
convert_speech_to_text()