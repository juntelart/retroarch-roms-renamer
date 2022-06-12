import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import glob
import os
import re

params_count = len(sys.argv)

if params_count != 4:
    print("Error: Missing parameters");
    print("Usage: python3 " + sys.argv[0] + " \"http://url-to-thumbnails\" \"/local/path/to/roms\" \".ext\"")
    print("E.g. python3 " + sys.argv[0] + " \"http://thumbnails.libretro.com/Nintendo%20-%20Nintendo%20Entertainment%20System/Named_Boxarts/\" \"/media/r/USB/roms/Nintendo Entertainment System\" \".nes\"")
    sys.exit()

url = sys.argv[1]
path = sys.argv[2]
rom_extension = sys.argv[3]

if not os.path.isdir(path):
    print("Local path doesn't exist")
    print("Usage: python3 " + sys.argv[0] + " \"http://url-to-thumbnails\" \"/local/path/to/roms\" \".ext\"")
    print("E.g. python3 " + sys.argv[0] + " \"http://thumbnails.libretro.com/Nintendo%20-%20Nintendo%20Entertainment%20System/Named_Boxarts/\" \"/media/r/USB/roms/Nintendo Entertainment System\" \".nes\"")
    sys.exit()

try:
    print("Retrieving libretro names...")
    response = requests.get(url)
    if not response.ok:
        print("Error connectirng to thumbails url")
        sys.exit()
    
    html = BeautifulSoup(response.text, 'html.parser')
    links = html.find_all('a')
    libretroNames = dict()
    for link in links:
        name = unquote(link['href'])
        name_without_extension = name.split(".png")[0]
        key = name_without_extension.split("(")[0].strip().lower()
        libretroNames[key] = name_without_extension
except requests.exceptions.ConnectionError as exc:
    print("Error connectirng to thumbails url")
    sys.exit()

os.chdir(path)

print("Renaming files...")
renamed_files_count = 0
for file in glob.glob("*" + rom_extension):
    file_without_extension = file.split(rom_extension)[0]
    forbidden_characters = r'[&*/:`<>?\|]'
    clean_file_name = re.sub(forbidden_characters, '_', file_without_extension)

    if (clean_file_name != file_without_extension):
        print("Forbidden character detected. Renaming...")
        os.rename(file_without_extension + rom_extension, clean_file_name + rom_extension)    

    key = file_without_extension.split("(")[0].strip().lower()
    if key in libretroNames:
        rightName = libretroNames[key] + rom_extension
        if (file != rightName):
            print(file + " -> " + rightName)
            renamed_files_count+=1
            os.rename(clean_file_name + rom_extension, rightName)

print("Renamed " + str(renamed_files_count) + " files")

