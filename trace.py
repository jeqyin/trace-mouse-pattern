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
        # self.circlecoordx = np.arange(matrixHalf+1)
        # self.circlecoordy = [calcCircle(self.circlecoordx[i]) for i in range(matrixHalf+1)]

    def convert_input(self, x, y, matrixHalf):
        x=int(x*self.xscale)
        y=int(y*self.yscale)
        x = max(matrixHalf, min(x, width - matrixHalf - 1))
        y = max(matrixHalf, min(y, height - matrixHalf - 1))
        return (x, y)
    
    def matrix_operation(self, x, y, matrixSize, action):
        matrixHalf = int(matrixSize/2)
        x, y = self.convert_input(x, y, matrixHalf)
        self.rmatrix = [self.r[i][j] for i in range(x-matrixHalf, x+matrixHalf+1) for j in range(y-matrixHalf, y+matrixHalf+1)]
        self.gmatrix = [self.g[i][j] for i in range(x-matrixHalf, x+matrixHalf+1) for j in range(y-matrixHalf, y+matrixHalf+1)]
        self.bmatrix = [self.b[i][j] for i in range(x-matrixHalf, x+matrixHalf+1) for j in range(y-matrixHalf, y+matrixHalf+1)]

        action()

        for i in range(0, matrixSize):
            for j in range(0, matrixSize):
                self.r[x+i-matrixHalf][y+j-matrixHalf] = self.rmatrix[i*matrixSize+j]
                self.g[x+i-matrixHalf][y+j-matrixHalf] = self.gmatrix[i*matrixSize+j]
                self.b[x+i-matrixHalf][y+j-matrixHalf] = self.bmatrix[i*matrixSize+j]

    def reverse(self):
        self.rmatrix.reverse()
        self.gmatrix.reverse()
        self.bmatrix.reverse()

    def redLine(self):
        self.rmatrix = [255] * matrixSize *matrixSize
        self.gmatrix = [0] * matrixSize *matrixSize
        self.bmatrix = [0] * matrixSize *matrixSize

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
width, height = img.size
pic = picture(img)

time.sleep(1)
while True:
    if keyboard.is_pressed('esc'):
        print("Drawing finished!\n")
        break
    
    x, y = pyautogui.position()

    if keyboard.is_pressed('shift'):
        pic.matrix_operation(x, y, randWidth(), pic.colorrotate)
    elif keyboard.is_pressed('ctrl'):
        pic.matrix_operation(x, y, randWidth(), pic.colorrotate2)
    else:
        pic.matrix_operation(x, y, randWidth(), pic.reverse)

outName = input("What you wanna name it? ")
type(outName)

pic.save(outName)
