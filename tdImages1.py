from PIL import Image
import numpy as np
import math
import cv2
img = Image.open('C:/Users/alberic/Downloads/lena.png')

dataRGB = img.getdata()

"""# Question 1
r = [(d[0], 0, 0) for d in dataRGB]
g = [(0, d[1], 0) for d in dataRGB]
b = [(0, 0, d[2]) for d in dataRGB]

img.putdata(r)
img.save('C:/Users/alberic/Downloads/r.png')
img.putdata(g)
img.save('C:/Users/alberic/Downloads/g.png')
img.putdata(b)
img.save('C:/Users/alberic/Downloads/b.png')"""

"""# Question 2
different_colors = set()
tot = 0
for d in dataRGB:
    tot +=1
    different_colors.add(d)
print(len(different_colors))"""

"""
#Question 3
def psnr(img1, img2):
    mse = np.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    max_pixel = 255.0
    return 20 * math.log10(max_pixel / math.sqrt(mse))

img1 = cv2.imread('C:/Users/alberic/Downloads/lena.png')
img2 = cv2.imread('C:/Users/alberic/Downloads/r.png',1)

print(psnr(img1,img2))
"""


"""#Question 4

def rgb_to_hsv(rgb):
    #convertit un tuple RGB en tuple HSV

    # Unpack the tuple for readability
    r, g, b = rgb

    # Compute the H value by finding the maximum of the RGB values
    rgb_max = max(rgb)
    rgb_min = min(rgb)

    # Compute the value
    v = rgb_max;
    if v == 0:
        h = s = 0
        return (h,s,v)


    # Compute the saturation value
    s = 255 * (rgb_max - rgb_min) // v

    if s == 0:
        h = 0
        return (h, s, v)

    # Compute the Hue
    if rgb_max == r:
        h = 0 + 43*(g - b)//(rgb_max - rgb_min)
    elif rgb_max == g:
        h = 85 + 43*(b - r)//(rgb_max - rgb_min)
    else: # RGB_MAX == B
        h = 171 + 43*(r - g)//(rgb_max - rgb_min)

    return (h, s, v)

dataHSV = []
for d in dataRGB:
    dataHSV.append(rgb_to_hsv(d))

img.putdata(dataHSV)
img.save('C:/Users/alberic/Downloads/lenaHSV.png')


def hsv_to_rgb(hsv):

    #convertit un tuple HSV en tuple RGB

    h, s, v = hsv

    # Check if the color is Grayscale
    if s == 0:
        r = v
        g = v
        b = v
        return (r, g, b)

    # Make hue 0-5
    region = h // 43

    # Find remainder part, make it from 0-255
    remainder = (h - (region * 43)) * 6

    # Calculate temp vars, doing integer multiplication
    p = (v * (255 - s)) >> 8
    q = (v * (255 - ((s * remainder) >> 8))) >> 8
    t = (v * (255 - ((s * (255 - remainder)) >> 8))) >> 8


    # Assign temp vars based on color cone region
    if region == 0:
        r = v
        g = t
        b = p

    elif region == 1:
        r = q
        g = v
        b = p

    elif region == 2:
        r = p
        g = v
        b = t

    elif region == 3:
        r = p
        g = q
        b = v

    elif region == 4:
        r = t
        g = p
        b = v
    else:
        r = v
        g = p
        b = q

    return (r, g, b)

dataRGB2 = []
for d in dataHSV:
    dataRGB2.append(hsv_to_rgb(d))
img.putdata(dataRGB2)
img.save('C:/Users/alberic/Downloads/lenaRGB2.png')

#On constate que la lena en hsv est bleue alors qu'après le retour en rgb elle a les bonnes couleurs.
"""

#l'entrée est tous les tuples rgb constituant l'image
#la sortie est ces tuples multipliés par les constantes pour obtenir un format YUV
def rgb_to_yuv(rgb):
    m = np.array([
        [0.29900, -0.147108,  0.614777],
        [0.58700, -0.288804, -0.514799],
        [0.11400,  0.435912, -0.099978]
    ])
    arr = np.dot(rgb, m)
    yuv = []
    for i in arr:
        yuv.append((int(round(i[0])),int(round(i[1])),int(round(i[2]))))

    return yuv


#l'entrée est tous les tuples YUV constituant l'image
#la sortie est ces tuples multipliés par les constantes pour obtenir un format RGB
def yuv_to_rgb(yuv):
    m = np.array([
        [1.000, 1.000, 1.000],
        [0.000, -0.394, 2.032],
        [1.140, -0.581, 0.000],
    ])
    arr = np.dot(yuv, m)
    rgb = []
    for i in arr:
        rgb.append((int(round(i[0])), int(round(i[1])), int(round(i[2]))))
    return rgb


dataYUV = rgb_to_yuv(dataRGB)
img.putdata(dataYUV)
img.save('C:/Users/alberic/Downloads/lenaYUV.png')


dataRGB3 = yuv_to_rgb(dataYUV)
img.putdata(dataRGB3)
img.save('C:/Users/alberic/Downloads/lenaRGB3.png')

#l'image en yuv est légerment plus rouge que la normale
#Une fois reconvertie en RGB, l'image est comme avant.