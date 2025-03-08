import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclb  # Ensure this is a valid module and that it is properly configured
import requests

engine = pyttsx3.init()
api_key = "9a3646392c994219b6764bdec45694c6"

# Get the available voices
voices = engine.getProperty('voices')

# Print details of each voice (optional)

# Print details of each voice
for index, voice in enumerate(voices):
    languages = voice.languages if hasattr(voice, 'languages') else ["Not Available"]
    print(f"Voice {index}: {voice.name}")

# Example: Change to the second voice in the list (if available)
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)

# Optional: Adjust rate and volume
engine.setProperty('rate', 200)
engine.setProperty('volume', 4.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def sayCommand(c):
    c = c.lower()
    if "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open mangadex" in c:
        webbrowser.open("https://mangadex.com")
    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = musiclb.music.get(song, "")
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find the song.")
    elif "say hello" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])
                for article in articles[:5]:  # Limit to top 5 articles
                    speak(article["title"])
            else:
                speak("Sorry, unable to retrieve news at this time.")
        except requests.exceptions.RequestException as e:
            speak(f"Error: {str(e)}")

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    recognizer = sr.Recognizer()

    while True:
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("listening..!")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Hello sir")
                    speak("Say the command..!")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    sayCommand(command)
        
      
        except sr.UnknownValueError:
            print("jarvis could not understand audio")
        except sr.WaitTimeoutError:
            print("Listening timed out, please try again.")
