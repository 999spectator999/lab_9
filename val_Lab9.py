def encode(password):
    new_pass = ""
    for char in password:
        new_pass += str(int(char) + 3)
    return new_pass

def decode(password):
    pass