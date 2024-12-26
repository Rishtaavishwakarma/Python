import qrcode
from PIL import Image 
qr= qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=15,border=3)
qr.add_data("i have to do best")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("for_you.png")