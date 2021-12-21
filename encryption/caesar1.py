alphabet = []
for i in range(ord("a"), ord("z") + 1):
    alphabet.append(chr(i))


def caesar_encrypt(key: int, data: str):
    result = ""
    for element in data:
        if element == " ":
            result += " "
        elif element.isupper():
            result += alphabet[
                (ord(element.lower()) + key - ord("a")) % len(alphabet)
            ].upper()
        else:
            result += alphabet[(ord(element) + key - ord("a")) % len(alphabet)]
    return result


encrypted = caesar_encrypt(1, "Ceci est un test")

print(encrypted)  # Dfdj ftu vo uftu
