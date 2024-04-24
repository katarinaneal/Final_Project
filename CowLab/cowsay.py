import sys
from heifer_generator import HeiferGenerator
from dragon import Dragon
from ice_dragon import IceDragon


def list_cows():
    return HeiferGenerator.get_cows()


def find_cow(name):
    cows = list_cows()
    for cow in cows:
        if cow.name == name:
            return cow
    return None


def main(args):
    cows = list_cows()

    # List cows
    if args[1] == '-1' or args[1] == '-l':
        print(f"Cows available: {' '.join([cow.name for cow in cows])} ")

    # Pick specific cow
    elif args[1] == '-n':
        cow = find_cow(args[2])
        if cow:
            print()
            message = ' '.join(args[3:])
            print(message + ' ')
            print(cow.image)
            # Check if cow is a Dragon
            if isinstance(cow, Dragon):
                if isinstance(cow, IceDragon):
                    print("This dragon cannot breathe fire.")
                else:
                    print("This dragon can breathe fire.")
        else:
            print(f'Could not find {args[2]} cow!')

    # Print default cow with message
    else:
        print()
        message = ' '.join(args[1:])
        print(message + " ")
        print(cows[0].image)


if __name__ == "__main__":
    main(sys.argv)

