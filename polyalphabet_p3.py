def polyalphabetic_cipher(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""
    
    # Membuat abjad baru berdasarkan kunci
    new_alphabet = ""
    for char in key:
        if char.lower() not in new_alphabet:
            new_alphabet += char.lower()
    for char in alphabet:
        if char not in new_alphabet:
            new_alphabet += char
    
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char_lower = char.lower()
            index = alphabet.index(char_lower)
            encrypted_char = new_alphabet[index]
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        # Spasi tidak dimasukkan dalam hasil enkripsi
        elif char.isspace():
            continue
    
    return encrypted_text

def main():
    plaintext = input("Masukkan Plaintext: ")
    key = input("Masukkan Kunci: ")
    
    encrypted_text = polyalphabetic_cipher(plaintext, key)
    
    print("Hasil Enkripsi:", encrypted_text)

if __name__ == "__main__":
    main()
