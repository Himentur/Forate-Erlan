import tkinter as tk
from tkinter import ttk, Tk, Entry, Frame, Label, PhotoImage, LabelFrame
from tkinter import messagebox
import psycopg2
from PIL import Image, ImageTk
from tkinter import LabelFrame
import subprocess


conn = psycopg2.connect(database="enu",
                        user="postgres",
                        host='localhost',
                        password="12345678",
                        port=5432)
cur = conn.cursor()

def exit_button():
    window.destroy()


def check_enter(event):
    if event.keysym == "Return":
        authenticate()


def show_selected_option(selected_option):
    selected_option = selected_option_var.get()
    with open("selected_lang.txt", "w", encoding="utf-8") as file:
        file.write(f'{selected_option}')
    if selected_option == 'Қазақ тілі':
        selected_option = 'kaz'
    elif selected_option == 'Русский язык':
        selected_option = 'rus'
    elif selected_option == 'English language':
        selected_option = 'eng'

    cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 2;")
    result_exit = cur.fetchone()
    button_exit.config(text=f'{result_exit[1]}')

    cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 3;")
    label_username_result = cur.fetchone()
    label_username.config(text=f'{label_username_result[1]}')

    cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 4;")
    label_password_result = cur.fetchone()
    label_password.config(text=f'{label_password_result[1]}')

    cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 5;")
    combobox_result = cur.fetchone()
    combobox.set(combobox_result[1])

    cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 7;")
    entry_name_result = cur.fetchone()
    entry_username.delete(0, tk.END)
    entry_username.insert(0, f'{entry_name_result[1]}')


def authenticate():
    username = entry_username.get()
    password = entry_password.get()

    if not username.isdigit():
        messagebox.showerror("Қателік/Ошибка/Error", "Пайдаланушы аты Студент ID болуы қажет. Мысалы: 404\n"
                                                     "Имя пользователя должно быть ID студента. Пример: 404\n"
                                                     "Username should be student ID. Example: 404")
    else:
        cur.execute(f"SELECT user_id, user_password FROM user_id_and_password WHERE user_id = {username};")
        result = cur.fetchone()
        if result and password == result[1]:
            with open("data.txt", "w") as file:
                file.write(f'{result[0]}')
            window.destroy()
            subprocess.run(['python', 'menu.py'])
        else:
            messagebox.showerror("Қателік/Ошибка/Error", "Бұрыс құпиясөз\nНеверный пароль\nInvalid password")


def on_enter_username(event):
    entry_username.delete(0, 'end')


def on_leave_username(event):
    name = entry_username.get()
    if name == '':
        entry_username.insert(0, 'Username')


def on_enter_password(event):
    entry_password.delete(0, 'end')


def on_leave_password(event):
    enter = entry_password.get()
    if enter == '':
        entry_password.insert(0, 'Password')


# create a main window
window = tk.Tk()
window.title('Forate')
window.geometry("1500x800")
window.attributes('-fullscreen', True)

# create a frame
frame1 = LabelFrame(window, width=600, height=600, border=0)
frame1.pack(side="left")
frame2 = LabelFrame(window, width=900, height=600, border=0)
frame2.pack(side="right")

# create style for entry
style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 12, "bold"))
style.map("Custom.TButton", foreground=[('focus', 'red')], background=[('focus', 'red')])

# import images
logo_image = Image.open("C:/Users/Yerlan/OneDrive/Рабочий стол/Education/2_cource/Python+SQL/pictures/LOGO_289x90.png")
logo_photo = ImageTk.PhotoImage(logo_image)
main_image = Image.open(
    "C:/Users/Yerlan/OneDrive/Рабочий стол/Education/2_cource/Python+SQL/pictures/login_ill_1076x697.png")
main_photo = ImageTk.PhotoImage(main_image)

# combobox
options = ['Қазақ тілі', 'Русский язык', 'English language']
selected_option_var = tk.StringVar()
combobox = ttk.Combobox(frame1, textvariable=selected_option_var, values=options, font=('Arial', 12))
combobox.set('Change Your language')
combobox.bind("<<ComboboxSelected>>", show_selected_option)

# create button, entry and so on
button_exit = ttk.Button(frame1, text='Exit', style="Custom.TButton", command=exit_button)
label_username = tk.Label(frame1, text='User ID', font=('Arial', 15))
label_password = tk.Label(frame1, text='Password', font=('Arial', 15))
entry_username = ttk.Entry(frame1, font=('Arial', 15))
entry_password = ttk.Entry(frame1, show="*", font=('Arial', 15))
label_logo = tk.Label(frame1, image=logo_photo)
label_main = tk.Label(frame2, image=main_photo)

# Places for elements(button, entry, images)
label_main.pack()
label_logo.pack(pady=20, padx=60)
label_username.pack(pady=20, padx=60)
entry_username.pack(pady=20, padx=60)
label_password.pack(pady=20, padx=60)
entry_password.pack(pady=20, padx=60)
combobox.pack(pady=20, padx=60)
button_exit.pack(pady=20, padx=60)

# button checker on laptop
entry_username.insert(0, 'Username')
entry_password.insert(0, 'Password')
entry_username.bind('<FocusIn>', on_enter_username)
entry_username.bind('<FocusOut>', on_leave_username)
entry_password.bind('<FocusIn>', on_enter_password)
entry_password.bind('<FocusOut>', on_leave_password)
entry_password.bind('<KeyPress>', check_enter)

window.mainloop()
