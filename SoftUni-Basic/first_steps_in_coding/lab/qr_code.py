import pyqrcode
import png
from pyqrcode import QRCode


address = "https://www.mobile.bg/pcgi/mobile.cgi?act=4&adv=11647182295013726"
url = pyqrcode.create (address)
url.png("ford.png" , scale = 8)
