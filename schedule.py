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

window = tk.Tk()
window.attributes('-fullscreen', True)
window.geometry('1600x750')
window.configure(bg='#689CD2')

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

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 9;")
result_back = cur.fetchone()
button_back = tk.Button(window, text=f'{result_back[1]}', bg='#690AB9', font=('Arial', 15), border=0.1, command=back_to_menu)
button_back.place(x=50, y=40)

frame_days = LabelFrame(window, width=750, height=700, bg='white', border=0)
frame_days.place(x=50, y=100)

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 54;")
result_monday = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 55;")
result_tuesday = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 56;")
result_wednesday = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 57;")
result_thursday = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 58;")
result_friday = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 59;")
result_saturday = cur.fetchone()

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

if result_user_id[4] == 'Pedagogical-sciences':
    label_monday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_monday[1]}(ಥ _ ಥ)\n{result_turkology[9]}\n{result_pedagogy_and_psychology[9]}\n{result_turkology[9]}\n{result_pedagogy_and_psychology[9]}',
                            font=('Arial', 15))

    label_tuesday = tk.Label(frame_days, borderwidth=10, bg='white',
                             text=f'{result_tuesday[1]}(〃＞目＜)\n{result_russian[9]}\n{result_english[9]}\n{result_english[9]}\n{result_turkology[9]}',
                             font=('Arial', 15))

    label_wednesday = tk.Label(frame_days, borderwidth=10, bg='white',
                               text=f'{result_wednesday[1]}ᕦ(ò_óˇ)ᕤ\n{result_russian[9]}\n{result_english[9]}',
                               font=('Arial', 15))

    label_thursday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_thursday[1]}＼（〇_ｏ）／\n{result_turkology[9]}\n{result_pedagogy_and_psychology[9]}',
                              font=('Arial', 15))

    label_friday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_friday[1]}(lll￢ω￢)\n{result_english[9]}\n{result_turkology[9]}',
                            font=('Arial', 15))

    label_saturday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_saturday[1]}♨_♨\n{result_pedagogy_and_psychology[9]}\n{result_turkology[9]}\n{result_turkology[9]}\n{result_pedagogy_and_psychology[9]}',
                              font=('Arial', 15))
    label_monday.grid(row=0, column=1, pady=20, padx=20)
    label_tuesday.grid(row=0, column=2, pady=20, padx=20)
    label_wednesday.grid(row=0, column=3, pady=20, padx=20)
    label_thursday.grid(row=1, column=1, pady=20, padx=20)
    label_friday.grid(row=1, column=2, pady=20, padx=20)
    label_saturday.grid(row=1, column=3, pady=20, padx=20)

elif result_user_id[4] == 'Arts-and-Humanitarian-sciences':
    label_monday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_monday[1]}(ಥ _ ಥ)\n{result_journalism[9]}\n{result_russian[9]}\n{result_english[9]}\n{result_english[9]}',
                            font=('Arial', 15))

    label_tuesday = tk.Label(frame_days, borderwidth=10, bg='white',
                             text=f'{result_tuesday[1]}ಠಿ_ಠ\n{result_pedagogy_and_psychology[9]}',
                             font=('Arial', 15))

    label_wednesday = tk.Label(frame_days, borderwidth=10, bg='white',
                               text=f'{result_wednesday[1]}o((>ω< ))o\n{result_russian[9]}\n{result_english[9]}',
                               font=('Arial', 15))

    label_thursday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_thursday[1]}o(TヘTo)\n{result_energy_efficient_design_of_buildings[9]}\n{result_pedagogy_and_psychology[9]}',
                              font=('Arial', 15))

    label_friday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_friday[1]}（＞人＜；）\n{result_english[9]}\n{result_turkology[9]}',
                            font=('Arial', 15))

    label_saturday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_saturday[1]}⊙﹏⊙∥\n{result_journalism[9]}\n{result_russian[9]}\n{result_english[9]}\n{result_english[9]}',
                              font=('Arial', 15))
    label_monday.grid(row=0, column=1, pady=20, padx=20)
    label_tuesday.grid(row=0, column=2, pady=20, padx=20)
    label_wednesday.grid(row=0, column=3, pady=20, padx=20)
    label_thursday.grid(row=1, column=1, pady=20, padx=20)
    label_friday.grid(row=1, column=2, pady=20, padx=20)
    label_saturday.grid(row=1, column=3, pady=20, padx=20)

