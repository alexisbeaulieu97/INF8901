
alphabet = []
for i in range(ord('a'), ord('z') + 1):
    alphabet.append(chr(i))

def caesar_encrypt(key: int, data: str):
    new_data = ""
    for element in data:
        if element == " ":
            new_data += " "
        elif element.isupper():
            new_data += alphabet[(ord(element.lower()) + key - ord('a')) % len(alphabet)].upper()
        else:
            new_data += alphabet[(ord(element) + key - ord('a')) % len(alphabet)]
    print(new_data)

def caesar_decrypt(key: int, data: str):
    new_data = ""
    for element in data:
        if element == " ":
            new_data += " "
        elif element.isupper():
            new_data += alphabet[(ord(element.lower()) - key - ord('a')) % len(alphabet)].upper()
        else:
            new_data += alphabet[(ord(element) - key - ord('a')) % len(alphabet)]
    print(new_data)


caesar_encrypt(1, "Ceci est un test") # Dfdj ftu vo uftu
caesar_decrypt(1, "Dfdj ftu vo uftu") # Ceci est un test
