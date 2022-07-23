from cryptography.fernet import Fernet


dirname = "Files"

def _write_key():
    key = Fernet.generate_key()
    with open('WorkingWindow/Cryptography/SecretKey.txt', 'wb') as key_file: 
        key_file.write(key)

        
def load_key():
    return open('WorkingWindow/Cryptography/SecretKey.txt', 'rb').read()


def encrypt_file(filename, key):
    f = Fernet(key)
    with open(f"{dirname}/{filename}", 'rb') as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
    with open(f"{dirname}/{filename}", 'wb') as file:
        file.write(encrypted_data) 
        
        
def re_encrypt_file(filename, new_data, key):
    f = Fernet(key)
    with open(f"{dirname}/{filename}", 'wb') as file:
        encrypted_data = f.encrypt(new_data)
        file.write(encrypted_data)
        

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(f"{dirname}/{filename}", 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(f"{dirname}/{filename}", 'wb') as file:
        file.write(decrypted_data)


def get_decrypted_text(filename, key):
    f = Fernet(key)
    with open(f"{dirname}/{filename}", 'rb') as file:
        encrypted_data = file.read()
    return f.decrypt(encrypted_data)


# if __name__ == "__main__":
#     from os import listdir
    
#     file_list = listdir(dirname)
    
#     for f in file_list:
#         encrypt_file(f, load_key())
        

    
