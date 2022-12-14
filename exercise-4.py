# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
print("Enter the lengths of all three sides of a triangle:")
#      Enter the lengths of three side of a triangle:
a = input("a:")
b = input("b:")
c = input("c:")

if (a == b and a==c):
  triangle_type = "equalateral"
elif (a != b and a != c and b != c):
  triangle_type = "scalene"
else:
  triangle_type = "isosceles"

print(f'A triangle with sides of {a}, {b} & {c} is a {triangle_type} triangle')
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
