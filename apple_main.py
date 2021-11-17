#   a123_apple_1.py
import turtle as trtl

#-----setup-----

t=0
tstep = 0.25      
delx = 2       
g = -1        
yvel = 20   
y=0            

apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=0.3, height=0.35)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image) # Make the screen aware of the new file

# apple = trtl.Turtle()

# apple.hideturtle()

pear = trtl.Turtle()

WorldBorder = (3,4)

drawer = trtl.Turtle()

posVal = True

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def border_control(border):
  for object_range in range(0,100,1):
    border.goto(100,-200)

def draw_apple(active_apple):
  global posVal
  active_apple.shape(apple_image)
  active_apple.penup()
  active_apple.goto(0,-200)
  if posVal == True:
    posVal = False
    active_apple.goto(-280,-200)
  else:
    posVal = True
    active_apple.goto(280,-200)

  wn.update()

def draw_pear(activate_pear):
  activate_pear.shape(pear_image)
  wn.update()

def object_fall(object):
  global t, yvel, y, tstep, delx, g
  for vel_sample in range(0,5,1):
    object.goto(vel_sample,-200)
    num = 0
  while (5):
    t=t+tstep
    x=t*delx
    yvel = yvel + g * tstep    
    y=y + yvel * tstep       
    object.goto(x,y)
    num = num + 1
    if object.ycor() < -200:
        print("OBJECT BORDER REACHED: ",object.ycor())
    if num > 200:
        object.clear()
        t=0
        tstep = 0.25      
        delx = 2       
        g = -1        
        yvel = 20   
        y=0      
        break
    print(num)
    
def get_mouse_click_coor(x, y):
    print(x, y)

def draw_an_A():
  drawer.color("blue")
  drawer.write("A", font=("Arial", 74, "bold")) 
  drawer.penup()
  drawer.forward(30)
  draw_pear(pear)
  object_fall(pear)

#-----function calls-----

trtl.onscreenclick(get_mouse_click_coor)

wn.onkeypress(draw_an_A, "a")

wn.listen()

wn.mainloop()