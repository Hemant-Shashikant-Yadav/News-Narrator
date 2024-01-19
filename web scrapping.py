import json

import requests
from bs4 import BeautifulSoup

# URL of the blog you want to scrape
url = 'https://www.bbc.com/news/world-asia-india-67770036'

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    h1_tags = soup.find_all('h1')
    h1_combined_string = ' '.join([str(tag.text) for tag in h1_tags])

    h2_tags = soup.find_all('h2')
    h2_combined_string = ' '.join([str(tag.text) for tag in h2_tags])

    p_tags = soup.find_all('p')
    p_combined_string = ' '.join([str(tag.text) for tag in p_tags])

    data_dict = {
        'h1_tags': h1_combined_string,
        'h2_tags': h2_combined_string,
        'p_tags': p_combined_string
    }

    # Convert the dictionary to JSON
    json_data = json.dumps(data_dict, indent=2)

    # Print or save the JSON data
    print(json_data)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
