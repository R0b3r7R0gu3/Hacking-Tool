import os
import shutil
from cryptography.fernet import Fernet
from getpass import getpass

# ========== File Encrypter / Decrypter ==========
def file_encrypter():
    key = Fernet.generate_key()
    fernet = Fernet(key)
    path = input("Percorso del file da criptare: ")

    if not os.path.isfile(path):
        print("File non trovato.")
        return

    with open(path, 'rb') as f:
        data = f.read()

    encrypted = fernet.encrypt(data)
    with open(path + ".enc", 'wb') as f:
        f.write(encrypted)
    print(f"File criptato con la chiave: {key.decode()}")

    # Salva la chiave in un file sicuro
    with open("passwords.key", 'wb') as keyfile:
        keyfile.write(key)

# ========== Password Manager (con crittografia) ==========
def password_manager():
    try:
        with open("passwords.key", 'rb') as keyfile:
            key = keyfile.read()
        fernet = Fernet(key)
    except FileNotFoundError:
        print("Errore: chiave di crittografia non trovata.")
        return

    action = input("1. Aggiungi password\n2. Visualizza password\nScegli: ")

    if action == "1":
        service = input("Servizio: ")
        username = input("Username: ")
        password = getpass("Password: ")
        encrypted_pw = fernet.encrypt(password.encode())
        with open("passwords.txt", "a") as pwfile:
            pwfile.write(f"{service} | {username} | {encrypted_pw.decode()}\n")
        print("Password salvata.")

    elif action == "2":
        try:
            with open("passwords.txt", "r") as pwfile:
                for line in pwfile:
                    service, username, encrypted_pw = line.strip().split(" | ")
                    decrypted_pw = fernet.decrypt(encrypted_pw.encode()).decode()
                    print(f"Servizio: {service}, Username: {username}, Password: {decrypted_pw}")
        except FileNotFoundError:
            print("Nessuna password salvata.")

# ========== Directory Sync ==========
def dir_sync():
    src = input("Cartella SORGENTE: ")
    dst = input("Cartella DESTINAZIONE: ")
    if not os.path.isdir(src):
        print("Cartella sorgente non valida.")
        return

    try:
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print("Cartelle sincronizzate!")
    except Exception as e:
        print(f"Errore: {e}")
