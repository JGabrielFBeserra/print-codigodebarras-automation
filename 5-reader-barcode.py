import cv2
from pyzbar.pyzbar import decode

img = cv2.imread("recorte.png")

barcodes = decode(img)

for barcode in barcodes:
    print("📦 Código:", barcode.data.decode("utf-8"))
    print("📄 Tipo:", barcode.type)