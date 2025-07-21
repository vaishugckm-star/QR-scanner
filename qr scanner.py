import qrcode
from pyzbar.pyzbar import decode
from PIL import Image 
myqr = qrcode.make("https://www.youtube.com/watch?v=dgCYDETwjcs&list=PLoGk-8pBKSRVWvGN372yBzrF15tSv22KY")
myqr1 = qrcode.make("https://web.whatsapp.com/")

myqr.save("myqr.png", scale = 8)
myqr1.save("myqr1.png", scale = 7)

b = decode(Image.open("myqr.png"))
b1 = decode(Image.open("myqr1.png"))
print(b[0].data.decode("ascii"))
print(b1[0].data.decode("ascii"))
print("QR codes generated and decoded successfully.")
print("You can scan the QR codes using a QR code scanner app or camera.")

