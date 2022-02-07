import qrcode
data = "Салоп Максим/7а/05.02.22/2334"
filename = "qrcode14"
img = qrcode.make(data)
img.save(filename)
