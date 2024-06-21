from os import listdir

from PIL import Image
img = Image.open(f"photo_5454194002032190823_y.jpg")
img.load()
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#text = pytesseract.image_to_string(img, lang="eng+rus")
#print(text)
#text = pytesseract.image_to_string(img, lang="eng+rus")
#print(text)

folder = "photos"
rendered_photos = dict()

for filename in listdir(folder):
    img = Image.open(f"{folder}/{filename}")
    img.load()

    text = pytesseract.image_to_string(img, lang="eng+rus")
    rendered_photos[text] = filename

text = input()
print(rendered_photos)
for key, value in rendered_photos.items():
    if text in key:
        print(value)
        mg = Image.open(f"{folder}/{value}")
        mg.load()
        mg.show()
