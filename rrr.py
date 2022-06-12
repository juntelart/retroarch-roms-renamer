import sys
import os
from libretro_retriever import Libretro_retriever
from file_renamer import File_renamer

def show_error(message):
    print(message);
    print("Usage: python3 " + sys.argv[0] + " \"http://url-to-thumbnails\" \"/local/path/to/files\" \".ext\"")
    print("E.g. python3 " + sys.argv[0] + " \"http://thumbnails.libretro.com/Nintendo%20-%20Nintendo%20Entertainment%20System/Named_Boxarts/\" \"/media/r/USB/roms/Nintendo Entertainment System\" \".nes\"")

params_count = len(sys.argv)

if params_count != 4:
    show_error("Error: Missing parameters")
    sys.exit()

url = sys.argv[1]
path = sys.argv[2]
extension = sys.argv[3]

if not os.path.isdir(path):
    show_error("Local path doesn't exist")
    sys.exit()

libretro_names = Libretro_retriever().execute(url)

print("Renaming files...")
renamed_files_count = File_renamer().execute(libretro_names, path, extension)
print("Renamed " + str(renamed_files_count) + " files")