elif result_user_id[4] == 'Social-sciences,journalism-and-information':
    label_monday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_monday[1]}(ಥ _ ಥ)\n{result_journalism[9]}\n{result_russian[9]}\n{result_english[9]}\n{result_english[9]}',
                            font=('Arial', 15))

    label_tuesday = tk.Label(frame_days, borderwidth=10, bg='white',
                             text=f'{result_tuesday[1]}~~>_<~~\n{result_journalism[9]}\n{result_russian[9]}\n{result_english[9]}\n{result_english[9]}',
                             font=('Arial', 15))

    label_wednesday = tk.Label(frame_days, borderwidth=10, bg='white',
                               text=f'{result_wednesday[1]}(。﹏。*)\n{result_russian[9]}\n{result_english[9]}',
                               font=('Arial', 15))

    label_thursday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_thursday[1]}( ͠° ͟ʖ ͡°)\n{result_english[9]}\n{result_turkology[9]}',
                              font=('Arial', 15))

    label_friday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_friday[1]}( ◍•㉦•◍ )\n{result_english[9]}\n{result_turkology[9]}',
                            font=('Arial', 15))

    label_saturday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_saturday[1]}༼ つ ◕_◕ ༽つ\n{result_journalism[9]}\n{result_russian[9]}\n{result_english[9]}\n{result_english[9]}',
                              font=('Arial', 15))
    label_monday.grid(row=0, column=1, pady=20, padx=20)
    label_tuesday.grid(row=0, column=2, pady=20, padx=20)
    label_wednesday.grid(row=0, column=3, pady=20, padx=20)
    label_thursday.grid(row=1, column=1, pady=20, padx=20)
    label_friday.grid(row=1, column=2, pady=20, padx=20)
    label_saturday.grid(row=1, column=3, pady=20, padx=20)

elif result_user_id[4] == 'Business,Management-and-law':
    label_monday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_monday[1]}(ಥ _ ಥ)\n{result_economics_and_business[9]}\n{result_economics_and_business[9]}\n{result_economics_and_business[9]}',
                            font=('Arial', 15))

    label_tuesday = tk.Label(frame_days, borderwidth=10, bg='white',
                             text=f'{result_tuesday[1]}(￣(工)￣)\n{result_economics_and_business[9]}\n{result_russian[9]}\n{result_english[9]}\n{result_english[9]}',
                             font=('Arial', 15))

    label_wednesday = tk.Label(frame_days, borderwidth=10, bg='white',
                               text=f'{result_wednesday[1]}¯\_( ͡° ͜ʖ ͡°)_/¯\n{result_russian[9]}\n{result_english[9]}',
                               font=('Arial', 15))

    label_thursday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_thursday[1]}✍(◔◡◔)\n{result_english[9]}\n{result_economics_and_business[9]}',
                              font=('Arial', 15))

    label_friday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_friday[1]}(ﾉ*ФωФ)ﾉ\n{result_english[9]}\n{result_economics_and_business[9]}',
                            font=('Arial', 15))

    label_saturday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_saturday[1]}(❤ ω ❤)\n{result_journalism[9]}\n{result_economics_and_business[9]}\n{result_english[9]}\n{result_english[9]}',
                              font=('Arial', 15))
    label_monday.grid(row=0, column=1, pady=20, padx=20)
    label_tuesday.grid(row=0, column=2, pady=20, padx=20)
    label_wednesday.grid(row=0, column=3, pady=20, padx=20)
    label_thursday.grid(row=1, column=1, pady=20, padx=20)
    label_friday.grid(row=1, column=2, pady=20, padx=20)
    label_saturday.grid(row=1, column=3, pady=20, padx=20)

