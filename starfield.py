import tkinter, random
#star class to do all stary things
class Star:
    def __init__(self, xPos=0, yPos=0, zPos=0, size=0, randomize = False):#asign key values in constructor
        if randomize:
            self.setRand()
        else:
            self.x = xPos
            self.y = yPos
            self.scale = size
            self.depth = zPos
    def setRand(self):
        self.x = random.randint(0,winWidth)-winWidth/2
        self.y = random.randint(0,winHeight)-winHeight/2
        self.scale = random.randint(0,maxStarSize*100)/100
        self.depth = random.randint(0,1000)+camPos
    def color(self):#gets colour of star
        hue = self.scale/maxStarSize*3
        r = 1-abs(hue%1-0.5)
        
    def draw(self):
        try:
            x1 = (self.x-self.scale)*300/(self.depth-camPos)+winWidth/2
            y1 = (self.y-self.scale)*300/(self.depth-camPos)+winHeight/2
            x2 = (self.x+self.scale)*300/(self.depth-camPos)+winWidth/2
            y2 = (self.y+self.scale)*300/(self.depth-camPos)+winHeight/2
            if x2<0 or x1>winWidth or y2<0 or y1>winHeight:
                self.setRand()
            else:
                canvas.create_oval(x1,y1,x2,y2, fill="#ffffff", outline = "#ffffff")#hex string tkinter colour :(
        except ZeroDivisionError:
            self.setRand()

winWidth = 600
winHeight = 360
win = tkinter.Tk()
canvas = tkinter.Canvas(win, width = 600, height = 360)
canvas.pack()


stars = []
maxStarSize = 4
camPos = 0
for i in range(0,200):
    stars.append(Star(randomize = True))

while True:
    canvas.delete("all")#clear screen
    canvas.create_rectangle(0,0,600,360,fill="#000000")#fill black
    for star in stars:
        star.draw()
    canvas.update()
    camPos+=5
