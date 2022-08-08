import sys
import qrcode
img=qrcode.make(sys.argv[1])
# print("second arg",sys.argv[2])
img.save("qrCodeImage.png")
print("saved as qrCodeImage.png")