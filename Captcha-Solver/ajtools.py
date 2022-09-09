'''
https://replit.com/talk/ask/Pytesseract-Auto-Shell-Install-Package-Issue/140049

https://replit.com/@Intenzi/ClientRequested
'''
import os
def pip_in_tess():
  os.system("install-pkg tesseract-ocr")
  #os.system("pip install Pillow")
  os.system("clear")
from PIL import Image
import pytesseract
import cv2
import requests


pytesseract.pytesseract.tesseract_cmd = "tesseract"
os.environ["TESSDATA_PREFIX"] = "/home/runner/.apt/usr/share/tesseract-ocr/4.00/tessdata/"

img_folder = 'Images'
test_url = "https://cdn.discordapp.com/attachments/830370436582998077/902028015402381322/captcha.png"

try:
  os.mkdir(img_folder)
except:
  pass

def get_img(url=None):
  if url ==None:
    url = test_url

  page = requests.get(url)

  f_ext = os.path.splitext(url)[-1]
  
  f_name = f'{img_folder}/img{f_ext}'

  with open(f_name, 'wb') as f:
      f.write(page.content)

  return f_name


def png_to_jpg(img):
  # Load .png image
  image = cv2.imread(img)

  # Save .jpg image
  cv2.imwrite(f'{img_folder}/img.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

def get_jpg_img(url):
  img = get_img(url)
  jpg_img = png_to_jpg(img)
  return jpg_img

def solve_img(url=None):
  if url ==None:
    url = test_url
  f = get_img(url)#get img to local dir
  
  text = pytesseract.image_to_string(Image.open(f))
  #print(f)
  print(text)
  def write_data():
    file = open(f"{img_folder}/img.txt",'w')
    file.write(text)
    file.close()
  write_data()
  return text

def solve_local_img(path=None):
  if path ==None:
    print('Need to enter a img path')
    return 
  
  text = pytesseract.image_to_string(Image.open(path))
  #print(f)
  print(text)
  def write_data():
    file = open(f"{img_folder}/img.txt",'w')
    file.write(text)
    file.close()
  write_data()
  return text

if __name__ == '__main__':
  pip_in_tess()
  solve_img(test_url)