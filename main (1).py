import turtle, random, math


# Global Variables
canvas_width = 1000
canvas_height = 1000
screen = turtle.Screen()
myPen = turtle.Turtle()

# Setup the Pen and Screen
screen.tracer(False)
screen.setup(canvas_width, canvas_height, startx = None, starty = None)
myPen.tracer(False)
myPen.hideturtle()
myPen.penup()
myPen.speed(0)


# draw the landscape
def drawLandscape():  
  '''
    ADD/CHANGE CODE BELOW               
    Use the helper functions defined below 
    OR create your own 
    in order to draw a landscape scene.
  '''
  
  # Example Landscape 
  drawSky()
  drawGrass()
 
  drawRock(-350,-450, "gray",20)
  drawRock(-380,-425,"gray",22)

  drawBird(-130,315,"brown", 40)
  drawBird(260, 310, "brown", 35)
  drawTrees(-320, 260, 9, 110)
  drawRock(-420,-250, "gray", 20)
  drawRock(420, -280, "gray", 20)
  drawTrees(-400, 120, 10, 130)
  drawTrees(-375,-80,4,150)
  drawTrees(200,-220,2,170)
  drawTrees(-200,-350,2,190)
     
  drawCloud(-200,375,40)
  drawCloud(400,370,40)
  drawCloud(-390, 370, 25) 
  drawCloud(-425,325,25)
  drawSun(0,380, 225)








############################################################
#
#  
#  Helper functions to draw shapes such as circles, 
#  rectangles, and triangles. 
#  Other functions include drawing trees, houses,
#  sun, cloud, sky, grass, rock, and bird.
#  
#  List of functions available:
#
#    drawTree(x, y, size)
#    drawTrees(x, y, numTrees, size)
#    drawHouse(x, y, color, size)
#    drawHouses(x, y, numHouses, size)
#    drawSun(x, y, radius)
#    drawCloud(x, y, size)
#    drawRock(x, y, color, size)
#    drawBird(x, y, color, size)
#    drawSky()
#    drawGrass()
#    drawCircle(x, y, color, radius)
#    drawSquare(x, y, color, size)
#    drawTriangle(x, y, fill, color, size)
#    drawRectangle(x, y, length, width, color)
#    getRandomColor()

#
############################################################





############################################################
#
#  drawTree(x, y, size)
#
#  This function draws a single tree at the location (x,y)
#
#  @param x: x position of tree
#  @param y: y position of tree
#  @param size: the size of the tree
#
############################################################
def drawTree(x, y, size):
  """
  Draw a single tree at the location (x,y).
  """
  # first draw 3 green layers of tringular tree branches
  drawTriangle(x, y, True, "green", size)
  drawTriangle(x, y-((60.0/200.0) * size), True, "green", size)
  drawTriangle(x, y-((120.0/200.0) * size), True, "green", size)
  
  # next draw the bottom rectangular brown trunk
  rectangle_length =  (80.0/200.0) * size
  rectangle_width = (30.0/200.0) * size
  triangle_height =  (math.sin(math.radians(60))*size)
  drawRectangle(x,y-(triangle_height) - (rectangle_length)/2.0, rectangle_length, rectangle_width, "brown")

  
############################################################
#
#  drawTrees(x, y, numTrees, size)
#
#  This function draws a group of trees starting at the
#  location (x,y). The number of trees drawn depends on the 
#  parameter numTrees. A scaling factor is used to make the 
#  trees at the back look smaller than the trees in the front.
#
#  @param x: starting x position for drawing the trees
#  @param y: starting y position for drawing the trees
#  @param numTrees: number of trees to draw
#  @param size: the size of the tree
#
############################################################
def drawTrees(x, y, numTrees, size):
  """
  Draw a group of trees starting at (x, y). 
  The number of trees drawn is specified by numTrees.
  
  A scaling factor is used to determine how small/big
  the tree becomes as the y-value is increases/decreases.
  """
 
  scaling_factor = 0.1  # scaling factor
  
  # loop to draw the trees
  for n in range(numTrees):
    random_num = random.randint(-2,2)
    size_value = size
    
    # scale size (small/big) depending on y value
    if (y < 0):
      size_value = size + math.fabs(scaling_factor * y)
    elif (size-(scaling_factor)*y <= 0):
      size_value = 10 # min size
    elif (y > 0):
      size_value = math.fabs(size - (scaling_factor)*y)
    
    # draw tree
    drawTree(x+n*((160.0/200.0)*size), y+(random_num * ((20.0/200.0)*size)), size_value)

    
    
