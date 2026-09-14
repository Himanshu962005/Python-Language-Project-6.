# Python-Language-Project-6.
## 1.Project - Artificial Intelligence Voice Assistant 🎙️.
**A desktop voice assistant built in Python that listens for a wake word, understands spoken commands, and responds using both rule-based actions and AI-powered conversation. Inspired by assistants like Alexa and Google Assistant, Jarvis can open websites, play music, read news headlines, and answer general questions using OpenAI's language model.**

**The project combines speech recognition, text-to-speech, and natural language processing into a single voice-controlled workflow. It listens continuously for the wake word "Jarvis," then activates to process a command — either handling it directly (opening a site, playing a song, fetching news) or forwarding it to an AI model for a conversational response, which is then spoken back to the user.**

**This assistant helps strengthen core Python skills by combining multiple real-world libraries and APIs — audio input/output, web automation, external API integration, and AI completions — into one cohesive application. Perfect for beginners and Python developers who want hands-on experience building voice-driven applications.**

### 🚀 Features
* Wake Word Detection ("Jarvis").
* Voice Command Recognition using Google Speech Recognition.
* Text-to-Speech Responses (gTTS + Pygame playback).
* Open Websites by Voice (Google, YouTube, Facebook, LinkedIn).
* Play Songs from a Custom Music Library.
* Fetch and Read Out Latest News Headlines.
* AI-Powered Conversational Responses via OpenAI's GPT Model.
* Modular Codebase with Separate Music Library File.

### 🛠️ Tech Stack
* 🔸 Python 3.
* 🔸 OpenAI API (GPT-3.5-Turbo).
* 🔸 SpeechRecognition.
* 🔸 gTTS (Google Text-to-Speech).
* 🔸 Pygame (Audio Playback).
* 🔸 Requests (News API Integration).
* 🔸 pyttsx3 (Offline TTS fallback).

### 📂 Project Structure
```
├── Jarvis.py          # Main assistant loop — wake word detection & command processing
├── Client.py           # Standalone OpenAI API usage example
├── MusicLibrary.py      # Dictionary of songs mapped to YouTube links
```

### ⚙️ How It Works
1. The assistant continuously listens through the microphone for the wake word **"Jarvis"**.
2. Once triggered, it listens for a follow-up voice command.
3. The command is matched against predefined actions (open website, play song, fetch news).
4. If no predefined action matches, the command is sent to OpenAI's GPT model for a conversational reply.
5. The response is converted to speech and played back to the user.

### 📌 Setup
1. Install the required dependencies:
   ```
   pip install openai speechrecognition pyttsx3 gTTS pygame requests pocketsphinx
   ```
2. Add your OpenAI API key in `Jarvis.py` and `Client.py`.
3. Add your NewsAPI key in `Jarvis.py`.
4. Run the assistant:
   ```
   python Jarvis.py
   ```

### 📌 Purpose
This project was created for learning and improving Python development skills by building a real-world voice assistant with a strong focus on API integration, audio processing, and combining rule-based logic with AI-powered responses.
