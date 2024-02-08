import sys
import os

# Importe la fonction decrypt_sym_key depuis ./Initialisation/flag1_register.py
current_directory = os.path.dirname(__file__)
initialisation_directory = os.path.join(current_directory, '..', 'Initialisation')
initialisation_directory = os.path.normpath(initialisation_directory)
if initialisation_directory not in sys.path:
    sys.path.append(initialisation_directory)
    
from flag1_register import decrypt_sym_key

if __name__ == "__main__":
    # données du challenge
    encrypted = """U2FsdGVkX1+29XFd2I+IEnjBbrRsDKkGSafinx7U0rCHvJTjdHb1BX+ZtTeFujdr\n"""
    symkey = "Yz134679258"

    try:
        decrypted = decrypt_sym_key(encrypted, symkey)
        print(decrypted)
    except Exception as e:
        print(e)
