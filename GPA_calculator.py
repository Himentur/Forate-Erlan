import tkinter as tk
from tkinter import ttk
import psycopg2

conn = psycopg2.connect(database="enu",
                        user="postgres",
                        host='localhost',
                        password="12345678",
                        port=5432)
cur = conn.cursor()

def calculate():
    try:
        entry_gpa_total = float(entry_gpa.get())
        entry_credit_value = float(entry_credit.get())
        total = entry_gpa_total*entry_credit_value / entry_credit_value
        result_label.config(text=f"Result: {total:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

def back_to_menu():
    window.destroy()

with open("selected_lang.txt", "r", encoding='utf-8') as file:
    selected_option = file.read()
    if selected_option == 'Қазақ тілі':
        selected_option = 'kaz'
    elif selected_option == 'Русский язык':
        selected_option = 'rus'
    elif selected_option == 'English language':
        selected_option = 'eng'

window = tk.Tk()
window.geometry("1920x1080")
window.attributes('-fullscreen', True)
window.configure(bg='#689CD2')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 9;")
result_back = cur.fetchone()
button_back = tk.Button(window, text=f'{result_back[1]}', bg='#690AB9', font=('Arial', 15), border=0.1, command=back_to_menu)
button_back.place(x=50, y=40)
entry_gpa = ttk.Entry(window, font=('Arial', 15), width=10)
entry_credit = ttk.Entry(window, font=('Arial', 15), width=10)
entry_gpa.place(x=650, y=300)
entry_credit.place(x=650, y=350)

button_calculate = tk.Button(window, text="Calculate", border=0.1, command=calculate)
button_calculate.place(x=650, y=400)

result_label = tk.Label(window, text="Result: ", font=('Arial', 15), bg='#689CD2')
result_label.place(x=650, y=450)

window.mainloop()