elif result_user_id[4] == 'Natural-sciences,mathematics-and-statistics':
    label_monday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_monday[1]}(ಥ _ ಥ)\n{result_math[9]}\n{result_math[9]}\n{result_math[9]}',
                            font=('Arial', 15))

    label_tuesday = tk.Label(frame_days, borderwidth=10, bg='white',
                             text=f'{result_tuesday[1]}U•ェ•*U\n{result_math[9]}\n{result_russian[9]}\n{result_english[9]}\n{result_english[9]}',
                             font=('Arial', 15))

    label_wednesday = tk.Label(frame_days, borderwidth=10, bg='white',
                               text=f'{result_wednesday[1]}(〜￣▽￣)〜〜(￣▽￣〜)\n{result_russian[9]}\n{result_english[9]}',
                               font=('Arial', 15))

    label_thursday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_thursday[1]}ヾ(⌐■_■)ノ♪\n{result_english[9]}\n{result_math[9]}',
                              font=('Arial', 15))

    label_friday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_friday[1]}(•_•)\n{result_english[9]}\n{result_math[9]}\n{result_math[9]}\n{result_math[9]}',
                            font=('Arial', 15))

    label_saturday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_saturday[1]}~\(≧▽≦)/~\n{result_journalism[9]}\n{result_economics_and_business[9]}\n{result_english[9]}\n{result_english[9]}',
                              font=('Arial', 15))
    label_monday.grid(row=0, column=1, pady=20, padx=20)
    label_tuesday.grid(row=0, column=2, pady=20, padx=20)
    label_wednesday.grid(row=0, column=3, pady=20, padx=20)
    label_thursday.grid(row=1, column=1, pady=20, padx=20)
    label_friday.grid(row=1, column=2, pady=20, padx=20)
    label_saturday.grid(row=1, column=3, pady=20, padx=20)

