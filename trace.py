from PIL import Image
from random import randrange
import pyautogui
import numpy as np
import keyboard
import time

default = "images/cherryflowers.JPG"

def randWidth():
    return randrange(13, 205, 2)

def calcCircle(x):
    return np.sqrt(matrixHalf**2 - x**2)

#def drawCircle(xarr, yarr):
    #TODO

class picture(object):
    def __init__(self, img):
        self.r, self.g, self.b, = np.array(img).T
        self.xscale, self.yscale = (img.size[0]/pyautogui.size()[0],img.size[1]/pyautogui.size()[1])
        self.imgwidth, self.imgheight = img.size
        # self.circlecoordx = np.arange(matrixHalf+1)
        # self.circlecoordy = [calcCircle(self.circlecoordx[i]) for i in range(matrixHalf+1)]

    def convert_input(self, x, y, matH, matW):
        x=int(x*self.xscale)
        y=int(y*self.yscale)
        x = max(matW, min(x, self.imgwidth - matW - 1))
        y = max(matH, min(y, self.imgheight - matH - 1))
        return (x, y)
    
    def matrix_operation(self, x, y, matH, action, matW=0):
        if not matW: #is there a better way?
            matW = matH
        matHHalf = int(matH/2)
        matWHalf = int(matW/2)
        x, y = self.convert_input(x, y, matHHalf, matWHalf)
        #print(matHHalf, x, self.r.size, self.imgheight, self.imgwidth)
        self.rmatrix = [self.r[i][j] for i in range(x-matWHalf, x+matWHalf+1) for j in range(y-matHHalf, y+matHHalf+1)]
        self.gmatrix = [self.g[i][j] for i in range(x-matWHalf, x+matWHalf+1) for j in range(y-matHHalf, y+matHHalf+1)]
        self.bmatrix = [self.b[i][j] for i in range(x-matWHalf, x+matWHalf+1) for j in range(y-matHHalf, y+matHHalf+1)]

        action()

        for i in range(0, matW):
            for j in range(0, matH):
                #print(matH, matW, matHHalf, matWHalf)
                #print(len(self.rmatrix), x)
                #print(i, matH, j, i*matW+j)
                #print(self.rmatrix[i*matW+j], "\n")
                self.r[x+i-matWHalf][y+j-matHHalf] = self.rmatrix[i*matH+j]
                self.g[x+i-matWHalf][y+j-matHHalf] = self.gmatrix[i*matH+j]
                self.b[x+i-matWHalf][y+j-matHHalf] = self.bmatrix[i*matH+j]

    def reverse(self):
        self.rmatrix.reverse()
        self.gmatrix.reverse()
        self.bmatrix.reverse()

    def redLine(self):
        self.rmatrix = [255] * len(self.rmatrix) *len(self.rmatrix[0])
        self.gmatrix = [0] * len(self.rmatrix) *len(self.rmatrix[0])
        self.bmatrix = [0] * len(self.rmatrix) *len(self.rmatrix[0])

    def colorrotate(self):
        temp = self.rmatrix
        self.rmatrix = self.gmatrix
        self.gmatrix = self.bmatrix
        self.bmatrix = temp

    def colorrotate2(self):
        temp = self.rmatrix
        self.rmatrix = self.bmatrix
        self.bmatrix = self.gmatrix
        self.gmatrix = temp

    #def circle(self):
        #TODO

    def save(self, name):
        im = Image.fromarray(np.dstack([item.T for item in (self.r,self.g,self.b,)]))
        im.save(name)

while True:
    try:
        imgPath = input("Enter image path name: ")
        type(imgPath)
        if(not imgPath):
            imgPath = default
            print("Opening default option: " + imgPath)
        img = Image.open(imgPath)
        break

    except IOError:
        print("Wrong path try again loser\n")

print("Successfully opened image! Press 'esc' to save and quit \n")
pic = picture(img)

time.sleep(1)

prevx = 0
while True:
    if keyboard.is_pressed('esc'):
        print("Drawing finished!\n")
        break
    
    x, y = pyautogui.position()

    if keyboard.is_pressed('shift'):
        pic.matrix_operation(x, y, randWidth(), pic.colorrotate)
    elif keyboard.is_pressed('ctrl'):
        pic.matrix_operation(x, y, randWidth(), pic.colorrotate2)
    elif prevx == x:
        pic.matrix_operation(x, y, randWidth(), pic.reverse, randWidth())
    else:
        pic.matrix_operation(x, y, randWidth(), pic.reverse)
    
    prevx = x

outName = input("What you wanna name it? ")
type(outName)

pic.save(outName)
