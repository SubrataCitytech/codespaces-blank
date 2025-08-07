import qrcode # type: ignore
from PIL import Image # type: ignore

data = input("Enter anything to generate QR: ")

# Create QR code instance
qr = qrcode.QRCode(version=3, box_size=8, border=4)
qr.add_data(data)
qr.make(fit=True)

# Generate QR code image
image = qr.make_image(fill="black", back_color="aqua")

# Save and show the image
image.save("qr_code.png")
image.show()