from PIL import Image
import random

def newImg():
    #new 7*7 canvas with white background
    img = Image.new('RGB', (7, 7), color=(random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))
    
    numIterations = random.randint(0, 27)
    numPixels = 0
    pixelsPlaced = []
    curPixel = (random.randint(0, 3), random.randint(0, 3))
    
    #for each iteration, new color
    for iterations in range(numIterations):
        R = random.randint(0, 254)
        G = random.randint(0, 254)
        B = random.randint(0, 254)
        numPixels = random.randint(3, 12)
        pixelsPlaced = []
    
        #for each layer, don't place any pixel where another pixel already is in the layer
        for i in range(numPixels):

            curPixel = (random.randint(0, 3), random.randint(0, 3))
            while curPixel in pixelsPlaced:
                curPixel = (random.randint(0, 3), random.randint(0, 3))
                
            pixelsPlaced.append(curPixel)
            img.putpixel((curPixel[0], curPixel[1]), (R,G,B))
            img.putpixel((3 + (3 - curPixel[0]), curPixel[1]), (R,G,B))
            img.putpixel((curPixel[0], 3 + (3 - curPixel[1])), (R,G,B))
            img.putpixel((3 + (3 - curPixel[0]), 3 + (3 - curPixel[1])), (R,G,B))
            
    #google credit: https://stackoverflow.com/questions/23460275/python-upscale-image-without-blur-pil
    #for this upscaling bit
    img = img.resize((700, 700), resample=Image.BOX)
    
    #google credit: https://stackoverflow.com/questions/54346063/how-to-draw-square-pixel-by-pixel-python-pil
    #for broader program flow
    img.save('profile_picture.png')
    
    return img

newImg()