import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Get the available voices
voices = engine.getProperty('voices')

# Print details of each voice
for index, voice in enumerate(voices):
    print(f"Voice {index}:")
    print(f"  ID: {voice.id}")
    print(f"  Name: {voice.name}")
    print(f"  Languages: {voice.languages}")
    print(f"  Gender: {voice.gender}")
    print(f"  Age: {voice.age}")
    print()
