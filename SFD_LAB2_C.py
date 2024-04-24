
print("Available Currencies: A)USD B)CAD C)YEN")
amount = float(input("Enter transaction amount: "))
currency = input("Transaction currency: ")
convert_to = input("Currency to convert to: ")

if currency == "A":
    if convert_to == "A":
        print("Conversion not needed...")
    elif convert_to == "B":
        converted_value = amount * 1.24
        print(f"Converted value: {round(converted_value, 2)} CAD")
    elif convert_to == "C":
        converted_value = amount * 108.59
        print(f"Converted value: {round(converted_value, 2)} YEN")
elif currency == "B":
    if convert_to == "A":
        converted_value = amount / 1.24
        print(f"Converted value: {round(converted_value, 2)} USD")
    elif convert_to == "B":
        print("Conversion not needed...")
    elif convert_to == "C":
        converted_value = (amount / 1.24) * 108.59
        print(f"Converted value: {round(converted_value, 2)} YEN")
elif currency == "C":
    if convert_to == "C":
        print("Conversion not needed...")
    elif convert_to == "A":
        converted_value = amount / 108.59
        print(f"Converted value: {round(converted_value, 2)} USD")
    elif convert_to == "B":
        converted_value = (amount / 108.59) * 1.24
        print(f"Converted value: {round(converted_value, 2)} CAD")