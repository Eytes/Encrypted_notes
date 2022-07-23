import hashlib
from .Logs import logs
    

def sing_in(login, password) -> bool:
    password = hashlib.sha256(password.encode())
    try:
        if logs[login] == password.hexdigest():
            return True
        return False # неправильный пароль
    except KeyError: # неправильный логин
        return False
    
    
if __name__ == "__main__":
    login = input("Введите логин: \n")
    password = input("Введите пароль: \n")

    if sing_in(login, password):
        print("access")
    else:
        print("Not access")




    
    
    
    