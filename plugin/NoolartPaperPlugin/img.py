from PIL import Image
import inspect, os
import argparse


def imgcrop(input, xPieces, yPieces):
    
    
    filename, file_extension = os.path.splitext(input)
    im = Image.open(input)
    imgwidth, imgheight = im.size
    height = imgheight // yPieces
    width = imgwidth // xPieces
    for i in range(0, yPieces):
        for j in range(0, xPieces):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = im.crop(box)
            try:
                a.save(filename + "-" + str(i) + "-" + str(j) + file_extension)
            except Exception as e:
                print(e)
                
filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))

parser = argparse.ArgumentParser()
parser.add_argument("--id")
args = parser.parse_args()
id = args.id

imgcrop(path+"\\imgs\\" + id + "Density.jpg", 3, 3)
imgcrop(path+"\\imgs\\" + id + "Magnetic.jpg", 3, 3)
imgcrop(path+"\\imgs\\" + id +  "Res.jpg", 3, 3)
imgcrop(path+"\\imgs\\" + id +  "Vs.jpg", 3, 3)
imgcrop(path+"\\imgs\\" + id +  "Vp.jpg", 3, 3)
imgcrop(path+"\\imgs\\" + id +  "Rad.jpg", 3, 3)
