import configparser
import os

import requests
from bs4 import BeautifulSoup

CONFIG_FILE = 'config.ini'
INPUT_DIR = 'inputs'


class AocClient:

    def __init__(self):
        os.makedirs(INPUT_DIR, exist_ok=True)

    def get_input(self, year, day):
        input_file_name = f'{INPUT_DIR}/{year}_{day}.input'

        # Return cached copy
        if os.path.isfile(input_file_name):
            with open(input_file_name, 'r') as input_file:
                return input_file.read().splitlines()

        session_cookie = self.get_session_cookie()

        print(f'Attempting to download input file for year {year} day {day}')
        response = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': session_cookie})

        if not response.status_code == 200:
            print(f'No input file for year {year} day {day}.')
            return

        input_data = response.text

        with open(input_file_name, 'w+') as input_file:
            print(f'Saving input file to `{input_file_name}`')
            input_file.write(input_data)

        return input_data.splitlines()

    def get_example(self, year, day):
        input_file_name = f'{INPUT_DIR}/{day}.example'

        # Return cached copy
        if os.path.isfile(input_file_name):
            with open(input_file_name, 'r') as input_file:
                return input_file.read().splitlines()

        try:
            downloaded = self.attempt_download_example(year, day)
            print('Found the following example input:')
            print('=====')
            for line in downloaded:
                print(line)
            print('=====')
            response = input('Is the above input correct? [Y]es use this input, [N]o I\'ll enter the input myself. ')
        except:
            print('Couldn\'t find example input for this day. Please enter it manually.')
            response = 'n'

        if response.lower() == 'y':
            example_input = downloaded
        else:
            # Prompt user for the example input
            print('Paste example input:  (Ctrl-D / Ctrl-Z to terminate)')
            example_input = []
            while True:
                try:
                    line = input()
                except EOFError:
                    break
                example_input.append(line)

        # Write it to file for next time
        with open(input_file_name, 'w+') as input_file:
            input_file.write('\n'.join(example_input))

        return example_input

    def attempt_download_example(self, year: int, day: int):
        session_cookie = self.get_session_cookie()
        response = requests.get(f'https://adventofcode.com/{year}/day/{day}', cookies={'session': session_cookie})
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find('pre').find('code').text.splitlines()

    def submit(self, year: int, day: int, part: int, answer: str):
        session_cookie = self.get_session_cookie()

        data = {
            'level': part,
            'answer': answer
        }
        response = requests.post(f'https://adventofcode.com/{year}/day/{day}/answer', cookies={'session': session_cookie}, data=data)

        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find('main').find('article').find('p').text

    @staticmethod
    def get_session_cookie():
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)

        if 'aoc' not in config or 'sessionCookie' not in config['aoc']:
            print('You\'ll need to provide your session cookie for adventofcode.com. In your webbrowser: F12 > '
                  'Storage/Application > Cookies.')
            session_cookie = input('Please enter your session cookie: ')
            config['aoc'] = {'sessionCookie': session_cookie}
            with open(CONFIG_FILE, 'w') as configFile:
                config.write(configFile)

        return config['aoc']['sessionCookie']
