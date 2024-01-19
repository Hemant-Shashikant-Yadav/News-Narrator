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
            print(f'{i+1} {voice.name} ({voice.id})')
    
    def text_to_speech(self, text: str, save: bool = False, file_name='output.mp3'):
        self.engine.say(text)
        time.sleep(1)  # Introduce a 2-second break
        self.engine.stop()  # Stop the speech
        print("Talking")
        
        if save:
            self.engine.save_to_file(text, file_name)
            self.engine.runAndWait()
        else:
            self.engine.runAndWait()


if __name__ == '__main__':
    # Use the name of the voice as a string
    tts = TextToSpeech("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0", 130, 1.5)
    tts.list_available_voices()
    tts.text_to_speech('''Renewable energy, notably solar and wind power, plays a pivotal role globally in the shift toward sustainable energy solutions. These technologies offer a clean alternative to fossil fuels, converting sunlight and wind into electricity through solar panels and turbines. The widespread adoption of renewables not only mitigates environmental impact but also boosts energy independence and resilience. Governments, businesses, and individuals are increasingly recognizing the urgency of transitioning to combat climate change. This transition involves technological advancements, such as energy storage innovations and smart grid technologies, addressing challenges associated with intermittent renewable sources. Economic benefits, including job creation and decreasing technology costs, underscore the feasibility of investing in renewable energy. Governments worldwide are implementing supportive policies and incentives to accelerate adoption, fostering a commitment to combat climate change and build a sustainable energy future.''', save=True, file_name='output.mp3')
