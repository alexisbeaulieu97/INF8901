
alphabet = []
for i in range(ord('a'), ord('z') + 1):
    alphabet.append(chr(i))

def caesar_encrypt(key: int, data: str):
    result = ""
    for element in data:
        if element == " ":
            result += " "
        elif element.isupper():
            result += alphabet[(ord(element.lower()) + key - ord('a')) % len(alphabet)].upper()
        else:
            result += alphabet[(ord(element) + key - ord('a')) % len(alphabet)]


def caesar_decrypt(key: int, data: str):
    result = ""
    for element in data:
        if element == " ":
            result += " "
        elif element.isupper():
            result += alphabet[(ord(element.lower()) - key - ord('a')) % len(alphabet)].upper()
        else:
            result += alphabet[(ord(element) - key - ord('a')) % len(alphabet)]


encrypted = caesar_encrypt(1, "Ceci est un test")
decrypted = caesar_decrypt(1, "Dfdj ftu vo uftu")

print(encrypted)  # Dfdj ftu vo uftu
print(decrypted)  # Ceci est un test
