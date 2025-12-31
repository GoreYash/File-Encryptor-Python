from cryptography.fernet import Fernet
import os

def generate(path):
    try:
        if (os.path.getsize(path) == 0):
            with open(path, 'wb') as file:
                key = Fernet.generate_key()
                file.write(key)
                print("Key created successfully")
    except FileNotFoundError:
        with open(path, 'w') as f_empty:
            pass
        generate(path)

generate('secret.key')