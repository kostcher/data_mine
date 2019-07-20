import errno
import os
import random
import time
from http import HTTPStatus

import requests


def file_put_content(path, data):
    if path.find('/') != -1:
        os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)

URL = 'https://icobench.com/icos'
STOP_ON = '<div class="no_data">'
START_PAGE = 1
SAVE_DIR = 'pages/'

site_data = requests.get(URL)

current_page = START_PAGE

while True:
    print(f'Start parse page №{current_page}')

    params = {
        'page': current_page
    }

    site_data = requests.get(URL, params=params)

    if site_data.status_code != HTTPStatus.OK:
        break

    site_data_source = site_data.text

    if site_data_source.find(STOP_ON) != -1:
        print(f'Finish on page №{current_page}')
        break

    file_put_content(SAVE_DIR + f'icobench_page_{current_page}.html', site_data_source)

    current_page += 1

    time.sleep(random.randint(1, 3))
