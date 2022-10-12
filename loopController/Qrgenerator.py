import qrcode

# Setting qr
qr = qrcode.QRCode(
	version=1,
	box_size=15,
	border=5
)

def generateQRCode(link:str):
  # Adding data
  qr.add_data(link)
  qr.make(fit=True)
  img = qr.make_image(fill='black', back_color='white')
  img.save('./static/qrcode.png')