
m1 = float(input("Enter m for Line 1: "))
b1 = float(input("Enter b for Line 1: "))
m2 = float(input("Enter m for Line 2: "))
b2 = float(input("Enter b for Line 2: "))

x = (b2 -b1) / (m1 - m2)
y = m1 * x + b1

print(f"The intersection point is ({round(x,2)},{round(y,2)}) ")