############################################################
#
#  drawHouse(x, y, color, size)
#
#  This function draws a house at the location (x,y).
#  The color of house is specified by the parameter color.
#
#  @param x: x position for drawing the house
#  @param y: y position for drawing the house
#  @param color: color of the house
#  @param size: the size of the house
#
############################################################
def drawHouse(x, y, color, size):
  """
  Draw a house at the point (x,y) in the specified color.
  """
  # Draw a square for bottom of house
  myPen.fillcolor(color)
  drawSquare(x, y, color, size)
  
  # Draw a triangle for top of house
  drawTriangle(x, y + ((math.sin(math.radians(60))*size)/2.0)+(size/2.0), True, color, size)



############################################################
#
#  drawHouses(x, y, numHouses, size)
#
#  This function draws a group of houses starting at the
#  location (x,y). The number of houses drawn depends on  
#  the parameter numHouses. A scaling factor is used to  
#  make the houses at the back look smaller than the houses 
#  in the front.
#
#  @param x: starting x position for drawing the houses
#  @param y: starting y position for drawing the houses
#  @param numHouses: number of houses to draw
#  @param size: the size of the house
#
############################################################  
def drawHouses(x, y, numHouses, size):
  """
  Draw a group of houses starting at (x, y). 
  The number of houses drawn is specified by numHouses.

  A scaling factor is used to determine how small/big
  the tree becomes as the y-value is increases/decreases.
  """
  for n in range(numHouses):
    random_num = random.randint(-50,20)
    randomColor = getRandomColor()
    drawHouse(x+n*(1.3*size), y+(random_num*((20.0/200.0)*size)), randomColor, size)

    
############################################################
#
#  drawSun(x, y, radius)
#
#  This function draws a sun at the location (x,y). 
#  The size of the sun is specified by the parameter radius. 
#
#  @param x: x position of the sun
#  @param y: y position of the sun
#  @param radius: the size of the sun
#
############################################################  
def drawSun(x, y, radius):
  """
  Draw a sun centered at the point (x,y) of size as 
  specified by radius.
  """
  myPen.setheading(0)
  myPen.speed(0)
  myPen.penup()
  myPen.goto(x,y)
  myPen.pendown()
  myPen.color("orange")
  for x in range(80):
    myPen.forward(radius)
    myPen.left(170)
  

  
############################################################
#
#  drawCloud(x, y, size)
#
#  This function draws a gray cloud at the location (x,y). 
#  The size of the cloud is specified by the parameter size. 
#
#  @param x: x position of the cloud
#  @param y: y position of the cloud
#  @param size: the size of the cloud
#
############################################################  
def drawCloud(x, y, size):
  """
  Draw a gray cloud at the point (x,y) in the specified
  size.
  """
  myPen.speed(0)
  myPen.penup()
  myPen.setheading(0)
  myPen.goto(x,y)
  myPen.color("gray")
  myPen.begin_fill()
  myPen.circle(size)
  myPen.goto(x+(size), y)
  myPen.circle(size)
  myPen.goto(x-(size), y)
  myPen.circle(size)
  myPen.end_fill()

  
  
  
