import tkinter as tk
from tkinter import LabelFrame, Label
from PIL import Image, ImageTk
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
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))



window = tk.Tk()
window.attributes('-fullscreen', True)
window.geometry('1600x750')

import_calendar_bg_image = Image.open("C:/Users/Yerlan/OneDrive/Рабочий стол/Education/2_cource/Python+SQL/pictures/gold background.png")
image_calendar_bg = ImageTk.PhotoImage(import_calendar_bg_image)
label_bg = Label(window, image=image_calendar_bg)
label_bg.place(x=0, y=0)

with open("selected_lang.txt", "r", encoding='utf-8') as file:
    selected_option = file.read()
    if selected_option == 'Қазақ тілі':
        selected_option = 'kaz'
    elif selected_option == 'Русский язык':
        selected_option = 'rus'
    elif selected_option == 'English language':
        selected_option = 'eng'
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 9;")
result_back = cur.fetchone()
button_back = tk.Button(window, text=f'{result_back[1]}', bg='#690AB9', font=('Arial', 15), border=0.1, command=back_to_menu)
button_back.place(x=50, y=40)

frame_autumn = LabelFrame(window, width=750, height=700, bg='#689CD2', border=0)
frame_autumn.place(x=50, y=100)

frame_spring = LabelFrame(window, width=750, height=700, bg='#689CD2', border=0)
frame_spring.place(x=800, y=40)

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 19;")
result_autumn_semester = cur.fetchone()
label_autumn_semester = tk.Label(frame_autumn, borderwidth=10, bg='yellow', text=f'{result_autumn_semester[1]} 🌞', font=('Arial', 15))
label_autumn_semester.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 20;")
result_begin_semester = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 41;")
result_september = cur.fetchone()
label_begin_semester = tk.Label(frame_autumn, borderwidth=10, bg='#689CD2', text=f'{result_begin_semester[1]}: 4 {result_september[1]}', font=('Arial', 15))
label_begin_semester.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 21;")
result_end_semester = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 42;")
result_december = cur.fetchone()
label_end_semester = tk.Label(frame_autumn, borderwidth=10, bg='#689CD2', text=f'{result_end_semester[1]}: 17 {result_december[1]}', font=('Arial', 15))
label_end_semester.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 22;")
result_date_middle_grade = cur.fetchone()
label_date_middle_grade = tk.Label(frame_autumn, borderwidth=10, bg='#689CD2', text=f'{result_date_middle_grade[1]}: 17 {result_december[1]}', font=('Arial', 15))
label_date_middle_grade.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 23;")
result_all_weeks = cur.fetchone()
label_all_weeks = tk.Label(frame_autumn, borderwidth=10, bg='#689CD2', text=f'{result_all_weeks[1]}: 15', font=('Arial', 15))
label_all_weeks.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 24;")
result_midterms = cur.fetchone()
label_midterms = tk.Label(frame_autumn, borderwidth=10, bg='yellow', text=f'{result_midterms[1]} 🌞', font=('Arial', 15))
label_midterms.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 25;")
result_midterm = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 43;")
result_october = cur.fetchone()
label_midterm1 = tk.Label(frame_autumn, borderwidth=10, bg='#689CD2', text=f'{result_midterm[1]}: 16-21 {result_october[1]}', font=('Arial', 15))
label_midterm1.pack(side='top', anchor='w')

label_midterm2 = tk.Label(frame_autumn, borderwidth=10, bg='#689CD2', text=f'{result_midterm[1]}: 11-16 {result_december[1]}', font=('Arial', 15))
label_midterm2.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 26;")
result_final_control_winter = cur.fetchone()
label_final_control_winter = tk.Label(frame_autumn, borderwidth=10, bg='yellow', text=f'{result_final_control_winter[1]}: 18 {result_december[1]}-30 {result_december[1]} 🌞', font=('Arial', 15))
label_final_control_winter.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 27;")
result_holidays = cur.fetchone()
label_holidays = tk.Label(frame_autumn, borderwidth=10, bg='#689CD2', text=f'{result_holidays[1]}', font=('Arial', 15))

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 28;")
result_new_year = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 44;")
result_january = cur.fetchone()
label_new_year = tk.Label(frame_autumn, borderwidth=10, bg='#689CD2', text=f'{result_new_year[1]}: 1-2 {result_january[1]}', font=('Arial', 15))
label_new_year.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 29;")
result_republic = cur.fetchone()
label_republic = tk.Label(frame_autumn, borderwidth=10, bg='#689CD2', text=f'{result_republic[1]}: 25 {result_october[1]}', font=('Arial', 15))
label_republic.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 30;")
result_independence = cur.fetchone()
label_independence = tk.Label(frame_autumn, borderwidth=10, bg='#689CD2', text=f'{result_independence[1]}: 16 {result_december[1]}', font=('Arial', 15))
label_independence.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 31;")
result_days_off = cur.fetchone()
label_days_off = tk.Label(frame_autumn, borderwidth=10, bg='#689CD2', text=f'{result_days_off[1]}: 3 {result_january[1]}-13 {result_january[1]}', font=('Arial', 15))
label_days_off.pack(side='top', anchor='w')

