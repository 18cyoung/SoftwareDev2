import math

a = int(input("Please enter your 'a' value: "))
b = int(input("Please enter your 'b' value: "))

c = math.sqrt(a**2+b**2)

ang1 = math.acos(a/c)
ang2 = math.atan(a/b)

print("Your 'c' Value (Hypotenuse) is:",c)
print("The interior angle is", round(ang1*(180/3.14159265359),1), "degrees")
print("The interior angle is", round(ang2*(180/3.14159265359),1), "degrees")
print("The interior angle is 90 degrees")
