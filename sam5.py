def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def encrypt_file():
    with open('secret.txt', 'r') as file:
        content = file.read()
    
    encrypted = caesar_cipher(content, 3)
    
    with open('encrypted.txt', 'w') as file:
        file.write(encrypted)
    
    print("Файл зашифрован!")

encrypt_file()