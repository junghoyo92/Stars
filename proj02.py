#CSE231 Section 2
#proj02

print('This program will draw stars at random positions with random colors given the users inputs for the number of stars and the length of the stars')

import turtle
import random

turtle.title('proj02.py')
turtle.setup(500,500,0,0)

# This part of the program prompts the user for the number of stars to draw and the length of the stars.
# The program also error checks to make sure the input is an integer digit and converts the input to an integer.

while True:
     n=input('Enter an integer for the number of stars: ')            #Prompts the user for the number of stars to draw.
     if n.isdigit():                                                  #Checks if the input is a digit.
          n=int(n)                                                    #If n is a digit, the digit is then changed to an integer for the rest of coding.
          break                                                       #Skips the else statement, if the if statement is true.
     else:                                                            #If the input is not a digit, it will notify the user that it is not a valid integer.
          print('The number must be an integer and at least 1')       #and continue to prompt the user for an integer.
          continue
     
while True:    
     length= input('Enter the length of the sides of the star: ')     #Promts the user for the length of the star to draw.
     if length.isdigit():                                             #Checks if the input is a digit.
          length=int(length)                                          #If n is a digit, the digit is then changed to an integer for the rest of coding.
          break                                                       #Skips the else statement, if the if statement is true.
     else:                                                            #If the input is not a digit, it will notify the user that it is not a valid integer.
          print('The number must be an integer and at least 1')       #and continue to prompt the user for an integer.
          continue

# This part of the program uses a for loop and to draw the star using the given inputs for length.

def star(points, length):            #Defines a function polygon with respect to the number of points on the star and its length.

     for i in range(points):            #For loop used to draw the star using the users input for length.
         turtle.right(180/points)
         turtle.forward(length)
         turtle.left((90/points)+90)
         turtle.forward(length)
         
# This part of the program uses a for loop to designate turtle to random positions with random colors to draw and fill the stars.

for x in range(n):                      #For loop uses the users input for the number of stars to draw that many stars.
     x=random.randint(-300,300)         #Designates random positions for the x value of the pen to go to throughout the loop.
     y=random.randint(-300,300)         #Designates random positions for the y value of the pen to go to throughout the loop.
     turtle.penup()                     #Picks the pen up prior to moving to a new location.
     turtle.goto(x,y)                   #Moves the pen to this random position of (x,y)
     turtle.pendown()                   #Places the pen at the random position of (x,y) to begin drawing.

     red=random.random()                #Designates a random range of color for red.
     green=random.random()              #Designates a random range of color for green.
     blue=random.random()               #Designates a random range of color for blue.
     turtle.color(red, green, blue)     #Designates a random mix of colors for (red, green, blue) for the pen.
     turtle.fillcolor(red, green, blue) #Designates a fill color for the image with the random mix of colors for (red, green, blue).

     turtle.begin_fill()                #Let's the program know when to begin the point of fill.
     star(5, length)                    #The star has 5 points and uses the users input for length to draw the star.
     turtle.end_fill()                  #Let's the program know when to finish the fill.

