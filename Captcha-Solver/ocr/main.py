import os
def download_the_data():
  os.system('curl -LO https://github.com/AakashKumarNain/CaptchaCracker/raw/master/captcha_images_v2.zip')
  os.system('unzip -qq captcha_images_v2.zip')
#download_the_data()

from ajtools import get_jpg_img
from ajocr import decode_batch_predictions



url = 'https://cdn.discordapp.com/attachments/830370436582998077/899978681353641984/captcha.png'

get_jpg_img(url)
decode_batch_predictions('Images/img.jpg')