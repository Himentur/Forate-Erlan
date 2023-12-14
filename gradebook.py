import tkinter as tk
from tkinter import Label, ttk, LabelFrame
import psycopg2
import subprocess

conn = psycopg2.connect(database="enu",
                        user="postgres",
                        host='localhost',
                        password="12345678",
                        port=5432)
cur = conn.cursor()

def back_to_menu():
    window.destroy()
    subprocess.run(['python', 'menu.py'])

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

# Create a Tkinter window
window = tk.Tk()
window.attributes('-fullscreen', True)
window.geometry('1920x1080')
window.config(bg='#689CD2')

frame_table = LabelFrame(window, width=900, height=900, bg='#689CD2', border=0)
frame_table.place(x=50, y=300)

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 9;")
result_back = cur.fetchone()
button_back = tk.Button(window, text=f'{result_back[1]}', bg='#690AB9', font=('Arial', 15), border=0.1, command=back_to_menu)
button_back.place(x=50, y=40)

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 51;")
result_week = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 3;")
result_student_id = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 25;")
result_midterm = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 52;")
result_test = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 53;")
result_subject = cur.fetchone()

tree = ttk.Treeview(frame_table)
# Define columns
tree["columns"] = ("User ID", "week1", "week2", "week3", "week4", "week5", "week6", "week7", "midterm_test", "subject")

# Format columns
tree.column("#0", width=0, stretch=tk.NO)
tree.column("User ID", anchor=tk.W, width=120)
tree.column("week1", anchor=tk.W, width=120)
tree.column("week2", anchor=tk.W, width=120)
tree.column("week3", anchor=tk.W, width=120)
tree.column("week4", anchor=tk.W, width=120)
tree.column("week5", anchor=tk.W, width=120)
tree.column("week6", anchor=tk.W, width=120)
tree.column("week7", anchor=tk.W, width=120)
tree.column("midterm_test", anchor=tk.W, width=120)
tree.column("subject", anchor=tk.W, width=200)
# Create headings
tree.heading("#0", text="", anchor=tk.W)
tree.heading("User ID", text=f'{result_student_id[1]}', anchor=tk.W)
tree.heading("week1", text=f"1 {result_week[1]}", anchor=tk.W)
tree.heading("week2", text=f"2 {result_week[1]}", anchor=tk.W)
tree.heading("week3", text=f"3 {result_week[1]}", anchor=tk.W)
tree.heading("week4", text=f"4 {result_week[1]}", anchor=tk.W)
tree.heading("week5", text=f"5 {result_week[1]}", anchor=tk.W)
tree.heading("week6", text=f"6 {result_week[1]}", anchor=tk.W)
tree.heading("week7", text=f"7 {result_week[1]}", anchor=tk.W)
tree.heading("midterm_test", text=f"{result_midterm[1]} {result_test[1]}", anchor=tk.W)
tree.heading("subject", text=f"{result_subject[1]}", anchor=tk.W)

cur.execute(f"SELECT * FROM math WHERE user_id = {result_user_id[0]};")
result_math = cur.fetchone()
cur.execute(f"SELECT * FROM ai_technologies WHERE user_id = {result_user_id[0]};")
result_ai_technologies = cur.fetchone()
cur.execute(f"SELECT * FROM animal_biotechnology WHERE user_id = {result_user_id[0]};")
result_animal_biotechnology = cur.fetchone()
cur.execute(f"SELECT * FROM economics_and_business WHERE user_id = {result_user_id[0]};")
result_economics_and_business = cur.fetchone()
cur.execute(f"SELECT * FROM energy_efficient_design_of_buildings WHERE user_id = {result_user_id[0]};")
result_energy_efficient_design_of_buildings = cur.fetchone()
cur.execute(f"SELECT * FROM english WHERE user_id = {result_user_id[0]};")
result_english = cur.fetchone()
cur.execute(f"SELECT * FROM journalism WHERE user_id = {result_user_id[0]};")
result_journalism = cur.fetchone()
cur.execute(f"SELECT * FROM pedagogy_and_psychology WHERE user_id = {result_user_id[0]};")
result_pedagogy_and_psychology = cur.fetchone()
cur.execute(f"SELECT * FROM russian WHERE user_id = {result_user_id[0]};")
result_russian = cur.fetchone()
cur.execute(f"SELECT * FROM tourism WHERE user_id = {result_user_id[0]};")
result_tourism = cur.fetchone()
cur.execute(f"SELECT * FROM turkology WHERE user_id = {result_user_id[0]};")
result_turkology = cur.fetchone()


