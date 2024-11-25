import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,border=4,
    )
qr.add_data("https://youtube.com/@needi_developer?si=OX0w9tsiBaniM54-")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("YT_QR1.png")