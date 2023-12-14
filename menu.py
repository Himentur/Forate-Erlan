import tkinter as tk
from tkinter import Label, PhotoImage, LabelFrame, ttk
from PIL import Image, ImageTk
import psycopg2
import subprocess

conn = psycopg2.connect(database="enu",
                        user="postgres",
                        host='localhost',
                        password="12345678",
                        port=5432)
cur = conn.cursor()

def exit_button():
    window.destroy()

def personal_data():
    window.destroy()
    subprocess.run(['python', 'personal_data.py'])

def schedule():
    window.destroy()
    subprocess.run(['python', 'schedule.py'])

def calendar():
    window.destroy()
    subprocess.run(['python', 'calendar.py'])

def gradebook():
    window.destroy()
    subprocess.run(['python', 'gradebook.py'])

window = tk.Tk()
window.attributes('-fullscreen', True)
window.geometry('1920x1080')

#create background image and place it
image_bg = Image.open("C:/Users/Yerlan/OneDrive/Рабочий стол/Education"
                      "/2_cource/Python+SQL/pictures/gold background.png")
photo_bg = ImageTk.PhotoImage(image_bg)
label_bg = Label(window, image=photo_bg)
label_bg.place(x=0, y=0)

# Create a frame
frame1 = LabelFrame(window, width=1700, height=770, bg='#689CD2', border=0)
frame1.pack(side='bottom')

# Import Image
import_personal_data_image = Image.open("C:/Users/Yerlan/OneDrive/Рабочий стол/Education/2_cource/Python+SQL/pictures/personal_data.png")
image_personal = ImageTk.PhotoImage(import_personal_data_image)
import_schedule_image = Image.open("C:/Users/Yerlan/OneDrive/Рабочий стол/Education/2_cource/Python+SQL/pictures/schedule.png")
image_schedule = ImageTk.PhotoImage(import_schedule_image)
import_academic_calendar_image = Image.open("C:/Users/Yerlan/OneDrive/Рабочий стол/Education/2_cource/Python+SQL/pictures/calendar.png")
image_academic_calendar = ImageTk.PhotoImage(import_academic_calendar_image)
import_gradebook_image = Image.open("C:/Users/Yerlan/OneDrive/Рабочий стол/Education/2_cource/Python+SQL/pictures/gradebook.png")
image_gradebook = ImageTk.PhotoImage(import_gradebook_image)
import_gpa_calculator_image = Image.open("C:/Users/Yerlan/OneDrive/Рабочий стол/Education/2_cource/Python+SQL/pictures/calculator.png")
image_gpa_calculator = ImageTk.PhotoImage(import_gpa_calculator_image)
import_library_image = Image.open("C:/Users/Yerlan/OneDrive/Рабочий стол/Education/2_cource/Python+SQL/pictures/library.png")
image_library = ImageTk.PhotoImage(import_library_image)

# Create buttons
button_personal = tk.Button(frame1, image=image_personal, border=0.1, command=personal_data)
button_schedule = tk.Button(frame1, image=image_schedule, border=0.1, command=schedule)
button_academic_calendar = tk.Button(frame1, image=image_academic_calendar, border=0.1, command=calendar)
button_gradebook = tk.Button(frame1, image=image_gradebook, border=0.1, command=gradebook)
button_gpa_calculator = tk.Button(frame1, image=image_gpa_calculator, border=0.1)
button_library = tk.Button(frame1, image=image_library, border=0.1)

# Selected language at the previous page
with open("selected_lang.txt", "r", encoding='utf-8') as file:
    selected_option = file.read()
    if selected_option == 'Қазақ тілі':
        selected_option = 'kaz'
    elif selected_option == 'Русский язык':
        selected_option = 'rus'
    elif selected_option == 'English language':
        selected_option = 'eng'
with open("data.txt", "r") as file:
    selected_user_id = file.read()
    cur.execute(f"SELECT * FROM enu_students WHERE user_id = {selected_user_id};")
    result_user_id = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 8;")
result_welcome = cur.fetchone()
label_username_hello = tk.Label(window, borderwidth=20, bg='#689CD2', fg='#FFFD73', text=f'{result_welcome[1]}, {result_user_id[1]}', font=('Arial', 25))
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 2;")
result_exit = cur.fetchone()
button_exit = tk.Button(window, width=12, text=f'{result_exit[1]}', bg='#FF4E40', fg='white', activebackground='#689CD2',
                        activeforeground='#FFFC00', border=0, font=('Arial', 18), command=exit_button)

# Place of all elements
label_username_hello.place(x=255, y=160)
button_exit.place(x=1107, y=197)
button_personal.grid(row=0, column=1, pady=20, padx=30)
button_schedule.grid(row=0, column=2, pady=20, padx=30)
button_academic_calendar.grid(row=0, column=3, pady=20, padx=30)
button_gradebook.grid(row=1, column=1, pady=20, padx=30)
button_gpa_calculator.grid(row=1, column=2, pady=20, padx=30)
button_library.grid(row=1, column=3, pady=20, padx=30)

window.mainloop()