#The second semester
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 45;")
result_april = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 46;")
result_february = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 47;")
result_march = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 48;")
result_may = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 49;")
result_june = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 50;")
result_july = cur.fetchone()

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 32;")
result_spring_semester = cur.fetchone()
label_spring_semester = tk.Label(frame_spring, borderwidth=10, bg='yellow', text=f'{result_spring_semester[1]} 🌞', font=('Arial', 15))
label_spring_semester.pack(side='top', anchor='w')

label_begin_semester2 = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_begin_semester[1]}: 15 {result_january[1]}', font=('Arial', 15))
label_begin_semester2.pack(side='top', anchor='w')

label_end_semester2 = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_end_semester[1]}: 28 {result_april[1]}', font=('Arial', 15))
label_end_semester2.pack(side='top', anchor='w')

label_date_middle_grade2 = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_date_middle_grade[1]}: 28 {result_april[1]}', font=('Arial', 15))
label_date_middle_grade2.pack(side='top', anchor='w')

label_all_weeks2 = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_all_weeks[1]}: 15', font=('Arial', 15))
label_all_weeks2.pack(side='top', anchor='w')

label_midterms2 = tk.Label(frame_spring, borderwidth=10, bg='yellow', text=f'{result_midterms[1]} 🌞', font=('Arial', 15))
label_midterms2.pack(side='top', anchor='w')

label_midterm12 = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_midterm[1]}: 26 {result_february[1]}-2 {result_march[1]}', font=('Arial', 15))
label_midterm12.pack(side='top', anchor='w')

label_midterm22 = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_midterm[1]}: 22-27 {result_april[1]}', font=('Arial', 15))
label_midterm22.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 33;")
result_final_control_summer = cur.fetchone()
label_final_control_summer = tk.Label(frame_spring, borderwidth=10, bg='yellow', text=f'{result_final_control_summer[1]}: 29 {result_april[1]}-18 {result_may[1]} 🌞', font=('Arial', 15))
label_final_control_summer.pack(side='top', anchor='w')

label_holidays2 = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_holidays[1]}', font=('Arial', 15))

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 34;")
result_Christ = cur.fetchone()
label_Christ = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_Christ[1]}: 7 {result_january[1]}', font=('Arial', 15))
label_Christ.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 35;")
result_women = cur.fetchone()
label_women = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_women[1]}: 8 {result_march[1]}', font=('Arial', 15))
label_women.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 36;")
result_nauryz = cur.fetchone()
label_nauryz = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_nauryz[1]}: 21-23 {result_march[1]}', font=('Arial', 15))
label_nauryz.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 37;")
result_unity = cur.fetchone()
label_unity = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_unity[1]}: 1 {result_may[1]}', font=('Arial', 15))
label_unity.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 38;")
result_defender = cur.fetchone()
label_defender = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_defender[1]}: 7 {result_may[1]}', font=('Arial', 15))
label_defender.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 39;")
result_victory = cur.fetchone()
label_victory = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_victory[1]}: 9 {result_may[1]}', font=('Arial', 15))
label_victory.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 40;")
result_capital_day = cur.fetchone()
label_capital_day = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_capital_day[1]}: 6 {result_july[1]}', font=('Arial', 15))
label_capital_day.pack(side='top', anchor='w')

label_days_off2 = tk.Label(frame_spring, borderwidth=10, bg='#689CD2', text=f'{result_days_off[1]}: 17 {result_june[1]}-31 {result_july[1]}', font=('Arial', 15))
label_days_off2.pack(side='top', anchor='w')


window.mainloop()