from gtts import gTTS
import base64
import io
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

app = Flask(__name__)
CORS(app)


def scrape_and_summarize(url):
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        h1_tags = soup.find_all('h1')
        h1_combined_string = ' '.join([str(tag.text) for tag in h1_tags])

        h2_tags = soup.find_all('h2')
        h2_combined_string = ' '.join([str(tag.text) for tag in h2_tags])

        p_tags = soup.find_all('p')
        p_combined_string = ' '.join([str(tag.text) for tag in p_tags])
    else:
        return "We cannot get the summery from this website please try from a different website."
    # Placeholder logic for scraping and summarization

    fullText = h1_combined_string + " " + h2_combined_string + " " + p_combined_string  #

    summary = summarizer(fullText, max_length=130, min_length=50, do_sample=False)

    b = summary[0]  # type: ignore
    c = b['summary_text']  # type: ignore
    return c


@app.route('/a', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        url = data['url']

        # Call the function to scrape and summarize
        summary = scrape_and_summarize(url)

        tts = gTTS(text=summary, lang='en')
        audio_stream = io.BytesIO()
        tts.write_to_fp(audio_stream)

        # Encode the BytesIO content in base64
        ttsEncodedAudio = base64.b64encode(audio_stream.getvalue()).decode('utf-8')

        # Respond with the summary
        response_data = {'summary': summary, 'audio': ttsEncodedAudio}
        return jsonify(response_data)

    except Exception as e:
        return jsonify({'err3or': str(e)}), 500


# if __name__ == '__main__':

import base64

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
app.run(debug=True)
