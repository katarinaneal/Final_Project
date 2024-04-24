import math
total = 0
numCalc = 0
result = float(round(0,1))
menu_select = 1
select = 1

while menu_select != 0:
    if select > 0 and select < 7:
        print(f"\nCurrent Result: {round(result,2)}\n")

        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average")


    select = int(input("\nEnter Menu Selection: "))

    if select < 0 or select > 7:
        print("\nError: Invalid selection")
        continue

    if select == 7 and numCalc == 0:
         print("Error: No calculations yet to average!")
         continue

    if select == 0:
        print("\nThanks for using this calculator. Goodbye!")
        break

    if select == 7:
        print(f"\nSum of calculation: {round(total,2)}")
        print(f"Number of calculation: {numCalc}")
        average = total / numCalc
        print(f"Average of calculations: {round(average,2)}")

    if select > 0 and select < 7:
        first = float(input("Enter first operand: "))
        second = float(input("Enter second operand: "))

        if select == 1:
            result = first + second
    
        elif select == 2:
            result = first - second

        elif select == 3:
            result = first * second

        elif select == 4:
            result = first / second

        elif select == 5:
            result = first ** second

        elif select == 6:
            result = math.log(first, second)

    total += result
    numCalc +=1