############################################################
#
#  drawRock(x, y, color, size)
#
#  This function draws a rock at the location (x,y). 
#  The color and size of the rock are specified by the 
#  parameters color and size. 
#
#  @param x: x position of the rock
#  @param y: y position of the rock
#  @param color: color of the rock
#  @param size: the size of the rock
#
############################################################  
def drawRock(x, y, color, size):
  """
  Draw a rock at the point (x,y) in the specified color
  and size.
  """
  myPen.setheading(0)
  myPen.penup()
  myPen.goto(x-size/2, y-size/2)
  myPen.color(color)
  myPen.speed(0)
  myPen.width(3)
  myPen.degrees(360)
  myPen.begin_fill()
  myPen.pendown()
  myPen.left(10)
  myPen.forward(size)
  myPen.left(15)
  myPen.forward(0.75*size)
  myPen.left(85)
  myPen.forward(size)
  myPen.left(15)
  myPen.forward(size * 0.333)
  myPen.left(10)
  myPen.forward(size * 0.5)
  myPen.left(45)
  myPen.forward(size)
  myPen.left(35)
  myPen.forward(size/1.3)
  myPen.left(50)
  myPen.forward(size)
  myPen.left(15)
  myPen.forward(size/2.0)
  myPen.left(70)
  myPen.forward(size/1.2)
  myPen.end_fill()


  
############################################################
#
#  drawBird(x, y, color, size)
#
#  This function draws a v-shaped bird at the location (x,y). 
#  The color and size of the bird are specified by the 
#  parameters color and size. 
#
#  @param x: x position of the bird
#  @param y: y position of the bird
#  @param color: color of the bird
#  @param size: the size of the bird
#
############################################################    
def drawBird(x, y, color, size):
  """
  Draw a v-shaped bird at (x, y) in the specified color
  and size.
  """
  myPen.setheading(0)
  myPen.speed(0)
  myPen.color(color)
  myPen.penup()
  myPen.goto(x,y)
  myPen.pendown()
  myPen.left(45)
  myPen.forward(size)
  myPen.right(90)
  myPen.forward(size/2.0)
  myPen.penup()
  myPen.goto(x,y)
  myPen.setheading(0)
  myPen.pendown()
  myPen.left(135)
  myPen.forward(size)
  myPen.left(90)
  myPen.forward(size/2.0)
  myPen.setheading(0)


############################################################
#
#  drawSky()
#
#  This function draws the sky using the background color
#  - light blue (#87ceeb). 
#  
############################################################    
def drawSky():
  """
  Create the sky by setting the background color to 
  light blue. 
  """
  global screen
  screen.bgcolor("#87CEEB")


############################################################
#
#  drawGrass()
#
#  This function draws the grass at the lower part of the
#  screen using the background color using a green color.
#   
#  
############################################################    
def drawGrass():
  """
  Draw a block of grass that covers the lower part of the
  screen.
  """
  drawRectangle(0, canvas_height/4.0, 750, canvas_width, "rgba(0, 128, 0, 0.76)")

  

############################################################
#
#  drawCircle(x, y, color, radius)
#
#  This function draws a circle at the location (x,y). 
#  The color and size of the circle are specified by the
#  parameters color and radius. 
#
#  @param x: x position of the circle
#  @param y: y position of the circle
#  @param color: color of the circle
#  @param radius: the size of the circle
#
############################################################  
def drawCircle(x, y, color, radius):
  """
  Draw a circle of the specified radius at the point (x,y)
  in the specified color and size.
  """
  myPen.speed(0)
  myPen.penup()
  myPen.setheading(0)
  myPen.goto(x, y-radius)
  myPen.width(3)
  myPen.pencolor(color)
  myPen.degrees(360)
  myPen.pendown()
  myPen.circle(radius)

  
############################################################
#
#  drawSquare(x, y, color, size)
#  This function draws a square at the location (x,y). 
#  The color and size of the square are specified by the
#  parameters color and size. 
#
#  @param x: x position of the square
#  @param y: y position of the square
#  @param color: color of the square
#  @param size: the size of the square
#
############################################################    
def drawSquare(x, y, color, size):
  """
  Draw a square centered at the point (x,y) in the 
  specified color and size.
  """
  global myPen
  # Setup
  myPen.setheading(0)
  myPen.speed(0)
  myPen.penup()
  myPen.goto(x,y-(size/2.0))
  myPen.shape('turtle')
  myPen.width(3)
  myPen.pencolor(color)
  myPen.degrees(360)

  # Draw the four sides of the square.
  myPen.down()
  myPen.forward(size/2.0)
  myPen.left(90)
  myPen.forward(size)
  myPen.left(90)
  myPen.forward(size)
  myPen.left(90)
  myPen.forward(size)
  myPen.left(90)
  myPen.forward(size/2.0)
  myPen.penup()
  

