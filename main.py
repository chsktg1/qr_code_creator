import sys
import qrcode
import os
img=qrcode.make(sys.argv[1])
img.save("qrCodeImage.png")
print("saved as qrCodeImage.png at "+os.getcwd())