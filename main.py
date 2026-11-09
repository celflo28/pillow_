from PIL import Image, ImageEnhance, ImageOps, ImageDraw

elias = Image.open("eliasfl.jpeg")

# Steg 1: Gör svartvit
bw_elias = elias.convert("L")

# Steg 2: Höj kontrasten
hc_elias = ImageEnhance.Contrast(bw_elias).enhance(1.4)

# Steg 3: Minska ljusheten (brightness)
emo_elias = ImageEnhance.Brightness(hc_elias).enhance(0.6)

# Steg 4: Spara bilden
emo_elias.save("emo_elias.jpeg")

with Image.open('emo_elias.jpeg') as img:
    # Inverterar alla pixlar över ett visst gränsvärde
    img = ImageOps.solarize(img, 60)

    # Lägger till en ram runt bilder
    img = ImageOps.expand(img, 10, 255)

    # Reducerar bitdjupet (antal färger)
    img = ImageOps.posterize(img, 2)

    # Skalar om en bild
    img = ImageOps.scale(img, 3)

    # Spegelvänder en bild
    img = ImageOps.mirror(img)

    img.save('newimage.jpg')

# flagga Sverige
# RGB-värden för blå och gul
BLUE = (0, 106, 167)
YELLOW = (254, 204, 0)

# Skapa en ny bild
im = Image.new("RGB", (160, 100), BLUE)

# Skapa ett ImageDraw-objekt för att kunna rita grafik
imd = ImageDraw.Draw(im)

# Rita två rektanglar
imd.rectangle([(50, 0), (70, 100)], YELLOW)
imd.rectangle([(0, 40), (160, 60)], YELLOW)

im.save("Sverige.png")

#flagga finland
WHITE = (0, 0, 0)
BLUE = (254, 204, 0)

# Skapa en ny bild
im = Image.new("RGB", (160, 100), BLUE)

# Skapa ett ImageDraw-objekt för att kunna rita grafik
imd = ImageDraw.Draw(im)

# Rita två rektanglar
imd.rectangle([(50, 0), (70, 100)], WHITE)
imd.rectangle([(0, 40), (160, 60)], WHITE)

im.save("ondsverige.png")