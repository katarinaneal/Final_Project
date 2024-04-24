import math

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

perimeter = 2 * length + 2 * width
area = length * width
diagonal = math.sqrt(length ** 2 + width ** 2)

print(f"Rectangle perimeter: {round(perimeter,2)}")
print(f"Rectangle area: {round(area,2)}")
print(f"Rectangle diagonal: {round(diagonal,2)}")
