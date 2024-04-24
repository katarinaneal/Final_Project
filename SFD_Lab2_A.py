
s1 = int(input("Enter side 1: "))
s2 = int(input("Enter side 2: "))
s3 = int(input("Enter side 3: "))

if s1 ** 2 + s2 ** 2 == s3 ** 2 or s1 ** 2 + s3 ** 2 == s2 ** 2 or s2 ** 2 + s3 ** 2 == s1 ** 2:
    print("This triangle has a right angle!")
else:
    print("This triangle doesn't have a right angle...")
