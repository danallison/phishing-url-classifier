import os
import requests

def fetch_phishtank_csv():
    '''
    Download the latest phishing URLs from phishtank.com
    '''
    api_key = os.environ['PHISHTANK_API_KEY']
    url = f'https://data.phishtank.com/data/{api_key}/online-valid.csv.gz'
    response = requests.get(url)
    with open('/usr/src/app/data/phishtank.csv.gz', 'wb') as file:
        file.write(response.content)
