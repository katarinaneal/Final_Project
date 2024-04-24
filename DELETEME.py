from console_gfx import ConsoleGfx

def display_menu():
    print("\nRLE Menu\n--------")
    print('0. Exit')
    print('1. Load File')
    print('2. Load Test Image')
    print('3. Read RLE String')
    print('4. Read RLE Hex String')
    print('5. Read Data Hex String')
    print('6. Display Image')
    print('7. Display RLE String')
    print('8. Display Hex RLE Data')
    print('9. Display Hex Flat Data')

def display_flat_hex_data(image_data):
    if image_data is None:
        return "(no data)"
    else:
        return to_hex_string(image_data)

def main():
    print('Welcome to the RLE image encoder! \n')
    print('Displaying Spectrum Image:')
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    image_data = None

    while True:
        display_menu()
        option = int(input('\nSelect a Menu Option: '))
        if option == 0:
            break
        elif option == 1:
            file_name = input('Enter the name of the file: ')
            image_data = ConsoleGfx.load_file(file_name)
        elif option == 2:
            image_data = ConsoleGfx.test_image
            print('Test image data loaded.')
        elif option == 3:
            input_data = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(input_data))
        elif option == 4:
            hex_str = input("Enter the hex string holding RLE data: ")
            image_data = ConsoleGfx.decode_rle_hex_string(hex_str)
        elif option == 5:
            hex_str = input("Enter the hex string holding flat data: ")
            image_data = ConsoleGfx.decode_flat_data_hex_string(hex_str)
        elif option == 6:
            if image_data is None:
                print("Displaying image...")
                print("(no data)")
            else:
                print("Displaying image...")
                ConsoleGfx.display_image(image_data)
        elif option == 7:
            if image_data is None:
                print("RLE representation: (no data)")
            else:
                ConsoleGfx.display_rle_string(image_data)
        elif option == 8:
            if image_data is None:
                print("RLE hex values: (no data)")
            else:
                ConsoleGfx.display_rle_hex_data(image_data)
        elif option == 9:
            print("Flat hex values:", display_flat_hex_data(image_data))
        else:
            print("Error! Invalid input.")

if __name__ == "__main__":
    main()
