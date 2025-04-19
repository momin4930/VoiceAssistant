# 🎙️ Maximus - Your Personal AI Voice Assistant

Maximus is a Python-based voice assistant designed to make your everyday tasks more fun and hands-free! Whether you want to create a note, manage your to-dos, hear a joke, or play a game, Maximus is here to help — with voice input and speech output.

## 🧠 Features

### ✅ General Capabilities
- **Voice Activation**: Responds to spoken commands using `speech_recognition`.
- **Text-to-Speech**: Talks back using `pyttsx3` with a customizable male voice.
- **Smart Greeting**: Welcomes you with personalized messages.

### 📝 Task & Note Management
- **Create a Note**: Speak your note, and Maximus will save it in `notes.txt`.
- **To-do List**:
  - Add items by voice.
  - View the current to-do list.
  - Data is saved persistently in `todos.txt`.

### 😂 Fun & Entertainment
- **Jokes**: Pulls a random joke from `jokes.txt`.
- **Quotes**: Inspires you with a quote from `quotes.txt`.
- **Facts**: Shares a random interesting fact from `facts.txt`.

### 🎮 Games
- **Guessing Game**: Try to guess a number Maximus is thinking of (1–10).
- **Rock-Paper-Scissors**: Classic game played via voice commands.

### 📚 Storytelling
- **Random Stories**: Listen to short, fun stories from Maximus.

### 😊 Mood Checker
- **Emotional Interaction**: Asks how you're feeling and responds appropriately.
  - If you're sad, Maximus might cheer you up with a joke!

### 🚪 Exit Command
- **Quit Program**: Say "exit", "quit", or "bye" to close Maximus.

---

---

## 🛠️ Requirements

- Python 3.7+
- Microphone

### 📦 Dependencies

Install all required packages using:

```bash
pip install speechrecognition pyttsx3 nltk

