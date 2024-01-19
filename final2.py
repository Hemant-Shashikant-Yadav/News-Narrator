import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news/world-asia-india-67770036'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    h1_tags = soup.find_all('h1')

    h1_combined_string = ' '.join([str(tag.text) for tag in h1_tags])


    p_tags = soup.find_all('p')

    p_combined_string = ' '.join([str(tag.text) for tag in p_tags])

    final = h1_combined_string+ p_combined_string
    print(final)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print("\n\n\n\n\n\n\n\n")
finalll = summarizer(final, max_length=130, min_length=30, do_sample=False)
print(finalll)
print(type(finalll))



import pyttsx3
import time


class TextToSpeech:
    engine: pyttsx3.Engine
    def __init__(self, voice, rate: int, volume: float):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)

        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def list_available_voices(self):
        voices = self.engine.getProperty('voices')

        for i, voice in enumerate(voices):
            print(f'{i + 1} {voice.name} ({voice.id})')

    def text_to_speech(self, text: str, save: bool = False, file_name='op111.mp3'):
        self.engine.say(text)
        print("\n\n\n\n\n\n\n\n")


        if save:
            self.engine.save_to_file(text, file_name)
            self.engine.runAndWait()
        else:
            self.engine.runAndWait()

tts = TextToSpeech("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0", 130, 1.5)
tts.text_to_speech(finalll, save=True, file_name='output.mp3')