elif result_user_id[4] == 'Information-and-communication-technology':
    label_monday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_monday[1]}(ಥ _ ಥ)\n{result_ai_technologies[9]}\n{result_math[9]}\n{result_math[9]}',
                            font=('Arial', 15))

    label_tuesday = tk.Label(frame_days, borderwidth=10, bg='white',
                             text=f'{result_tuesday[1]}(∩^o^)⊃━☆\n{result_math[9]}\n{result_ai_technologies[9]}\n{result_english[9]}',
                             font=('Arial', 15))

    label_wednesday = tk.Label(frame_days, borderwidth=10, bg='white',
                               text=f'{result_wednesday[1]}(∪.∪ )...zzz\n{result_russian[9]}\n{result_ai_technologies[9]}',
                               font=('Arial', 15))

    label_thursday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_thursday[1]}(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧\n{result_english[9]}\n{result_math[9]}',
                              font=('Arial', 15))

    label_friday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_friday[1]}(^///^)\n{result_ai_technologies[9]}\n{result_math[9]}\n{result_math[9]}\n{result_math[9]}',
                            font=('Arial', 15))

    label_saturday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_saturday[1]}(´▽`ʃ♡ƪ)\n{result_journalism[9]}\n{result_ai_technologies[9]}\n{result_english[9]}\n{result_english[9]}',
                              font=('Arial', 15))
    label_monday.grid(row=0, column=1, pady=20, padx=20)
    label_tuesday.grid(row=0, column=2, pady=20, padx=20)
    label_wednesday.grid(row=0, column=3, pady=20, padx=20)
    label_thursday.grid(row=1, column=1, pady=20, padx=20)
    label_friday.grid(row=1, column=2, pady=20, padx=20)
    label_saturday.grid(row=1, column=3, pady=20, padx=20)

elif result_user_id[4] == 'Engineering,manufacturing-and-building-industries':
    label_monday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_monday[1]}(ಥ _ ಥ)\n{result_energy_efficient_design_of_buildings[9]}\n{result_math[9]}\n{result_math[9]}',
                            font=('Arial', 15))

    label_tuesday = tk.Label(frame_days, borderwidth=10, bg='white',
                             text=f'{result_tuesday[1]}(p≧w≦q)\n{result_math[9]}\n{result_ai_technologies[9]}\n{result_english[9]}',
                             font=('Arial', 15))

    label_wednesday = tk.Label(frame_days, borderwidth=10, bg='white',
                               text=f'{result_wednesday[1]}o((>ω< ))o\n{result_energy_efficient_design_of_buildings[9]}\n{result_ai_technologies[9]}',
                               font=('Arial', 15))

    label_thursday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_thursday[1]}(✿◡‿◡)\n{result_english[9]}\n{result_energy_efficient_design_of_buildings[9]}',
                              font=('Arial', 15))

    label_friday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_friday[1]}(•_•)\n{result_energy_efficient_design_of_buildings[9]}\n{result_math[9]}\n{result_math[9]}\n{result_math[9]}',
                            font=('Arial', 15))

    label_saturday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_saturday[1]}( •̀ .̫ •́ )✧\n{result_journalism[9]}\n{result_energy_efficient_design_of_buildings[9]}\n{result_english[9]}\n{result_english[9]}',
                              font=('Arial', 15))
    label_monday.grid(row=0, column=1, pady=20, padx=20)
    label_tuesday.grid(row=0, column=2, pady=20, padx=20)
    label_wednesday.grid(row=0, column=3, pady=20, padx=20)
    label_thursday.grid(row=1, column=1, pady=20, padx=20)
    label_friday.grid(row=1, column=2, pady=20, padx=20)
    label_saturday.grid(row=1, column=3, pady=20, padx=20)

elif result_user_id[4] == 'Services':
    label_monday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_monday[1]}(ಥ _ ಥ)\n{result_tourism[9]}\n{result_math[9]}\n{result_math[9]}',
                            font=('Arial', 15))

    label_tuesday = tk.Label(frame_days, borderwidth=10, bg='white',
                             text=f'{result_tuesday[1]}（。＾▽＾）\n{result_tourism[9]}\n{result_tourism[9]}\n{result_english[9]}',
                             font=('Arial', 15))

    label_wednesday = tk.Label(frame_days, borderwidth=10, bg='white',
                               text=f'{result_wednesday[1]}(￣o￣) . z Z\n{result_tourism[9]}\n{result_ai_technologies[9]}',
                               font=('Arial', 15))

    label_thursday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_thursday[1]}ヾ(•ω•`)o\n{result_english[9]}\n{result_tourism[9]}',
                              font=('Arial', 15))

    label_friday = tk.Label(frame_days, borderwidth=10, bg='white',
                            text=f'{result_friday[1]}(´。＿。｀)\n{result_tourism[9]}\n{result_math[9]}\n{result_math[9]}\n{result_math[9]}',
                            font=('Arial', 15))

    label_saturday = tk.Label(frame_days, borderwidth=10, bg='white',
                              text=f'{result_saturday[1]}(┬┬﹏┬┬)\n{result_tourism[9]}\n{result_tourism[9]}\n{result_english[9]}\n{result_english[9]}',
                              font=('Arial', 15))
    label_monday.grid(row=0, column=1, pady=20, padx=20)
    label_tuesday.grid(row=0, column=2, pady=20, padx=20)
    label_wednesday.grid(row=0, column=3, pady=20, padx=20)
    label_thursday.grid(row=1, column=1, pady=20, padx=20)
    label_friday.grid(row=1, column=2, pady=20, padx=20)
    label_saturday.grid(row=1, column=3, pady=20, padx=20)

window.mainloop()