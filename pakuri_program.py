from pakuri import Pakuri
from pakudex import Pakudex

def display_menu():
    print('\nPakudex Main Menu\n-----------------')
    print('1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit')

def main():
    print('Welcome to Pakudex: Tracker Extraordinaire!')
    while True:
        try:
            pakudex_capacity = int(input('Enter max capacity of the Pakudex: '))
            if pakudex_capacity > 0:
                print(f'The Pakudex can hold {pakudex_capacity} species of Pakuri.')
                break
            else:
                raise ValueError
        except ValueError:
            print('Please enter a valid size.')

    pakudex_instance = Pakudex(pakudex_capacity)  # Renamed the instance variable
    while True:
        display_menu()
        try:
            print()
            user_choice = int(input('What would you like to do? '))
            if user_choice == 1:
                if pakudex_instance.get_size() > 0:  # Using the instance variable
                    print('Pakuri In Pakudex:')
                    for idx, species in enumerate(pakudex_instance.get_species_array()):  # Using the instance variable
                        print(f'{idx + 1}. {species}')
                else:
                    print('No Pakuri in Pakudex yet!')
            elif user_choice == 2:
                species_name = input('Enter the name of the species to display: ')
                stats = pakudex_instance.get_stats(species_name)  # Using the instance variable
                if stats:
                    print(f'Species: {species_name}\nAttack: {stats[0]}\nDefense: {stats[1]}\nSpeed: {stats[2]}')
                else:
                    print('Error: No such Pakuri!')
            elif user_choice == 3:
                if pakudex_instance.get_size() < pakudex_instance.get_capacity():  # Using the instance variable
                    species_name = input('Enter the name of the species to add: ')
                    pakudex_instance.add_pakuri(species_name)  # Using the instance variable
                    print(f'Pakuri species {species_name} successfully added!')
                else:
                    print('Error: Pakudex is full!')
            elif user_choice == 4:
                species_name = input('Enter the name of the species to evolve: ')
                if pakudex_instance.evolve_species(species_name):  # Using the instance variable
                    print(f'{species_name} has evolved!')
                else:
                    print('Error: No such Pakuri!')
            elif user_choice == 5:
                pakudex_instance.sort_pakuri()  # Using the instance variable
                print('Pakuri have been sorted!')
            elif user_choice == 6:
                print('Thanks for using Pakudex! Bye!')
                break
            else:
                print('Unrecognized menu selection!')
        except ValueError:
            print('Unrecognized menu selection!')

if __name__ == "__main__":
    main()
