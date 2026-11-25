ALPHABET_SIZE = 26

# read a messade and a key
message: str = input("Message: ")
key: int = int(input("Key: "))

#==============================================================
# encription loop
#==============================================================

ciphertext: str = ""

for character in message:

    # check whether the character is an uppercase letter (A-Z)
    if "A" <= character <= "Z":
        shifted = ord(character) + key
        if shifted > ord("Z"):
            shifted -= ALPHABET_SIZE
        ciphertext += chr(shifted) 

    # check whether the character is an lowercase letter (a-z)
    elif  "a" <= character <= "z": 
        shifted = ord(character) + key
        if shifted > ord("z"):
            shifted -= ALPHABET_SIZE
        ciphertext += chr(shifted)

    # unchanged non-alphabetic characters
    else:
        ciphertext += character


# print encrypted message
print("Ciphertext:", ciphertext)

#==============================================================
# decription loop
#==============================================================

plaintext: str = ""

for character in ciphertext:

    # check whether the character is an lowercase letter (A-Z)
    if "A" <= character <= "Z":
        shifted = ord(character) - key
        if shifted < ord("A"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted) 

    # check whether the character is an lowercase letter (a-z)
    elif  "a" <= character <= "z":
        shifted = ord(character) - key
        if shifted < ord("a"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted)

    # unchanged non-alphabetic characters
    else:
        plaintext += character


# print decrypted message
print("Plaintext:", plaintext)


# check if the message equals the plantext
assert message == plaintext, "The encription-decription doesn't close"
