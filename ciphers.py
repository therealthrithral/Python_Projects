text = 'Hello Zaira'
shift = 3
custom_key = 'python'


def caesar(message, offset, direction):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text_caesar = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text_caesar += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            encrypted_text_caesar += alphabet[new_index]
    return encrypted_text_caesar


def vigenere(message, key, direction):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            # Find the right key character to encode
            key_char = key[key_index % len(key)]
            key_index += 1
            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text


encrypted_vigenere = vigenere(text, custom_key, 1)
print('encrypted_vigenere:', encrypted_vigenere)

encrypted_caesar = caesar(text, shift, 1)
print('encrypted_caesar:', encrypted_caesar)

decrypted_vigenere = vigenere(encrypted_vigenere, custom_key, -1)
print('decrypted_vigenere', decrypted_vigenere)

decrypted_caesar = caesar(encrypted_caesar, shift, -1)
print('decrypted_caesar', decrypted_caesar)
