def encode(password):
    new_pass = ""
    for char in password:
        new_pass += str(int(char) + 3)
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
