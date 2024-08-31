import time
import pyttsx3
import speech_recognition as sr

def speak(text):
    print("Audio is processing")

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        r.pause_threshold = 0.5
        r.non_speaking_duration = 0.3
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

        try:
            print("Recognizing...")
            current_time = time.time()
            query = r.recognize_google(audio, language='en-in')
            time_After_recognize = time.time()
            print("The time taken to recognize the speech is:", time_After_recognize - current_time)
            print("User said:", query)
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""
        return query.lower()

text = recognize()
speak(text) if text else speak("No text recognized")
