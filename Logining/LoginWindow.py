from tkinter import *
from tkinter import messagebox as mb
from .SingIn import sing_in


def login_window():
    def check():
        nonlocal access
        if sing_in(login=l.get(), password=p.get()):
            mb.showinfo(
                "Доступ",
                "Успешно"
            )
            root.destroy()
            access = True
        
        else:
            mb.showerror(
                "Доступ",
                "Не верный логин или пароль"
            )

    root = Tk()
    root.resizable(False, False)
    root.title("Авторизация")
    
    access = False


    # поля для ввода логина и пароля
    log_label = Label(root, text="Логин:")
    l = Entry(root, width=30)
    log_label.grid(row=0, column=0)
    l.grid(row=0, column=1, columnspan=4)

    pas_label = Label(root, text="Пароль:")
    p = Entry(root, width=30)
    pas_label.grid(row=1, column=0)
    p.grid(row=1, column=1, columnspan=4)


    # кнопка для проверки правильности введенных данных
    b = Button(root, text="Войти", command=check)
    b.grid(row=2, column=2)


    root.mainloop()
    
    return access


if __name__ == "__main__":
    login_window()