cur.execute(f"SELECT SUM((week1 + week2 + week3 + week4 + week5 + week6 + week7) / 7 + midterm_test) / 2 AS total "
            f"FROM math where user_id = {result_user_id[0]}")
result_total_math = cur.fetchone()
cur.execute(f"SELECT SUM((week1 + week2 + week3 + week4 + week5 + week6 + week7) / 7 + midterm_test) / 2 AS total "
            f"FROM ai_technologies where user_id = {result_user_id[0]}")
result_total_ai_technologies = cur.fetchone()
cur.execute(f"SELECT SUM((week1 + week2 + week3 + week4 + week5 + week6 + week7) / 7 + midterm_test) / 2 AS total "
            f"FROM animal_biotechnology where user_id = {result_user_id[0]}")
result_total_animal_biotechnology = cur.fetchone()
cur.execute(f"SELECT SUM((week1 + week2 + week3 + week4 + week5 + week6 + week7) / 7 + midterm_test) / 2 AS total "
            f"FROM economics_and_business where user_id = {result_user_id[0]}")
result_total_economics_and_business = cur.fetchone()
cur.execute(f"SELECT SUM((week1 + week2 + week3 + week4 + week5 + week6 + week7) / 7 + midterm_test) / 2 AS total "
            f"FROM energy_efficient_design_of_buildings where user_id = {result_user_id[0]}")
result_total_energy_efficient_design_of_buildings = cur.fetchone()
cur.execute(f"SELECT SUM((week1 + week2 + week3 + week4 + week5 + week6 + week7) / 7 + midterm_test) / 2 AS total "
            f"FROM english where user_id = {result_user_id[0]}")
result_total_english = cur.fetchone()
cur.execute(f"SELECT SUM((week1 + week2 + week3 + week4 + week5 + week6 + week7) / 7 + midterm_test) / 2 AS total "
            f"FROM journalism where user_id = {result_user_id[0]}")
result_total_journalism = cur.fetchone()
cur.execute(f"SELECT SUM((week1 + week2 + week3 + week4 + week5 + week6 + week7) / 7 + midterm_test) / 2 AS total "
            f"FROM pedagogy_and_psychology where user_id = {result_user_id[0]}")
result_total_pedagogy_and_psychology = cur.fetchone()
cur.execute(f"SELECT SUM((week1 + week2 + week3 + week4 + week5 + week6 + week7) / 7 + midterm_test) / 2 AS total "
            f"FROM russian where user_id = {result_user_id[0]}")
result_total_russian = cur.fetchone()
cur.execute(f"SELECT SUM((week1 + week2 + week3 + week4 + week5 + week6 + week7) / 7 + midterm_test) / 2 AS total "
            f"FROM tourism where user_id = {result_user_id[0]}")
result_total_tourism = cur.fetchone()
cur.execute(f"SELECT SUM((week1 + week2 + week3 + week4 + week5 + week6 + week7) / 7 + midterm_test) / 2 AS total "
            f"FROM turkology where user_id = {result_user_id[0]}")
result_total_turkology = cur.fetchone()


# Insert data into the table
data = [result_math, result_ai_technologies, result_animal_biotechnology, result_economics_and_business, result_energy_efficient_design_of_buildings,
        result_english, result_journalism, result_pedagogy_and_psychology, result_russian, result_tourism, result_turkology]

for row in data:
    tree.insert("", tk.END, values=row)

# Pack the Treeview widget
tree.pack(expand=True, fill=tk.BOTH)



label_result_math = tk.Label(window, borderwidth=10, bg='yellow', text=f'{result_math[9]}', font=('Arial', 15))
label_result_math.place(x=190, y=10)
label_result_math_total = tk.Label(window, borderwidth=10, bg='red', text=f'{result_total_math[0]}', font=('Arial', 30))
label_result_math_total.place(x=190, y=55)

