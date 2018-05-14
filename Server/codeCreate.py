import qrcode
from PIL import Image

def getCountAddress(name,accountAd):
    QRcode = qrcode.main.QRCode()
    QRcode.add_data(accountAd)
    addImg = QRcode.make_image()
    addImg.save("../image/"+name+".png")
