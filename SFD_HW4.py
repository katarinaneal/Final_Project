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

def decode_rle(rle_data):
    flat_data = []
    for i in range(0, len(rle_data), 2):
        count = rle_data[i]
        value = rle_data[i+1]
        flat_data.extend([value]*count)
    return flat_data

def to_hex_string(data):
    strg = ""
    for i in data:
        h = hex(i)
        strg += h[2:]
    return strg

def count_runs(flat_data):
    runs = 0
    if len(flat_data) == 0:
        return runs

    elem = flat_data[0]
    count = 1
    runs = 1

    for i in range(1, len(flat_data)):
        if count == 15:
            runs += 1
            elem = flat_data[i]
            count = 1
        elif elem != flat_data[i]:
            runs += 1
            elem = flat_data[i]
            count = 1
        else:
            count += 1

    return runs

def encode_rle(flat_data):
    n = len(flat_data)
    i = 0
    result = []

    while i < n:
        count = 1
        while (i + 1 < n and flat_data[i] == flat_data[i + 1]):
            count += 1
            if count == 15:
                i += 1
                break
            i += 1
        if (i == n):
            result.extend([int(count), flat_data[i - 1]])
        else:
            result.extend([int(count), flat_data[i]])
        i += 1

    return result

def get_decoded_length(rle_data):
    length = 0
    for i in range(0, len(rle_data), 2):
        length += rle_data[i]
    return length

def string_to_data(data_string):
    byte_data = []
    for char in data_string:
        byte = int(char, 16)
        byte_data.append(byte)
    return byte_data


def to_rle_string(rle_data):
    # Initializing rle_string.
    rle_string = ""

    # Looping through the rle_data list in steps of 2.
    for i in range(0, len(rle_data), 2):
        # Concatenating run length (in decimal) with rle_string.
        rle_string += str(rle_data[i])

        # Concatenating run value (after converting it into hexadecimal) with rle_string.
        rle_string += hex(rle_data[i + 1])[-1]

        # Concatenating ":" delimiter with rle_string.
        if (i != len(rle_data) - 2):
            rle_string += ":"

            # Returning rle_string.
    return rle_string


def string_to_rle(rle_string):
    rle_data = []
    lst = rle_string.split(":")
    for element in lst:
        run_length = int(element[0:-1])
        run_value = int(element[-1], 16)
        rle_data.append(run_length)
        rle_data.append(run_value)
    return rle_data

def display_flat_hex_data(image_data):
    if image_data:
        hex_data = to_hex_string(image_data)
        print("Flat hex values:", hex_data)
    else:
        print("Flat hex values: (no data)")

def decode_rle_hex_string(hex_str):
    rle_data = []
    for i in range(0, len(hex_str), 2):
        count = int(hex_str[i], 16)
        value = int(hex_str[i + 1], 16)
        rle_data.extend([count, value])
    return rle_data

def decode_flat_data_hex_string(hex_str):
    byte_data = []
    for i in range(0, len(hex_str), 2):
        byte = int(hex_str[i:i+2], 16)
        byte_data.append(byte)
    return byte_data


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
            image_data = decode_rle_hex_string(hex_str)

        elif option == 5:
            hex_str = input("Enter the hex string holding flat data: ")
            image_data = decode_flat_data_hex_string(hex_str)
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
                print("RLE representation:", to_rle_string(image_data))
        elif option == 8:
            if image_data is None:
                print("RLE hex values: (no data)")
            else:
                rle_data = encode_rle(image_data)
                rle_hex_str = to_hex_string(rle_data)
                print("RLE hex values:", rle_hex_str)
        elif option == 9:
            display_flat_hex_data(image_data)
        else:
            print("Error! Invalid input.")

if __name__ == "__main__":
    main()