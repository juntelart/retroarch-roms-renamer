# Retroarch ROMs Renamer

It's a little script to rename roms according to libretro names convenion for that the thmbnails download feature match with correct thumbnail

## STEPS

### Clone this repository

```bash
git clone https://github.com/juntelart/retroarch-roms-renamer.git
cd retroarch-roms-renamer
```

### Check libretro thumbnails URL
Go to http://thumbnails.libretro.com/ Just check what is a libretro thumbnails url (You can use Boxarts folder or Snaps or Titles), for example for NES:

http://thumbnails.libretro.com/Nintendo%20-%20Nintendo%20Entertainment%20System/Named_Boxarts/

### Execute script

To execute script you shouls to pass 3 params. We recommend make backup of your folder firstly:
* Libretro thumbnails URL (http://thumbnails.libretro.com/[system]/Named_Boxarts/)
* Local ROMs path (E.g. /media/user/roms/Nintendo Entertainment System)
* ROMs extension (E.g. .nes)
  
Example (for NES):
```bash
python3 rrr.py "http://thumbnails.libretro.com/Nintendo%20-%20Nintendo%20Entertainment%20System/Named_Boxarts/" "/media/user/roms/Nintendo Entertainment System" ".nes"