def hex_char_decode(digit):
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    digit = digit.upper()

    if digit in hex_dict:
        return hex_dict[digit]
    else:
        return None

def hex_string_decode(hex_string):
    result = 0
    if hex_string[0] == "0" and hex_string[1] == "x":
        hex_string = hex_string[2:]
    for digit in hex_string:
        decoded_digit = hex_char_decode(digit)
        if decoded_digit is None:
            return None

        result = (result << 4) | decoded_digit

    return result


def binary_string_decode(binary_string):
    result = 0

    if binary_string[0] == "0" and binary_string[1] == "b":
        binary_string = binary_string[2:]
    for digit in binary_string:
        if digit not in ('0', '1'):
            return None

        result = (result << 1) | int(digit)

    return result


def binary_to_hex(binary_string):
    decimal_value = binary_string_decode(binary_string)
    if decimal_value is None:
        return None

    hex_string = hex(decimal_value).upper()

    return hex_string[2:]


def main():
    while True:
        print("\nDecoding Menu\n"
              "-------------\n"
              "1. Decode hexadecimal\n"
              "2. Decode binary\n"
              "3. Convert binary to hexadecimal\n"
              "4. Quit")

        user_choice = int(input("Please enter an option: "))

        if user_choice == 1:
            hex_string = input("Please enter the numeric string to convert: ")
            result = hex_string_decode(hex_string)
            if result is not None:
                print(f"Result: {result}")
            else:
                print("Invalid input. Please enter a valid hexadecimal string.")
        elif user_choice == 2:
            binary_string = input("Please enter the numeric string to convert: ")
            result = binary_string_decode(binary_string)
            if result is not None:
                print(f"Result: {result}")
            else:
                print("Invalid input. Please enter a valid binary string.")
        elif user_choice == 3:
            binary_string = input("Please enter the numeric string to convert: ")
            result = binary_to_hex(binary_string)
            if result is not None:
                print(f"Result: {result}")
            else:
                print("Invalid input. Please enter a valid binary string.")
        else:
            break


if __name__ == '__main__':
    main()