############################################################
#
#  drawTriangle(x, y, fill, color, size)
#  This function draws a triangle at the location (x,y). 
#  The outline color and size of the triangle are specified
#  by the parameters color and size. An additional fill 
#  color can be specified by the parameter fill.
#
#  @param x: x position of the triangle
#  @param y: y position of the triangle
#  @param fill: fill color of the triangle
#  @param color: outline color of the triangle
#  @param size: the size of the triangle
#
############################################################    
def drawTriangle(x, y, fill, color, size):
  """
  Draws a triangle centered at the point (x,y) in the 
  specified color and size. The triangle will also be 
  filled with the color as specified by fill.
  """
  global myPen, screen
  # Setup Pen
  myPen.setheading(0)
  myPen.penup()
  myPen.goto(x,y)
  myPen.speed(0)
  myPen.shape('turtle')
  myPen.width(3)
  myPen.degrees(360)
  if(fill == True):
    # Draw the three sides of the Triangle with filling.
    myPen.pencolor(color)
    myPen.goto(x, y-((math.sin(math.radians(60))*size)/2.0))
    myPen.down()
    myPen.fillcolor(color)
    myPen.fill(True)
    myPen.begin_fill()
    myPen.forward(size/2.0)
    myPen.left(120)
    myPen.forward(size)
    myPen.left(120)
    myPen.forward(size)
    myPen.left(120)
    myPen.forward(size/2.0)
    myPen.end_fill()
    myPen.penup()
    myPen.setheading(0)
    myPen.done()
  else:
    # Draw the three sides of the triangle without filling.
    myPen.pencolor(color)
    myPen.down()
    myPen.forward(size/2.0)
    myPen.left(120)
    myPen.forward(size)
    myPen.left(120)
    myPen.forward(size)
    myPen.left(120)
    myPen.forward(size/2.0)
    myPen.penup()
    myPen.setheading(0)
    myPen.done()

    
############################################################
#
#  drawRectangle(x, y, length, width, color)
#  This function draws a rectangle at the location (x,y). 
#  The color and size of the rectangle are specified
#  by the parameters color, length, and width. 
#
#  @param x: x position of the rectangle
#  @param y: y position of the rectangle
#  @param length: the length of the rectangle
#  @param width: the width of the rectangle
#  @param color: outline color of the rectangle
#
############################################################        
def drawRectangle(x, y, length, width, color):
  """
  Draw a rectangle centered at the point (x,y) with the
  specified color, length, and width.
  """
  # Setup Pen
  myPen.setheading(0)
  myPen.penup()
  myPen.goto(x,y-(length/2))
  myPen.speed(0)
  myPen.shape('turtle')
  myPen.width(3)
  myPen.pencolor(color)
  myPen.degrees(360)

  # Draw the four sides of the rectangle.
  myPen.forward(width/2)
  myPen.fillcolor(color)
  myPen.fill(True)
  myPen.begin_fill()
  myPen.left(90)
  myPen.forward(length/2)
  myPen.left(90)
  myPen.forward(width)
  myPen.left(90)
  myPen.forward(length)
  myPen.left(90)
  myPen.forward(width)
  myPen.left(90)
  myPen.forward(length)
  myPen.end_fill()
  myPen.penup()
  myPen.setheading(0)
  myPen.done()

############################################################
#
#  getRandomColor()
#  This function returns a random RGB value (either red, 
#  green, or blue)
#
#  @return random RGB value (red, green, or blue)
#
############################################################        
def getRandomColor():
  """
  Return a random tuple of rgb values that can represent 
  red, green, or blue.
  """
  rgb = [255,0,0]
  random.shuffle(rgb)
  return tuple(rgb) 



# call the function to draw the landscape
drawLandscape()
