import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import argparse


def shorten_link(token, url):
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks',
                             headers = {'Authorization': f'Bearer {token}'},
                             json = {"long_url": url})
    response.raise_for_status()
    link_shorten = response.json()['link']
    return link_shorten


def count_clicks(token, bitlink):
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary',
                            headers = {'Authorization': f'Bearer {token}'},
                            params = {"units": '-1'})
    response.raise_for_status()              
    clicks_count = response.json()["total_clicks"]
    return clicks_count


def createParser():
    parser = argparse.ArgumentParser(description = "Create parser which allow us to use the entered link as an argument in command prompt")
    return parser


if __name__ == '__main__':
    load_dotenv()
    secret_token = os.getenv("BITLY_API_TOKEN")
    try:
        parser = createParser()
        parser.add_argument('link', help = 'Entered link for Bitly API')
        args = parser.parse_args()
        print(args)
        if args.link:
            your_link = args.link
        else:
            your_link = input('Input the link: ')

        check_on_bitlink = your_link.startswith("https://bit.ly")
        if check_on_bitlink:
            parsed = urlparse(your_link)
            print("Count clicks of your bitlink is", count_clicks(secret_token, f'{parsed.netloc}{parsed.path}'))
        else:
            short_link = shorten_link(secret_token,your_link)
            print('Yout bitlink is', short_link)
    except requests.exceptions.HTTPError:
        print("Your URL is not correct")

