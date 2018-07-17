import os
import requests
from hashlib import md5

def fetch_phishtank_csv():
    '''
    Download the latest phishing URLs from phishtank.com
    '''
    api_key = os.environ['PHISHTANK_API_KEY']
    url = f'https://data.phishtank.com/data/{api_key}/online-valid.csv.gz'

    print('fetching file from phishtank.com')
    response = requests.get(url)

    # Phishtank updates their data every hour, so we include
    # in the filename the md5 hash of the contents as a way
    # of versioning the data.
    file_hash = md5(response.content).hexdigest()
    file_path = f'/usr/src/app/data/phishtank-{file_hash}.csv.gz'

    with open(file_path, 'wb') as file:
        print(f'saving file to {file_path}')
        file.write(response.content)
    print('done')
