import qrcode

image = qrcode.make("https://github.com/davidson-dev")
image.save("perfilGitHub.png")
