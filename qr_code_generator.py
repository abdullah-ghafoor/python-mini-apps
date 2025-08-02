import pyqrcode
from PIL import Image
import png

link = input("Input Anything to generate a QR : ")

qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png",scale=5)
img = Image.open("QRCode.png") 
img.show()