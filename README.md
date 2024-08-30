# Desk_Duck

<img width="581" alt="Screenshot 2024-08-22 at 7 03 17 PM" src="https://github.com/user-attachments/assets/58215b06-403e-4dd9-aa21-2d56e7787d67">

An ai chatbot to serve as a "rubber duck" for when you're stuck on a project.

## Summary

Desk Duck aims to be a an AI Assistant to help with programming. You can ask it about various programming questions. It is designed to help get over coding hurdles by helping you think through problems and get over errors faster.  Desk Duck uses webcam capabilities to track user's eye contact and begins listening upon contact. It is voice operated and outputs audio and to command line. It uses stt (speech to text) to accept user input and tts (text to speech) to output an answer. In it's current iteration it does not yet interact with the code directly. We are aiming to add that in the future.

## Instructions

### Installation

- Clone or Download the repo
- Install dependencies using req.txt or mac_req.txt
- Create and update a `.env` file bassed on `sample.env`

### Running the project

- In terminal, change directories to `desk_duck/app`
- Run `python main.py` to start the program

### Useage

- Look at your camera to trigger voice recognition
- Speak clearly and ask your programming related question
- Say stop or shutup to stop the app from listening and answering (future - iteration)

## Dependencies

- VS Code
- API Key - https://platform.openai.com/docs/overview
- ChatGPT account

### Windows

- Windows 10 or later
- From the root directory in terminal execute `pip install -r req.txt`

### Mac os

- OSX 13 (Ventura) or later
- From the root directory in terminal execute `pip install -r mac_req.txt`
#### Trouble shooting

*some users needed to install additional dependancies using Homebrew*

```
xcode-select --install
brew remove portaudio
brew install portaudio
pip3 install pyaudio
```

## Contributors

- Timothy Heidcamp
- Ethan Mcmanus
- Duane Anglin
- Daraun Prince
- Matilda Wang
- Shephali Dubey

## Presentation
https://youtu.be/jttEAuCHjto?si=bXJqBI2XHtUkdck6

## Sources:
https://github.com/amitt1236/Gaze_estimation/blob/master/gaze.py
https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
ChatGPT

