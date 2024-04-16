def col(x,y,w,h,x2,y2,w2,h2):
   if (x + w >= x2) and (x <= x2 + w2) and (y + h >= y2) and (y <= y2 + h2):
       return True
   else:
       return False
x = 50
y = 950
ysp = 0
grav = 0.2
jump = False
pr = -6
a = 0
xy = 700
yx = 975
x1 = 0
y1 = -100
def setup():
    size(1920,1000)
    rectMode(CENTER)
def draw():
    global x,y,ysp,grav,jump,pr,a,xy,yx,x1,y1
    background(1)
    rect(x1,y1,100,50)
    rect(x,y,50,50)
    ysp += grav
    y += ysp
    if y > height - 25:
        y = height - 25
        ysp = 0
        jump = False
    if keyPressed == True:
        if key == 'W' or key == 'w':
            if jump == False:
                ysp = pr
                jump = True    
    if x > 600:
        xy -= 6
        x -= 6  
    x += 6
    if x1 > 600:
        xy -= 6
        x1 -= 6
        x -= 6
    x1 += 6
    if col(xy,yx,50,50,x,y,50,50):
        ysp = -0.2
        jump == False
        if keyPressed == True:
            if key == 'W' or key == 'w':
                ysp = pr
    if col(xy + 500,yx,50,50,x,y,50,50):
        ysp = -0.2
        jump == False
        if keyPressed == True:
            if key == 'W' or key == 'w':
                ysp = pr
    if col(xy,yx,1,1,x,y,50,50):
        noLoop()
    if col(xy + 500,yx,1,1,x,y,50,50):
        noLoop()
    if col(xy + 65,yx + 25,20,40,x,y,50,50):
        noLoop()
    if col(xy + 1115,yx + 25,20,40,x,y,50,50):
        noLoop()
    if col(xy + 1500,yx,1000,50,x,y,50,50):
        ysp = -0.2
        jump == False
        if keyPressed == True:
            if key == 'W' or key == 'w':
                ysp = pr
    if col(xy + 2475,yx - 100,50,100,x,y,50,50):
        x = -2000
        x1 = 3175
        y1 = 800
    if col(xy + 1500,yx,1,1,x,y,50,50):
        noLoop()
    else:
        rect(xy,yx,50,50)
        rect(xy + 500,yx,50,50)
        triangle(xy + 50,yx + 25,xy + 100,yx + 25, xy + 75,yx - 25)
        triangle(xy + 1100,yx + 25,xy + 1150,yx + 25, xy + 1125,yx - 25)
        rect(xy + 2000,yx,1000,50)
        fill(255,0,222)
        ellipse(xy + 2500, yx - 100,50,100)
        fill(255)
        
            
