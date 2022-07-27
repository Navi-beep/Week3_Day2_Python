# func 1 What is the area of a circle with a radius of 7cm?
# func 2 What is the hypotenuse of a right angle with sides of 3in and 4in?

from math import sqrt , pi


#print(pi)

#func 1
def area_of_circle(radius):
        x =  ((radius * pi)**2)
        print(x)
        

#func 2
def hypotenuse(a,b):
        a = input(float("What is the length of your first side?: "))
        b = input(float("What is the length of your second side?: "))
        print(sqrt(a ** 2 + b ** 2))

#def func(x):
 #       x = 10
#        print(x)