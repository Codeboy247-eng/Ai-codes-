import tkinter as tk

# Caesar Cipher Function
def decrypt_caesar():
    encrypted_text = entry_text.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        result_label.config(text="Shift must be a number.")
        return
    
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
    
            if char.islower():
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted_text += char 
    
    result_label.config(text=f"🔓 Decrypted: {decrypted_text}")


window = tk.Tk()
window.title("Caesar Cipher Decryptor")
window.geometry("400x250")


title_label = tk.Label(window, text="🕵️ Caesar Cipher GUI Decryptor", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Encrypted Text Entry
tk.Label(window, text="Enter Encrypted Text:").pack()
entry_text = tk.Entry(window, width=30)
entry_text.pack(pady=5)

# Shift Entry
tk.Label(window, text="Enter Shift Number:").pack()
entry_shift = tk.Entry(window, width=10)
entry_shift.pack(pady=5)

# Decrypt Button
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_caesar)
decrypt_button.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="", fg="green", font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)

# Run the GUI
window.mainloop()
