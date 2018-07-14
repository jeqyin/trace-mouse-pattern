from PIL import Image
import pyautogui
import numpy as np
import keyboard
import time

chunkSize = 3
chunkHalf = int(chunkSize/2)

class picture(object):
    def __init__(self, img):
        self.r, self.g, self.b, = np.array(img).T
    
    def chunk(self, x, y, action):
        self.rChunk = [self.r[i][j] for i in range(x-chunkHalf, x+chunkHalf+1) for j in range(y-chunkHalf, y+chunkHalf+1)]
        self.gChunk = [self.g[i][j] for i in range(x-chunkHalf, x+chunkHalf+1) for j in range(y-chunkHalf, y+chunkHalf+1)]
        self.bChunk = [self.b[i][j] for i in range(x-chunkHalf, x+chunkHalf+1) for j in range(y-chunkHalf, y+chunkHalf+1)]

        if action == "reverse":
            self.reverse()
        elif action == "red":
            self.redLine()

        for i in range(0, chunkSize):
            for j in range(0, chunkSize):
                self.r[x+i-chunkHalf][y+j-chunkHalf] = self.rChunk[i*chunkSize+j]
                self.g[x+i-chunkHalf][y+j-chunkHalf] = self.gChunk[i*chunkSize+j]
                self.b[x+i-chunkHalf][y+j-chunkHalf] = self.bChunk[i*chunkSize+j]

    def reverse(self):
        self.rChunk.reverse()
        self.gChunk.reverse()
        self.bChunk.reverse()

    def redLine(self):
        self.rChunk = [255] * chunkSize *chunkSize
        self.gChunk = [0] * chunkSize *chunkSize
        self.bChunk = [0] * chunkSize *chunkSize

    def save(self, name):
        im = Image.fromarray(np.dstack([item.T for item in (self.r,self.g,self.b,)]))
        im.save(name)

imgPath = input("Enter image path name: ")
type(imgPath)

img = Image.open(imgPath)
width, height = img.size
pic = picture(img)

time.sleep(10)
while True:
    if keyboard.is_pressed('s'):
        print("Drawing finished!\n")
        break
    x, y = pyautogui.position()
    x = max(chunkHalf, min(x, width - chunkHalf - 1))
    y = max(chunkHalf, min(y, height - chunkHalf - 1))
    pic.chunk(x, y, "reverse")

outName = input("What you wanna name it? ")
type(outName)

pic.save(outName)
