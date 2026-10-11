import mathutils as m

print("Calculating Perimeter of Rectangle")
l = int(input("Enter length:"))
b = int(input("Enter bredth:"))
p = m.perimeter(l,b)
print("peimeter of rectangle is",p)

print("Calculating Area of Circle")
r = int(input("Enter radius "))
a = m.area(r)
print("area of circle is",a)