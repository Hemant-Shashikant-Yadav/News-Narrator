from gtts import gTTS
from pydub import AudioSegment

# Your text
text = """ Renewable energy sources, such as solar and wind power, have emerged as pivotal components in the global shift toward sustainable and environmentally friendly energy solutions. Harnessing the inexhaustible power of the sun and the relentless force of the wind, these technologies offer a clean alternative to traditional fossil fuels. Solar panels convert sunlight into electricity, and wind turbines harness kinetic energy from the wind to generate power. The widespread adoption of renewable energy not only mitigates the environmental impact associated with conventional energy sources but also contributes to energy independence and resilience. Governments, businesses, and individuals worldwide are increasingly recognizing the imperative of transitioning to renewable energy to combat climate change and ensure a sustainable future. 
This transition to renewable energy is accompanied by rapid technological advancements and a growing emphasis on energy efficiency. Innovations in energy storage solutions, such as advanced batteries, play a crucial role in addressing the intermittent nature of renewable sources, ensuring a reliable and consistent power supply. Additionally, smart grid technologies enable efficient energy distribution and consumption, optimizing the integration of renewables into existing energy infrastructures. The economic benefits of investing in renewable energy are also becoming evident, as job creation in the green energy sector expands and the costs of renewable technologies continue to decrease. Governments worldwide are implementing supportive policies and incentives to accelerate the adoption of renewable energy, fostering a global commitment to combat climate change and build a sustainable energy future for generations to come
"""


# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine
tts = gTTS(text=text, lang=language, slow=False)

# Save the converted audio to a file
tts.save("output.mp3")

# Load the audio file
audio = AudioSegment.from_mp3("output.mp3")

# Modify pitch using pydub
pitch_factor = 1.5  # You can adjust this value to change the pitch
output_with_pitch = audio.speedup(playback_speed=pitch_factor)

# Export the modified audio to a file
output_with_pitch.export("output_with_pitch.mp3", format="mp3")

