from math import sqrt

print("Enter the three legs of a triangle to see if it is a triangle, a right triangle, an obtuse triangle, and/or an acute triange.")
side_a=input("Input side a:")
side_b=input("Input side b:")
side_c=input("Input side c:")
def is_triangle():
    if (side_a > side_b + side_c) or (side_b > side_a + side_c) or (side_c > side_a + side_b):
        print ("Not a triangle.")
    else:
        print ("Is a triangle.")

is_triangle()