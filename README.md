# Personal-Voice-Assistant
#this is an voice assistant using python 
here's all the things mentioned what it can do 
This script is designed to act as a personal voice assistant. It can perform a variety of tasks based on voice commands given by the user. Here is a detailed breakdown of the tasks it can perform:

1. **Greeting the User**:
   - Based on the current time, the assistant can greet the user with a "Good morning!", "Good afternoon!", or "Good evening!".

2. **Opening Websites**:
   - The assistant can open YouTube, Wikipedia, or Google in a web browser if asked to do so by the user (e.g., "Open YouTube").

3. **Playing Music**:
   - The assistant can play a specific music file located at "C:/Users/pravi/Downloads/vinee-heights-126947.mp3" if asked to "open music".

4. **Telling the Time**:
   - The assistant can tell the user the current time if asked (e.g., "What is the time?").

5. **Providing Information from Wikipedia**:
   - If the user asks a question starting with "What is", the assistant will provide a brief summary from Wikipedia.

6. **Performing Calculations**:
   - The assistant can perform calculations using WolframAlpha if the user asks it to "calculate" something.

7. **General Responses**:
   - The assistant can respond to basic conversational queries like "How are you?", "Who are you?", and "Hello" or "Hi".

8. **Providing Weather Information**:
   - The assistant can provide the current weather information for a specified city using the OpenWeatherMap API (e.g., "What's the weather in [city]?").

9. **Providing News Headlines**:
   - The assistant can provide the top news headlines using the NewsAPI (e.g., "Give me the news").

10. **Setting and Showing Reminders**:
    - The assistant can set a reminder if the user asks it to "set a reminder to [task]".
    - It can also show the reminders that have been set if the user asks to "show reminders".

11. **Handling Unrecognized Commands**:
    - If the assistant does not understand the command, it will ask the user to rephrase the question.

### Usage
- The assistant uses speech recognition to listen to the user's commands.
- It uses text-to-speech to respond to the user.
- The script runs in a continuous loop, continuously listening for new commands and processing them accordingly.

### External Dependencies
- `speech_recognition` for converting speech to text.
- `pyttsx3` for converting text to speech.
- `webbrowser` for opening web pages.
- `datetime` for getting the current time.
- `wikipedia` for fetching summaries from Wikipedia.
- `wolframalpha` for performing calculations.
- `requests` for making API calls to OpenWeatherMap and NewsAPI.

