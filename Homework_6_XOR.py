"""Exclusive disjunction.
    
    Input arguments: the message is read from the file,
        key, must be string.
        If the key is not entered, it is generated automatically.
    Output: encrypted message is written to the file.
    """
import random
import mymodule as m

input_str = m.read_from_file()
encryption_key = m.txt("""Введите ключ 
    (Enter - ключ сгенерируется автоматически):""")

if not encryption_key:
    encryption_key = ""
    for i in range(random.randint(1, len(input_str))):
        key = random.choice("""0123456789abcdefghijklmnopqrstuvwxyz
            ABCDEFGHIJKLMNOPQRSTUVWXYZ""")
        encryption_key += key

    print(f"Вы не ввели ключ, держите наш:\n{encryption_key}")
    
encryption_key = bytearray(encryption_key, "utf-8")
encrypted = bytearray()
 
length = len(encryption_key)
for i in range(0, len(input_str)):
    encrypted.append(input_str[i] ^ encryption_key[i % len(encryption_key)])

m.write_to_file(encrypted)