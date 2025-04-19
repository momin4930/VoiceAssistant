import speech_recognition as sr
import pyttsx3 as tts
import os
import sys
import time
import random
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

speaker.setProperty('rate', 165)
speaker.setProperty('volume', 0.9)

# Persistent to-do list
TODO_FILE = "todos.txt"
todo_list = []

# External files for jokes, quotes, and facts
JOKES_FILE = "jokes.txt"
QUOTES_FILE = "quotes.txt"
FACTS_FILE = "facts.txt"

def load_file_lines(filename):
    """Load lines from a file, return empty list if file doesn't exist."""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

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
    print("I am Maximus! How can I help?")

def greet2():
    speak("O hey there, Hope you are having a wonderful day, How can I help?")
    print("O hey there, Hope you are having a wonderful day, How can I help?")

def create_note():
    try:
        speak("What should the note say?")
        print("What should the note say?")

        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic, timeout=5)
            note = recognizer.recognize_google(audio)
            print(f"Note: {note}")

        with open(f"notes.txt", 'w') as f:
            f.write(note)

        speak(f"Note saved as notes")
        print(f"Note saved as notes")

    except Exception as e:
        print(f"ERROR in create_note: {e}")
        speak("Sorry, I couldn't create the note. Please try again.")

def add_todo():
    try:
        speak("What should I add to your to-do list?")
        print("What should I add to your to-do list?")

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
        print("Your to-do list is empty!")
    else:
        speak(f"You have {len(todo_list)} items:")
        for i, item in enumerate(todo_list, 1):
            speak(f"Item {i}: {item}")
            print(f"Todo {i}: {item}")

def tell_joke():
    jokes = load_file_lines(JOKES_FILE)
    if jokes:
        joku=random.choice(jokes)
        speak(joku)
        print(joku)
    else:
        speak("Sorry, I don't have any jokes right now.")
        print("Sorry, I don't have any jokes right now.")

def tell_quote():
    quotes = load_file_lines(QUOTES_FILE)
    if quotes:
        qutoess=random.choice(quotes)
        speak(qutoess)
        print(quotes)
    else:
        speak("I don't have any quotes right now.")
        print("I don't have any quotes right now.")

def tell_fact():
    facts = load_file_lines(FACTS_FILE)
    if facts:
        factos=random.choice(facts)
        speak(factos)
        print(factos)
    else:
        speak("I don't have any facts right now.")
        print("I don't have any facts right now.")

def play_guessing_game():
    speak("I'm thinking of a number between 1 and 10. Can you guess it?")
    print("I'm thinking of a number between 1 and 10. Can you guess it?")
    number = random.randint(1, 10)
    
    for attempt in range(3):
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.5)
                audio = recognizer.listen(mic, timeout=5)
                guess = int(recognizer.recognize_google(audio))
                
                if guess == number:
                    speak("Wow, you got it right!")
                    print("Wow, you got it right!")
                    return
                elif guess < number:
                    speak("Too low!")
                    print("Too low!")
                else:
                    speak("Too high!")
                    print("Too high!")
        except:
            speak("Sorry, I didn't catch that. Try again.")
    
    speak(f"Game over! The number was {number}.")

def play_rps():
    speak("Let's play Rock, Paper, Scissors! Say your choice.")
    print("Let's play Rock, Paper, Scissors! Say your choice.")
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic, timeout=5)
            user_choice = recognizer.recognize_google(audio).lower()
            
            if user_choice not in choices:
                speak("Invalid choice. Try rock, paper, or scissors.")
                return
            
            speak(f"You chose {user_choice}, I chose {computer_choice}.")
            
            if user_choice == computer_choice:
                speak("It's a tie!")
                print("It's a tie!")
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "paper" and computer_choice == "rock") or \
                 (user_choice == "scissors" and computer_choice == "paper"):
                speak("You win!")
                print("You win!")
            else:
                speak("I win!")
                print("I win!")
    except:
        speak("Sorry, I didn't understand. Let's try again later.")

def tell_story():
    stories = [
        "Once upon a time, a little robot named Maximus helped humans with their tasks. One day, he saved the world by fixing a giant computer bug!",
        "There was a wise old owl who lived in a tree. He gave great advice, but no one listened because he spoke in Python code.",
    ]
    speak(random.choice(stories))

def check_mood():
    speak("How are you feeling today?")
    print("How are you feeling today?")
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic, timeout=5)
            mood = recognizer.recognize_google(audio).lower()
            
            if any(word in mood for word in ["happy", "good", "great"]):
                speak("That's awesome! Let's make today even better!")
            elif any(word in mood for word in ["sad", "tired", "bad"]):
                speak("I’m sorry to hear that. Maybe a joke will cheer you up?")
                tell_joke()
            else:
                speak("I hope you have a fantastic day!")
    except:
        speak("I couldn't hear you, but I hope you're doing well!")

def quit_program():
    speak("Goodbye!")
    print("Goodbye!")
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
        
        elif any(word in tokens for word in ["joke", "funny"]):
            tell_joke()
        
        elif any(word in tokens for word in ["quote", "inspiration"]):
            tell_quote()
        
        elif any(word in tokens for word in ["fact", "interesting"]):
            tell_fact()
        
        elif any(word in tokens for word in ["game", "play", "guess"]):
            if "guess" in tokens:
                play_guessing_game()
            elif any(word in tokens for word in ["rock", "paper", "scissors"]):
                play_rps()
        
        elif any(word in tokens for word in ["story", "tell me a story"]):
            tell_story()
        
        elif any(word in tokens for word in ["mood", "how are you", "feeling"]):
            check_mood()
        
        elif any(word in tokens for word in ["bye", "exit", "quit"]):
            quit_program()
        
        else:
            speak("I didn't understand. Try saying 'tell me a joke', 'play a game', or 'add a task'.")

    except Exception as e:
        print(f"ERROR in intent_classifier: {e}")
        speak("Sorry, I encountered an error. Please try again.")

def main():
    greet1()
    
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
            print("I didn't hear anything. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            print("Sorry, I didn't understand that.")
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
