def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else chr((ord(char) - 65 + shift) % 26 + 65)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted_char = chr((ord(char) - 97 - shift) % 26 + 97) if char.islower() else chr((ord(char) - 65 - shift) % 26 + 65)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

with open("C:/Users/Devanshu/Desktop/Python/PDS Manual/SET-4/plaintext.txt", "r") as file:
    plaintext = file.read()

shift = 3

ciphertext = encrypt(plaintext, shift)
print("Encrypted text:", ciphertext)

decrypted_text = decrypt(ciphertext, shift)
print("Decrypted text:", decrypted_text)

with open("decrypted_plaintext.txt", "w") as file:
    file.write(decrypted_text)
