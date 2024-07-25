def encode(password):
    new_pass = ""
    for char in password:
        num = int(char) + 3
        if (num > 9):
            new_pass += str(num % 10)
        else:
            new_pass += str(num)
    return new_pass

def decode(password): # Takes a string of numbers, and returns a string of the numbers after adding 3
    decode_dict = {
        "4": "1",
        "5": "2",
        "6": "3",
        "7": "4",
        "8": "5",
        "9": "6",
        "0": "7",
        "1": "8",
        "2": "9",
        "3": "0"
    }

    enc_arr = list(password)
    arr = list()

    for char in enc_arr:
        new_char = decode_dict[char]
        # print(new_char)
        arr.append(new_char)

    return "".join(arr)

def menu():
    print("Menu\n-------------"
          ,"\n1. Encode"
          ,"\n2. Decode"
          ,"\n3. Quit")

def main():
    new_password = ""
    while (True):
        menu()
        option = int(input("\nPlease enter an option: "))
        match option:
            case 1:
                password = input("Please enter the password to encode: ")
                new_password += encode(password)
                print("Your password has been encoded and stored!\n")
            case 2:
                password = decode(new_password)
                print(f"The encoded password is {new_password}, and the original password is {password}.")
            case 3:
                break

if __name__ == "__main__":
    main()
