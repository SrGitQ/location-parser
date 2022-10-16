import qrcode

# Setting qr
qr = qrcode.QRCode(
	version=1,
	box_size=15,
	border=5
)


def QRgenerator(link:str, id:str='qe'):
  # Adding data
  qr.add_data(link)

  qr.make(fit=True)

  img = qr.make_image(fill_color='rgb(153,153,153)', back_color='rgb(244,244,245)')
  img.save(f'./sessionMng/static/codes/{id}_QR.png')