label_result_ai_technologies = tk.Label(window, borderwidth=10, bg='yellow', text=f'{result_ai_technologies[9]}', font=('Arial', 15))
label_result_ai_technologies.place(x=300, y=10)
label_result_ai_technologies_total = tk.Label(window, borderwidth=10, bg='red', text=f'{result_total_ai_technologies[0]}', font=('Arial', 30))
label_result_ai_technologies_total.place(x=345, y=55)

label_result_animal_biotechnology = tk.Label(window, borderwidth=10, bg='yellow', text=f'{result_animal_biotechnology[9]}', font=('Arial', 15))
label_result_animal_biotechnology.place(x=520, y=10)
label_result_animal_biotechnology_total = tk.Label(window, borderwidth=10, bg='red', text=f'{result_total_animal_biotechnology[0]}', font=('Arial', 30))
label_result_animal_biotechnology_total.place(x=590, y=55)

label_result_economics_and_business = tk.Label(window, borderwidth=10, bg='yellow', text=f'{result_economics_and_business[9]}', font=('Arial', 15))
label_result_economics_and_business.place(x=770, y=10)
label_result_economics_and_business_total = tk.Label(window, borderwidth=10, bg='red', text=f'{result_total_economics_and_business[0]}', font=('Arial', 30))
label_result_economics_and_business_total.place(x=855, y=55)

label_result_energy_efficient_design_of_buildings = tk.Label(window, borderwidth=10, bg='yellow', text=f'{result_energy_efficient_design_of_buildings[9]}', font=('Arial', 15))
label_result_energy_efficient_design_of_buildings.place(x=1070, y=10)
label_result_energy_efficient_design_of_buildings_total = tk.Label(window, borderwidth=10, bg='red', text=f'{result_total_energy_efficient_design_of_buildings[0]}', font=('Arial', 30))
label_result_energy_efficient_design_of_buildings_total.place(x=1200, y=55)

label_result_english = tk.Label(window, borderwidth=10, bg='yellow', text=f'{result_english[9]}', font=('Arial', 15))
label_result_english.place(x=150, y=800)
label_result_english_total = tk.Label(window, borderwidth=10, bg='red', text=f'{result_total_english[0]}', font=('Arial', 30))
label_result_english_total.place(x=200, y=733)

label_result_journalism = tk.Label(window, borderwidth=10, bg='yellow', text=f'{result_journalism[9]}', font=('Arial', 15))
label_result_journalism.place(x=380, y=800)
label_result_journalism_total = tk.Label(window, borderwidth=10, bg='red', text=f'{result_total_journalism[0]}', font=('Arial', 30))
label_result_journalism_total.place(x=405, y=733)

label_result_pedagogy_and_psychology = tk.Label(window, borderwidth=10, bg='yellow', text=f'{result_pedagogy_and_psychology[9]}', font=('Arial', 15))
label_result_pedagogy_and_psychology.place(x=550, y=800)
label_result_pedagogy_and_psychology_total = tk.Label(window, borderwidth=10, bg='red', text=f'{result_total_pedagogy_and_psychology[0]}', font=('Arial', 30))
label_result_pedagogy_and_psychology_total.place(x=645, y=733)

label_result_russian = tk.Label(window, borderwidth=10, bg='yellow', text=f'{result_russian[9]}', font=('Arial', 15))
label_result_russian.place(x=850, y=800)
label_result_russian_total = tk.Label(window, borderwidth=10, bg='red', text=f'{result_total_russian[0]}', font=('Arial', 30))
label_result_russian_total.place(x=905, y=733)

label_result_tourism = tk.Label(window, borderwidth=10, bg='yellow', text=f'{result_tourism[9]}', font=('Arial', 15))
label_result_tourism.place(x=1070, y=800)
label_result_tourism_total = tk.Label(window, borderwidth=10, bg='red', text=f'{result_total_tourism[0]}', font=('Arial', 30))
label_result_tourism_total.place(x=1083, y=733)

label_result_turkology = tk.Label(window, borderwidth=10, bg='yellow', text=f'{result_turkology[9]}', font=('Arial', 15))
label_result_turkology.place(x=1190, y=800)
label_result_turkology_total = tk.Label(window, borderwidth=10, bg='red', text=f'{result_total_turkology[0]}', font=('Arial', 30))
label_result_turkology_total.place(x=1210, y=733)

# Run the Tkinter event loop
window.mainloop()