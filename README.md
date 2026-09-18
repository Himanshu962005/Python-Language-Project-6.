# Python-Language-Project-6.
## 1. Project - Artificial Intelligence Voice Assistant 🎙️.
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
3. Add your OpenAI API key in `Jarvis.py` and `Client.py`.
4. Add your NewsAPI key in `Jarvis.py`.
5. Run the assistant:
   ```
   python Jarvis.py
   ```

### 📌 Purpose
This project was created for learning and improving Python development skills by building a real-world voice assistant with a strong focus on API integration, audio processing, and combining rule-based logic with AI-powered responses.

## 2. Project - Auto Reply AI Chatbot 🤖.
**A Python-only chatbot web app built with Streamlit. It works instantly in demo mode with no setup required, and can be upgraded to real AI-powered replies by adding any OpenAI-compatible API key. Designed as a lightweight, ready-to-deploy customer support assistant.**

**The project combines a Streamlit chat UI with a simple, dependency-free API client written using Python's standard library. It listens for user messages in a chat window, checks whether an API key is configured, and either generates a rule-based demo reply or forwards the conversation to an OpenAI-compatible chat completion endpoint for a real AI response.**

**This assistant helps strengthen core Python skills by combining a modern web UI framework, HTTP requests without external libraries, session state management, and API integration into one cohesive application. Perfect for beginners and Python developers who want hands-on experience building and deploying AI-powered chat apps.**

### 🚀 Features
* Instant Demo Mode — works with zero configuration, no API key required.
* Real AI Replies via any OpenAI-compatible Chat Completions API.
* Streamlit Chat UI with Persistent Session History.
* Configurable Model & API Base URL (supports OpenAI, local models, and other compatible providers).
* Custom Assistant Instructions (editable system prompt).
* Clear Conversation Button.
* Friendly Error Handling for invalid keys, network failures, and provider errors.
* Zero Third-Party HTTP Dependencies — uses Python's built-in `urllib`.

### 🛠️ Tech Stack
* 🔸 Python 3.10+.
* 🔸 Streamlit (Chat UI & Session State).
* 🔸 urllib (Standard Library HTTP Requests).
* 🔸 OpenAI-Compatible Chat Completions API.

### 📂 Project Structure

```
├── app.py              # Main Streamlit app — chat UI, demo mode & AI reply logic
├── requirements.txt     # Python dependencies
├── .env.example         # Reference for optional environment variables
├── .gitignore           # Ignores .venv, .env, and cache files
```

### ⚙️ How It Works
1. The app opens a Streamlit chat window and displays the conversation history.
2. When the user sends a message, it is added to the session state and shown on screen.
3. If no API key is configured, the app replies using simple rule-based demo logic.
4. If an API key is provided in the sidebar (or via secrets/environment variables), the full conversation is sent to the configured OpenAI-compatible endpoint.
5. The AI's response is displayed in the chat window and saved to the session history.

### 📌 Setup
1. Install Python 3.10 or newer and make sure it's added to PATH.
2. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install the required dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the chatbot:
   ```powershell
   streamlit run app.py
   ```
5. (Optional) Add your API key in the sidebar, or set it as an environment variable before running:
   ```powershell
   $env:OPENAI_API_KEY = "your_api_key_here"
   streamlit run app.py
   ```

### 📌 Purpose
**This project was created for learning and improving Python development skills by building a real-world, deployable AI chatbot with a strong focus on web UI development, API integration, and writing clean, dependency-light HTTP client code.**
