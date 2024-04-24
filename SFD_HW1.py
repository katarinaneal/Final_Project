
print("Available movies today:")
print("A)12 Strong:     1)2:30   2)4:40   3)7:50   4)10:50")
print("B)Coco:          1)12:40  2)3:45")
print("C)The Post:      1)12:45  2)3:35   3)7:05   4)9:55")


choice = input("Movie choice:  ")
showtime = int(input("Showtime:      "))

if choice not in 'ABC' or showtime < 1 or showtime > 4:
    print("Invalid option; please restart app...")
elif choice in 'B' and showtime > 2:
    print("Invalid option; please restart app...")
else:
    adult = int(input("Adult tickets: "))
    kid = int(input("Kid tickets:   "))

    if adult + kid > 30:
        print("Invalid option; please restart app...")
    else:
        if showtime == 1 and (choice == "B" or choice == "C"):
            cost = adult * 11.17 + kid * 8.00
        else:
            cost = adult * 12.45 + kid * 9.68

        print(f"Total cost:    ${round(cost, 2)}")
