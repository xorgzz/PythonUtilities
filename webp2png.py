#!/usr/bin/python3

import os
from PIL import Image

def webp2png(webp, png):
    webp_image = Image.open(webp)
    png_image = webp_image.convert("RGBA")
    png_image.save(png)


def processData():
    pwd = os.getcwd()
    print(f"[*] Processing data in {pwd} [*]")
    if not (os.path.isdir(f"{pwd}/PNGED-{pwd.split('/')[-1]}")):
        os.mkdir(f"{pwd}/PNGED-{pwd.split('/')[-1]}")
    if not (os.path.isdir(f"{pwd}/WEBPED-{pwd.split('/')[-1]}")):
        os.mkdir(f"{pwd}/WEBPED-{pwd.split('/')[-1]}")
    webpPath = f"{pwd}/WEBPED-{pwd.split('/')[-1]}"
    outPath = f"{pwd}/PNGED-{pwd.split('/')[-1]}"
    for file in os.listdir():
        if (file.split('.')[-1] == "webp"):
            webp2png(file, f"{outPath}/{'.'.join(file.split('.')[0:-1])}.png")
            #os.system(f"ffmpeg -loglevel quiet -i \"{file}\" {outPath}/{'.'.join(file.split('.')[0:-1])}.png")
            os.system(f"mv \"{file}\" WEBPED-*")
    print("\t[*] End report [*]")
    print(f"WEBP files processed: {len(os.listdir(outPath))} = {len(os.listdir(outPath))/len(os.listdir(webpPath))*100}%")


def main():
    files = os.listdir()
    for i in range(len(files)):
        if (files[i].split('.')[-1] == "webp"):
            processData()
            break
    return
    
if __name__ == "__main__":
    main()
