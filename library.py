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



def display_search_result(result_search):
    tree = ttk.Treeview(frame_search_result)
    tree["columns"] = ("Book ID", "Book Name", "Author Name", "Publisher Name", "Publication Year")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Book ID", anchor=tk.W, width=120)
    tree.column("Book Name", anchor=tk.W, width=120)
    tree.column("Author Name", anchor=tk.W, width=120)
    tree.column("Publisher Name", anchor=tk.W, width=120)
    tree.column("Publication Year", anchor=tk.W, width=120)

    tree.heading("#0", text="")
    tree.heading("Book ID", text="Book ID")
    tree.heading("Book Name", text="Book Name")
    tree.heading("Author Name", text="Author Name")
    tree.heading("Publisher Name", text="Publisher Name")
    tree.heading("Publication Year", text="Publication Year")

    for index, row in enumerate(result_search):
        tree.insert("", index, values=row)

    tree.pack(expand=True, fill=tk.BOTH)

def search():
    entry_id_g = entry_id.get()
    entry_name_g = entry_name.get()
    entry_author_name_g = entry_author_name.get()
    entry_publisher_name_g = entry_publisher_name.get()
    entry_publication_year_g = entry_publication_year.get()

    if entry_id_g == f'{result_entry_id[1]}':
        entry_id.delete(0, 'end')
    if entry_name_g == f'{result_entry_name[1]}':
        entry_name.delete(0, 'end')
    if entry_author_name_g == f'{result_entry_author_name[1]}':
        entry_author_name.delete(0, 'end')
    if entry_publisher_name_g == f'{result_entry_publisher_name[1]}':
        entry_publisher_name.delete(0, 'end')
    if entry_publication_year_g == f'{result_entry_publication_year[1]}':
        entry_publication_year.delete(0, 'end')

    entry_id_value = entry_id.get()
    entry_name_value = entry_name.get()
    entry_author_name_value = entry_author_name.get()
    entry_publisher_name_value = entry_publisher_name.get()
    entry_publication_year_value = entry_publication_year.get()

    query = "SELECT * FROM library_book_list WHERE "

    conditions = []
    if entry_id_value:
        conditions.append(f"CAST(book_id AS TEXT) LIKE '%{entry_id_value}%'")
    if entry_name_value:
        conditions.append(f"lower(book_name) LIKE '%{entry_name_value}%'")
    if entry_author_name_value:
        conditions.append(f"lower(author_name) LIKE '%{entry_author_name_value}%'")
    if entry_publisher_name_value:
        conditions.append(f"lower(publisher_name) LIKE '%{entry_publisher_name_value}%'")
    if entry_publication_year_value:
        conditions.append(f"CAST(publication_year AS TEXT) LIKE '%{entry_publication_year_value}%'")

    query += " AND ".join(conditions)
    cur.execute(query)
    print(query)
    result_search = cur.fetchall()
    print(result_search)
    display_search_result(result_search)

def back_to_menu():
    window.destroy()
    # subprocess.run(['python', 'menu.py'])

def on_enter_entry(event):
    entry_id.delete(0, 'end')


def on_leave_entry_id(event):
    name = entry_id.get()
    if name == '':
        entry_id.insert(0, f'{result_entry_id[1]}')

def on_enter_entry_name(event):
    entry_name.delete(0, 'end')


def on_leave_entry_name(event):
    name = entry_name.get()
    if name == '':
        entry_name.insert(0, f'{result_entry_name[1]}')

def on_enter_entry_author_name(event):
    entry_author_name.delete(0, 'end')


def on_leave_entry_author_name(event):
    name = entry_author_name.get()
    if name == '':
        entry_author_name.insert(0, f'{result_entry_author_name[1]}')

def on_enter_entry_publisher_name(event):
    entry_publisher_name.delete(0, 'end')


def on_leave_entry_publisher_name(event):
    name = entry_publisher_name.get()
    if name == '':
        entry_publisher_name.insert(0, f'{result_entry_publisher_name[1]}')

def on_enter_entry_publication_year(event):
    entry_publication_year.delete(0, 'end')


def on_leave_entry_publication_year(event):
    name = entry_publication_year.get()
    if name == '':
        entry_publication_year.insert(0, f'{result_entry_publication_year[1]}')


window = tk.Tk()
window.geometry("1920x1080")
window.attributes('-fullscreen', True)
window.configure(bg='#689CD2')

frame_search = LabelFrame(window, bg='grey', width=800, height=400, border=0)
frame_search.place(x=50, y=100)

frame_search_result = LabelFrame(window, bg='#689CD2', width=400, height=400, border=0)
frame_search_result.place(x=500, y=100)

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

entry_id = ttk.Entry(frame_search,  font=('Arial', 15), width=30)
entry_name = ttk.Entry(frame_search, font=('Arial', 15), width=30)
entry_author_name = ttk.Entry(frame_search, font=('Arial', 15), width=30)
entry_publisher_name = ttk.Entry(frame_search, font=('Arial', 15), width=30)
entry_publication_year = ttk.Entry(frame_search, font=('Arial', 15), width=30)


entry_id.pack(side='top', anchor='w', pady=10, padx=10)
entry_name.pack(side='top', anchor='w', pady=10, padx=10)
entry_author_name.pack(side='top', anchor='w', pady=10, padx=10)
entry_publisher_name.pack(side='top', anchor='w', pady=10, padx=10)
entry_publication_year.pack(side='top', anchor='w', pady=10, padx=10)

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 60;")
result_entry_id = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 61;")
result_entry_name = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 62;")
result_entry_author_name = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 63;")
result_entry_publisher_name = cur.fetchone()
cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 64;")
result_entry_publication_year = cur.fetchone()


entry_id.insert(0, f'{result_entry_id[1]}')
entry_name.insert(0, f'{result_entry_name[1]}')
entry_author_name.insert(0, f'{result_entry_author_name[1]}')
entry_publisher_name.insert(0, f'{result_entry_publisher_name[1]}')
entry_publication_year.insert(0, f'{result_entry_publication_year[1]}')


entry_id.bind('<FocusIn>', on_enter_entry)
entry_id.bind('<FocusOut>', on_leave_entry_id)
entry_name.bind('<FocusIn>', on_enter_entry_name)
entry_name.bind('<FocusOut>', on_leave_entry_name)
entry_author_name.bind('<FocusIn>', on_enter_entry_author_name)
entry_author_name.bind('<FocusOut>', on_leave_entry_author_name)
entry_publisher_name.bind('<FocusIn>', on_enter_entry_publisher_name)
entry_publisher_name.bind('<FocusOut>', on_leave_entry_publisher_name)
entry_publication_year.bind('<FocusIn>', on_enter_entry_publication_year)
entry_publication_year.bind('<FocusOut>', on_leave_entry_publication_year)


cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 9;")
result_back = cur.fetchone()
button_back = tk.Button(window, text=f'{result_back[1]}', bg='#690AB9', font=('Arial', 15), border=0.1, command=back_to_menu)
button_back.place(x=50, y=40)
button_search = tk.Button(window, text='Search', bg='#690AB9', font=('Arial', 15), border=0.1, command=search)
button_search.place(x=600, y=600)

window.mainloop()
