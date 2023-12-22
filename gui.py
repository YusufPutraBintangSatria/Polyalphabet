import tkinter as tk

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

def encrypt_text():
    plaintext = entry_plaintext.get()
    key = entry_key.get()
    
    encrypted_text = polyalphabetic_cipher(plaintext, key)
    result_label.config(text=f"Hasil Enkripsi: {encrypted_text}")

# Membuat GUI
root = tk.Tk()
root.title("Polyalphabetic Cipher")

# Label dan Entry untuk Plaintext
label_plaintext = tk.Label(root, text="Plaintext:")
label_plaintext.pack()
entry_plaintext = tk.Entry(root)
entry_plaintext.pack()

# Label dan Entry untuk Key
label_key = tk.Label(root, text="Key:")
label_key.pack()
entry_key = tk.Entry(root)
entry_key.pack()

# Tombol untuk Enkripsi
encrypt_button = tk.Button(root, text="Enkripsi", command=encrypt_text)
encrypt_button.pack()

# Label untuk Menampilkan Hasil Enkripsi
result_label = tk.Label(root, text="")
result_label.pack()

# Menjalankan loop GUI
root.mainloop()
