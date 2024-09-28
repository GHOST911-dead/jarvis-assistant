
Jarvis - Your Personal Assistant

Jarvis is a voice-activated personal assistant designed to perform various tasks, from web series recommendations to battery monitoring. Built using Python, Jarvis leverages libraries like pyttsx3 for text-to-speech, speech recognition for voice commands, and various APIs for enhanced functionality.

Features

- Voice Recognition: Responds to voice commands using speech recognition.
- Web Series Suggestions: Recommends a random web series along with its plot summary.
- Battery Monitoring: Notifies the user when the battery percentage drops below a certain threshold.
- Application Launcher: Opens common applications like Notepad, Calculator, and web browsers.
- Joke Fetcher: Retrieves a random joke from an online API.
- Folder Creator: Creates directories as per user input.
- API Interaction: Allows users to post data to a sample API.

Tools & Technologies

- Python
- pyttsx3
- SpeechRecognition
- Wikipedia API
- requests
- pandas
- WMI (Windows Management Instrumentation)
- JSON handling

Installation Instructions

Prerequisites

Make sure you have Python installed on your system. You can download it from python.org.

Step-by-Step Installation

1. Clone the repository:

   git clone https://github.com/yourusername/jarvis.git
   cd jarvis

2. Install the required libraries:

   pip install pyttsx3 SpeechRecognition wikipedia-api requests pandas wmi

3. Ensure you have the necessary permissions to access your microphone for voice commands.

4. Run the main script:

   python jarvis.py
