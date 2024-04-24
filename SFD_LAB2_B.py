
WaterUsage = float(input("Enter your water usage in gallons: "))
gal = WaterUsage / 1000

if 0 <= WaterUsage <= 5999:
    cost = gal * 2.35
elif 6000 <= WaterUsage <= 20000:
    cost = ((WaterUsage - 5999) * (3.75) / 1000) + 5999 * 2.35 / 1000
else:
    cost = ((WaterUsage - 20000) * (6) / 1000) +  (5999 * 2.35 / 1000) + 14000 * 3.75 / 1000
print(f"Money owed: ${round(cost,2)}")


