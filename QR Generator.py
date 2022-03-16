import qrcode
img = qrcode.make("https://www.github.com/kunalvijay42")
img.save("github.jpg")