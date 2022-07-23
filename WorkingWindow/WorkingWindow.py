from tkinter import *
from tkinter import messagebox as mb
from os import listdir
# from Cryptography import *
from .Cryptography import *


def working_window():     
    def show_content(event):        
        def delete_text():
            text.delete(1.0, END)
            
        def insert_text():
            text.insert(1.0, get_decrypted_text(select_file, load_key()).decode()) 
        
        def set_active_file(select_file):
            nonlocal active_file_name
            
            active_file['text'] = f"Открыт:\t{select_file}"    
            active_file_name = select_file        

        select_file = list_box.get(list_box.curselection()[0])
        set_active_file(select_file)
        delete_text()
        insert_text()
        
    def fill_listbox():
        for fname in list_files:
            list_box.insert(END, fname)
        
    def save_change():
        answer = mb.askyesno(
            f"Изменения в файле {active_file_name}",
            f"Вы хотите сохранить изменения в файле {active_file_name}?"
        )
        
        if answer == True:
            try:
                re_encrypt_file(active_file_name, text.get(1.0, END).encode(), load_key())
                mb.showinfo(
                    "Уведомление",
                    f"Файл {active_file_name} изменен"
                )
            except:
                mb.showwarning(
                    "Уведомление",
                    f"Не удалось сохранить изменения в файл {active_file_name}"    
                )
        
    
    list_files = listdir("Files")
    
    root = Tk()
    root.title()
    root.resizable(False, False)
    
    active_file = Label(root, width=50, text="Пока никакой файл не открыт")
    active_file.grid(row=0, column=1, columnspan=3)
    active_file_name = ''
    
    text = Text(root, height=30, width=50, wrap=WORD)
    text.grid(row=1, column=1, columnspan=3)
    
    list_box = Listbox(root, width=24, selectmode=SINGLE)
    list_box.grid(row=1, column=0)
    fill_listbox()
    list_box.bind("<Double-Button-1>", show_content)
        
    save_button = Button(root, text="Сохранить", command=save_change)
    save_button.grid(row=2, column=4)
    
    root.mainloop()


if __name__ == "__main__":
    working_window()