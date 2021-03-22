import mymodule as m

def XOR(input_str, encryption_key):
    """Exclusive disjunction
    
    Input arguments: message and key, must be string
    Output: encrypted and decrypted strings
    """
    encrypted = ""
    length = len(encryption_key)

    for i in range(0, len(input_str)):
        letter = input_str[i]
        key = encryption_key[i % length]
        encrypted += chr(ord(letter) ^ ord(key))
        
    return encrypted

input_str = (m.text("Введите шифр: "))
input_key = (m.text("Введите ключ: "))

print(f"Введенная строка: {input_str}")
encr_strg = XOR(input_str, input_key)
print(f"Зашифрованная строка: {encr_strg}")
print(f"Расшифрованная строка: {XOR(encr_strg, input_key)}")