import imp
#QR Code Generator Python Project
#This is a console based project
#In this project we are able to create customizable QR Code

import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10, border=4)

qr.add_data("https://github.com/omvalia")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("some_file.png")
