#!/usr/bin/python3.11
import fitz
import io
from PIL import Image
import os, sys

def main(file):
	try:
		pdf_file = fitz.open(file)
		exportPath = f"{os.path.dirname(os.path.abspath(file))}/{file.split('/')[-1]}_EXTRACTED_IMAGES"	
		flagged = True
		for iPage in range(len(pdf_file)):
			page = pdf_file[iPage] 
			if page.get_images():
				if flagged:
					print(f"[*] Any found image be extracted to {exportPath.split('/')[-1]}")
					flagged = False

				print(f"[*] Found a total of {len(page.get_images())} images in page {iPage+1}")
				
				if not os.path.exists(exportPath):
					os.mkdir(exportPath)
			else: 
				print(f"[!] No images found on page {iPage+1}")
			x=0
			for iImage, img in enumerate(page.get_images(), start=1):
				bImage = pdf_file.extract_image(img[0])
				rawImageBytes = bImage["image"] 
				imgExt = bImage["ext"]

				with open(f"{exportPath}/img_{x}.{imgExt}", "wb") as fs:
					fs.write(rawImageBytes)
				
				x+=1

	except:
		print(f"[!] Error opening the file")

if __name__ == "__main__":
	if len(sys.argv) == 2:
		if os.path.exists(sys.argv[1]):
			main(sys.argv[1])
		else:
			print(f"[!] File does not exist")
	else:
		print(f"[!] Pass .pdf file as an argument")
