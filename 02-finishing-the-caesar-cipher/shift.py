# num=ord("A") # function (build-in)
# print(num)

# letter=chr(82)
# print(letter)

# key=5
# plaintext_letter="M"

# shift_number = ord(plaintext_letter) + key
# letter=chr(shift_number)

# print(letter)

# ciphertext_letter="P"

# assert letter == ciphertext_letter

# output -> print
# input -> input

ALPHABET_SIZE = 26

message: str = input("Message: ")
key: int = int(input("Key: "))

# print(type(message))
# print(type(key))

# 'str' -> STRING (words)
# 'int' -> INTERGER (whole number)

ciphertext: str = ""

# encription loop
for character in message:
    # check whether our character is between "A" and "Z"
    # if character >= "A" and character <= "Z":
    if "A" <= character <= "Z":
        shifted = ord(character)+key
        if shifted > ord("Z"):
            shifted -= ALPHABET_SIZE
        ciphertext += chr(shifted) 
    else:
        ciphertext += character

print("Chipertext: ", ciphertext)

plaintext:str = ""

# decription loop
for character in ciphertext:
    # check whether our character is between "A" and "Z"
    # if character >= "A" and character <= "Z":
    if "A" <= character <= "Z":
        shifted = ord(character)-key
        if shifted < ord("A"):
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted) 
    else:
        plaintext += character



print("Plaintext: ", plaintext)

# check if the message equals the plantext
assert message == plaintext, "The encription-decription doesn't close"


