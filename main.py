import speech_recognition as sr
import pyttsx3 as tts
import os
import sys
import time  
from nltk.tokenize import word_tokenize

# Initialize speech recognizer and speaker
recognizer = sr.Recognizer()
speaker = tts.init()

# SET MALE VOICE 
voices = speaker.getProperty('voices')
for voice in voices:
    if "male" in voice.name.lower() or "david" in voice.name.lower():
        speaker.setProperty('voice', voice.id)
        break

speaker.setProperty('rate', 170)

# Persistent to-do list
TODO_FILE = "todos.txt"
todo_list = []

# Load todos from file
if os.path.exists(TODO_FILE):
    with open(TODO_FILE, 'r') as f:
        todo_list = [line.strip() for line in f.readlines()]

def save_todos():
    with open(TODO_FILE, 'w') as f:
        for item in todo_list:
            f.write(f"{item}\n")

def speak(text):
    """Safe speaking function with error handling"""
    try:
        speaker.say(text)
        speaker.runAndWait()
        time.sleep(0.3) 
    except Exception as e:
        print(f"Speech error: {e}")

def greet1():
    speak("I am Maximus! How can I help?")

def greet2():
    speak("O hey there, Hope you are having a wonderful day, How can I help?")

def create_note():
    try:
        speak("What should the note say?")

        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic, timeout=5)
            note = recognizer.recognize_google(audio)
            print(f"Note: {note}")


        with open(f"notes.txt", 'w') as f:
            f.write(note)

        speak(f"Note saved as notes")

    except Exception as e:
        print(f"ERROR in create_note: {e}")
        speak("Sorry, I couldn't create the note. Please try again.")

def add_todo():
    try:
        speak("What should I add to your to-do list?")

        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic, timeout=5)
            item = recognizer.recognize_google(audio)
            print(f"Adding todo: {item}")

        todo_list.append(item)
        save_todos()

        speak(f"Added: {item}")

    except Exception as e:
        print(f"ERROR in add_todo: {e}")
        speak("Sorry, I didn't catch that. Please try again.")

def show_todos():
    if not todo_list:
        speak("Your to-do list is empty!")
    else:
        speak(f"You have {len(todo_list)} items:")
        for i, item in enumerate(todo_list, 1):
            speak(f"Item {i}: {item}")
            print(f"Todo {i}: {item}")

def quit_program():
    speak("Goodbye!")
    sys.exit(0)

def intent_classifier(message):
    try:
        print(f"User said: {message}")
        tokens = word_tokenize(message.lower())

        if any(word in tokens for word in ["hello", "hi", "hey"]):
            greet2()
        
        elif "note" in tokens and any(word in tokens for word in ["create", "make", "write"]):
            create_note()
        
        elif any(word in tokens for word in ["todo", "task", "reminder", "list"]):
            if any(word in tokens for word in ["add", "new", "create", "insert"]):
                add_todo()
            elif any(word in tokens for word in ["show", "read", "tell", "what"]):
                show_todos()
        
        elif any(word in tokens for word in ["bye", "exit", "quit"]):
            quit_program()
        
        else:
            speak("I didn't understand. Try saying 'add a task' or 'show my task' or 'create a new note'.")

    except Exception as e:
        print(f"ERROR in intent_classifier: {e}")
        speak("Sorry, I encountered an error. Please try again.")

def main():
    greet1()
    print("I am Maximus! How can I help?")
    
    while True:
        try:
            with sr.Microphone() as mic:
                print("\nListening... (say 'exit' to quit)")
                recognizer.adjust_for_ambient_noise(mic, duration=0.5)
                audio = recognizer.listen(mic, timeout=5, phrase_time_limit=8)
                
                message = recognizer.recognize_google(audio)
                print(f"Recognized: {message}")
                
                intent_classifier(message)

        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
        except Exception as e:
            print(f"Main loop error: {e}")
            speak("Something went wrong. Let's try again.")

if __name__ == "__main__":
    try:
        word_tokenize("test")
    except:
        import nltk
        nltk.download('punkt')
    
    main()
