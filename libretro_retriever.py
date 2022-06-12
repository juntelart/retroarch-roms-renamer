import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

class Libretro_retriever:

    def execute(self, url):
        try:
            response = requests.get(url)
            if not response.ok:
                print("Error connectirng to thumbails url")
                sys.exit()
            
            html = BeautifulSoup(response.text, 'html.parser')
            links = html.find_all('a')
            libretro_names = dict()
            for link in links:
                name = unquote(link['href'])
                name_without_extension = name.split(".png")[0]
                key = name_without_extension.split("(")[0].strip().lower()
                libretro_names[key] = name_without_extension
            return libretro_names
        except requests.exceptions.ConnectionError as exc:
            return dict()