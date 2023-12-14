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

def back_to_menu():
    window.destroy()
    subprocess.run(['python', 'menu.py'])

window = tk.Tk()
window.attributes('-fullscreen', True)
window.geometry('1600x750')

frame_avatar = LabelFrame(window, width=350, height=325, bg='#689CD2', border=0)
frame_avatar.place(x=50, y=80)

frame_main_info = LabelFrame(window, width=700, height=350, bg='#689CD2', border=0)
frame_main_info.place(x=430, y=80)

frame_tips = LabelFrame(window, width=900, height=900, border=0)
frame_tips.pack(side='top', anchor='e', pady=50, padx=50)

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

image_bg = Image.open(f"C:/Users/Yerlan/OneDrive/Рабочий стол/Education/2_cource/Python+SQL/pictures/{result_user_id[2]}.png")
photo_bg = ImageTk.PhotoImage(image_bg)
label_bg = Label(frame_avatar, image=photo_bg)
label_bg.place(x=0, y=0)

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 10;")
result_name = cur.fetchone()
label_name = tk.Label(frame_main_info, borderwidth=10, bg='#689CD2', text=f'{result_name[1]}: {result_user_id[1]}', font=('Arial', 15))
label_name.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 11;")
result_gender = cur.fetchone()
label_gender = tk.Label(frame_main_info, borderwidth=10, bg='#689CD2', text=f'{result_gender[1]}: {result_user_id[2]}', font=('Arial', 15))
label_gender.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 12;")
result_gpa = cur.fetchone()
label_gpa = tk.Label(frame_main_info, borderwidth=10, bg='#689CD2', text=f'{result_gpa[1]}: {result_user_id[6]}', font=('Arial', 15))
label_gpa.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 13;")
result_birthday = cur.fetchone()
label_birthday = tk.Label(frame_main_info, borderwidth=10, bg='#689CD2', text=f'{result_birthday[1]}: {result_user_id[3]}', font=('Arial', 15))
label_birthday.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 14;")
result_specialization = cur.fetchone()
label_specialization = tk.Label(frame_main_info, borderwidth=10, bg='#689CD2', text=f'{result_specialization[1]}: {result_user_id[5]}', font=('Arial', 15))
label_specialization.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 15;")
result_department = cur.fetchone()
label_department = tk.Label(frame_main_info, borderwidth=10, bg='#689CD2', text=f'{result_department[1]}: {result_user_id[4]}', font=('Arial', 15))
label_department.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 16;")
result_height = cur.fetchone()
label_height = tk.Label(frame_main_info, borderwidth=10, bg='#689CD2', text=f'{result_height[1]}: {result_user_id[7]}', font=('Arial', 15))
label_height.pack(side='top', anchor='w')

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 17;")
result_weight = cur.fetchone()
label_weight = tk.Label(frame_main_info, borderwidth=10, bg='#689CD2', text=f'{result_weight[1]}: {result_user_id[8]}', font=('Arial', 15))
label_weight.pack(side='top', anchor='w')

if result_user_id[2] == 'Male':
    if selected_option == 'kaz':
        word_gender = ['Оның', 'Ол', 'оның', 'ол']
    if selected_option == 'rus':
        word_gender = ['Его', 'Он', 'его', 'он']
    if selected_option == 'eng':
        word_gender = ['His', 'He', 'his', 'he']
else:
    if selected_option == 'kaz':
        word_gender = ['Оның', 'Ол', 'оның', 'ол']
    if selected_option == 'rus':
        word_gender = ['Её', 'Она', 'её', 'она']
    if selected_option == 'eng':
        word_gender = ['Her', 'She', 'her', 'she']

if selected_option == 'kaz':
    label_description = tk.Label(window, text=f'Жеке студентты сипаттау, студенттің аты {result_user_id[1]}: '
                                              f'{word_gender[0]} жынысы {result_user_id[2]} болып келеді, {word_gender[2]} орташа бағасы {result_user_id[6]}'
                                              f' {word_gender[2]} туған күні {result_user_id[3]}, \n{word_gender[3]} {result_user_id[5]} оқиды'
                                              f' {result_user_id[4]} кафедрасында, Еуразиялық Ұлттық Университетінде оқиды,'
                                              f' \n{word_gender[2]} бойы {result_user_id[7]}, және де {word_gender[2]} салмағы {result_user_id[8]}'
                                              f' енді басты ақпарат оның Хоббиі және де ең сүйікті заты. \n{word_gender[0]} хоббиі'
                                              f' {result_user_id[9]} болып табылады және оның ең сүйікті заты ол {result_user_id[10]}.'
                                              f' Біздің ойымызша {word_gender[3]} керемет тұлға атанады',
                                 font=('Arial', 16))
if selected_option == 'rus':
    label_description = tk.Label(window, text=f'Индивидуальная описание про студента по имени {result_user_id[1]}: '
                                              f'{word_gender[0]} пол является {result_user_id[2]}, {word_gender[2]} средняя оценка {result_user_id[6]}'
                                              f' {word_gender[2]} день рождение {result_user_id[3]} числа, \n{word_gender[3]} учится в {result_user_id[5]}'
                                              f' в кафедре {result_user_id[4]}, в Евразийском Национальном Университете,'
                                              f' \n{word_gender[2]} рост {result_user_id[7]}, также {word_gender[2]} вес составляет {result_user_id[8]}'
                                              f' и теперь самое важное это Хобби и Любимая вещь на свете. \n{word_gender[0]} хобби'
                                              f' это {result_user_id[9]}. Также его любимая вещь является {result_user_id[10]}.'
                                              f' Мы думаем что {word_gender[3]} будет великолепной личностью',
                                 font=('Arial', 16))
if selected_option == 'eng':
    label_description = tk.Label(window, text=f'Individual Description about student {result_user_id[1]}: '
                                              f'{word_gender[0]} gender is {result_user_id[2]}, {word_gender[2]} gpa is {result_user_id[6]}'
                                              f' {word_gender[2]} birthday is {result_user_id[3]}, \n{word_gender[3]} is study in {result_user_id[5]}'
                                              f' in department {result_user_id[4]}, in the Eurasian National University,'
                                              f' \n{word_gender[2]} height is {result_user_id[7]}, also {word_gender[2]} weight is {result_user_id[8]}'
                                              f' and the most important is Hobby and Favourite thing. \n{word_gender[0]} hobby'
                                              f' is {result_user_id[9]}. And the favourite thing is {result_user_id[10]}.'
                                              f' We think that {word_gender[3]} would be greate personality',
                                 font=('Arial', 16))






label_description.place(x=50, y=500)

cur.execute(f"SELECT * FROM {selected_option} WHERE lan_id = 18;")
result_tips = cur.fetchone()
label_tips = tk.Label(frame_tips, text=f'{result_tips[1]}', font=('Arial', 15))
label_tips.pack(side='top', pady=10)

if result_user_id[0] == 404 or 111 or 222 or 333 or 444 or 555 or 777 or 888 or 999 or 666:
    result_user_id_tip = ''
    if result_user_id[0] == 404:
        if selected_option == 'kaz':
            result_user_id_tip = 'О, сіздің жүзіңіз осындай екен ғой \nМиссис Қате 😏'
        if selected_option == 'rus':
            result_user_id_tip = 'О, так вот как вы выглядите \nМиссис Ошибка 😏'
        if selected_option == 'rus':
            result_user_id_tip = 'Oh, that is how do you look \nMrs Error 😏'
    elif result_user_id[0] == 111:
        if selected_option == 'kaz':
            result_user_id_tip = 'Сіздің ID бұндай болғаны тағдыр шығар, \nяғни бірінші бірінші бірінші 🤔'
        if selected_option == 'rus':
            result_user_id_tip = 'Ваш ID должно быть ваша судьба, \nя имею ввиду первый первый первый 🤔'
        if selected_option == 'eng':
            result_user_id_tip = 'Your ID should be real your fate, \ni mean first first first 🤔'
    elif result_user_id[0] == 222:
        if selected_option == 'kaz':
            result_user_id_tip = ('"Кімде кімнің өмірлік нөмірі 2 болса, олардың тағдыры ерекшеленеді.\n '
                                  'Оларда ерекше рухани жаңғыру болады 🙂" ')
        if selected_option == 'rus':
            result_user_id_tip = ('"Те у кого жизненный номер имеет цифру 2, их ждет особая судьба.\n '
                                  'У них особое духовное развитие 🙂" ')
        if selected_option == 'eng':
            result_user_id_tip = ('"For those whose life number is 2, fate has a special meaning.\n '
                                  'They are predisposed to spiritual development 🙂" ')
    elif result_user_id[0] == 333:
        if selected_option == 'kaz':
            result_user_id_tip = 'Құдай үштікті жақсы көреді ❤'
        if selected_option == 'rus':
            result_user_id_tip = 'Бог любит троицу ❤'
        if selected_option == 'eng':
            result_user_id_tip = 'God loves trinity ❤'
    elif result_user_id[0] == 444:
        if selected_option == 'kaz':
            result_user_id_tip = 'Азияда бұл өлімнің саны, \nой кешір 👀'
        if selected_option == 'rus':
            result_user_id_tip = 'В Азии это цифра смерти, \nупс понять и простить 👀'
        if selected_option == 'eng':
            result_user_id_tip = 'In Asia it means death, \nugh sorry 👀'
    elif result_user_id[0] == 555:
        if selected_option == 'kaz':
            result_user_id_tip = 'Үздік студент 😎'
        if selected_option == 'rus':
            result_user_id_tip = 'Отличный студент 😎'
        if selected_option == 'eng':
            result_user_id_tip = 'Excellent student 😎'
    elif result_user_id[0] == 777:
        if selected_option == 'kaz':
            result_user_id_tip = 'Нағыз Қазақ 😎'
        if selected_option == 'rus':
            result_user_id_tip = 'Настоящий Казах 😎'
        if selected_option == 'eng':
            result_user_id_tip = 'The True Kazakh 😎'
    elif result_user_id[0] == 888:
        if selected_option == 'kaz':
            result_user_id_tip = 'Сізде өте керемет id, \nсата аласызба😏?'
        if selected_option == 'rus':
            result_user_id_tip = 'У вас отличный id, \nможете продать его😏?'
        if selected_option == 'eng':
            result_user_id_tip = 'You have a very cool id, \ncan you sell it😏?'
    elif result_user_id[0] == 666:
        if selected_option == 'kaz':
            result_user_id_tip = 'Шайтан😈? Сіз \nЕНУ да оқығыңыз келе ме😳??!!'
        if selected_option == 'rus':
            result_user_id_tip = 'Дьявол😈? Вы хотите \nучится в ЕНУ😳??!!'
        if selected_option == 'eng':
            result_user_id_tip = 'Diablo😈? Are you gonna \nstudy in ENU😳??!!'
    else:
        if selected_option == 'kaz':
            result_user_id_tip = f'Сіздің ID {result_user_id[0]}, \nбұл өте қызықты...😴'
        if selected_option == 'rus':
            result_user_id_tip = f'Ваш ID {result_user_id[0]}, \nэто очень интересно...😴'
        if selected_option == 'eng':
            result_user_id_tip = f'Your ID is {result_user_id[0]}, \nthat is interesting...😴'
    label_name_tips = tk.Label(frame_tips, text=f'{result_user_id_tip}', font=('Arial', 15))
    label_name_tips.pack(side='top', anchor='w', pady=10)

if result_user_id[1] == "Erlan":
    result_name_erlan = ''
    if selected_option == 'kaz':
        result_name_erlan = 'Ерлан сен данышпансын \nლ(╹◡╹ლ)'
    if selected_option == 'rus':
        result_name_erlan = 'Ерлан ты гений \nლ(╹◡╹ლ)'
    if selected_option == 'eng':
        result_name_erlan = 'Erlan you are genius \nლ(╹◡╹ლ)'
    label_name_erlan = tk.Label(frame_tips, text=f'{result_name_erlan}', font=('Arial', 15))
    label_name_erlan.pack(side='top', anchor='w', pady=10)

if result_user_id[4] == 'Pedagogical-sciences':
    result_department_pedagogical_sciences = ''
    if selected_option == 'kaz':
        result_department_pedagogical_sciences = 'Мұғалімдер өте керемет адамдар'
    elif selected_option == 'rus':
        result_department_pedagogical_sciences = 'Учителя крутые люди'
    elif selected_option == 'eng':
        result_department_pedagogical_sciences = 'Teachers are very cool guys'
    label_department_tips = tk.Label(frame_tips, text=f'{result_department_pedagogical_sciences}', font=('Arial', 15))
    label_department_tips.pack(side='top', anchor='w', pady=10)
elif result_user_id[4] == 'Arts-and-Humanitarian-sciences':
    result_department_arts_and_humanitarian_sciences = 'Have you heard about \nart or humanitarian sciences?'
    if selected_option == 'kaz':
        result_department_arts_and_humanitarian_sciences = 'Гуманитарий және арт \nғылымы туралы естідіңізбе?'
    elif selected_option == 'rus':
        result_department_arts_and_humanitarian_sciences = 'Вы слышали про арт \nи Гуманитарные науки?'
    elif selected_option == 'eng':
        result_department_arts_and_humanitarian_sciences = 'Have you heard about \nart or humanitarian sciences?'
    label_department_tips = tk.Label(frame_tips, text=f'{result_department_arts_and_humanitarian_sciences}', font=('Arial', 15))
    label_department_tips.pack(side='top', anchor='w')
elif result_user_id[4] == 'Social-sciences,journalism-and-information':
    result_department_social_sciences_journalism_and_information = 'Journalist? \nTake the camera'
    if selected_option == 'kaz':
        result_department_social_sciences_journalism_and_information = 'Журналист? \nКамераны қолға алыңыз'
    elif selected_option == 'rus':
        result_department_social_sciences_journalism_and_information = 'Журналист? \nБерите камеру в руки'
    elif selected_option == 'eng':
        result_department_social_sciences_journalism_and_information = 'Journalist? \nTake the camera'
    label_department_tips = tk.Label(frame_tips, text=f'{result_department_social_sciences_journalism_and_information}',
                                     font=('Arial', 15))
    label_department_tips.pack(side='top', anchor='w', pady=10)
elif result_user_id[4] == 'Business,Management-and-law':
    result_department_business_management_and_law = 'Businessman? \nLike a busy guy?'
    if selected_option == 'kaz':
        result_department_business_management_and_law = 'Бизнесмен? \nКлассика киіміндегі адам ба?'
    elif selected_option == 'rus':
        result_department_business_management_and_law = 'Бизнесмен? \nВечно занятой?'
    elif selected_option == 'eng':
        result_department_business_management_and_law = 'Businessman? \nLike a busy guy?'
    label_department_tips = tk.Label(frame_tips, text=f'{result_department_business_management_and_law}',
                                     font=('Arial', 15))
    label_department_tips.pack(side='top', anchor='w', pady=10)
elif result_user_id[4] == 'Natural-sciences,mathematics-and-statistics':
    result_department_natural_sciences_mathematics_and_statistics = 'We are not Engineers, \nwe are mathematians'
    if selected_option == 'kaz':
        result_department_natural_sciences_mathematics_and_statistics = 'Біз инженер емеспіз, \nБіз математикпіз'
    elif selected_option == 'rus':
        result_department_natural_sciences_mathematics_and_statistics = 'Мы не инженеры, \nМы математики'
    elif selected_option == 'eng':
        result_department_natural_sciences_mathematics_and_statistics = 'We are not Engineers, \nwe are mathematians'
    label_department_tips = tk.Label(frame_tips, text=f'{result_department_natural_sciences_mathematics_and_statistics}',
                                     font=('Arial', 15))
    label_department_tips.pack(side='top', anchor='w', pady=10)
elif result_user_id[4] == 'Information-and-communication-technology':
    result_department_information_and_communication_technology = 'Programmer? \nCan you fix the printer?'
    if selected_option == 'kaz':
        result_department_information_and_communication_technology = 'Программист? \nПринтер жөндеп бере аласыз ба?'
    elif selected_option == 'rus':
        result_department_information_and_communication_technology = 'Программист? \nМожете починить принтер?'
    elif selected_option == 'eng':
        result_department_information_and_communication_technology = 'Programmer? \nCan you fix the printer?'
    label_department_tips = tk.Label(frame_tips, text=f'{result_department_information_and_communication_technology}',
                                     font=('Arial', 15))
    label_department_tips.pack(side='top', anchor='w', pady=10)
elif result_user_id[4] == 'Engineering,manufacturing-and-building-industries':
    result_department_engineer_manufacturing_and_building_industries = 'Are builder or \nlike a Engineer?'
    if selected_option == 'kaz':
        result_department_engineer_manufacturing_and_building_industries = 'Құрылысшы \nӘлде Инженер?'
    elif selected_option == 'rus':
        result_department_engineer_manufacturing_and_building_industries = 'Строитель \nИли Инженер?'
    elif selected_option == 'eng':
        result_department_engineer_manufacturing_and_building_industries = 'Are builder or \nlike a Engineer?'
    label_department_tips = tk.Label(frame_tips, text=f'{result_department_engineer_manufacturing_and_building_industries}',
                                     font=('Arial', 15))
    label_department_tips.pack(side='top', anchor='w', pady=10)
elif result_user_id[4] == 'Services':
    result_department_services = 'Guys are learn the world history and \nEnglish language to study in Services?'
    if selected_option == 'kaz':
        result_department_services = 'Демек сервисте оқу үшін \nАғылшын және тарих пәндерін оқисындар ма?'
    elif selected_option == 'rus':
        result_department_services = 'Ребята вы учите историю и англисский\nДля того чтобы учится в сервисах?'
    elif selected_option == 'eng':
        result_department_services = 'Are you guys learn the history and \nEnglish language to study in Services?'
    label_department_tips = tk.Label(frame_tips, text=f'{result_department_services}',
                                     font=('Arial', 15))
    label_department_tips.pack(side='top', anchor='w', pady=10)


if 1.0 <= float(result_user_id[6]) <= 2.5:
    result_gpa_lower = 'Bro you need to study, \nmore passion more energy o(〃＾▽＾〃)o'
    if selected_option == 'kaz':
        result_gpa_lower = 'Сізге оқу қажет, \nКөп құштар көп энергия o(〃＾▽＾〃)o'
    elif selected_option == 'rus':
        result_gpa_lower = 'Вам нужно учится, \nБольше страсти больше энергии o(〃＾▽＾〃)o'
    elif selected_option == 'eng':
        result_gpa_lower = 'Bro you need to study, \nMore passion more energy o(〃＾▽＾〃)o'
    label_gpa_tips = tk.Label(frame_tips, text=f'{result_gpa_lower}', font=('Arial', 15))
    label_gpa_tips.pack(side='top', anchor='w', pady=10)
elif 3.0 >= float(result_user_id[6]) >= 2.5:
    result_gpa_higher = 'Сізде өте жақсы көрсеткіш, \nСіз білімді студентсіз 🐱‍👤'
    if selected_option == 'kaz':
        result_gpa_higher = 'Сізде өте жақсы көрсеткіш, \nСіз білімді студентсіз 🐱‍👤'
    elif selected_option == 'rus':
        result_gpa_higher = 'У вас хороший показатель, \nВы образованный 🐱‍👤'
    elif selected_option == 'eng':
        result_gpa_higher = 'Bro you have a good gpa, \nyou are smart 🐱‍👤'
    label_gpa_tips = tk.Label(frame_tips, text=f'{result_gpa_higher}', font=('Arial', 15))
    label_gpa_tips.pack(side='top', anchor='w', pady=10)
elif 3.0 < float(result_user_id[6]) < 4.0:
    result_gpa_higher2 = 'Керемет көрсеткіш?! \nҮлгі болатын жағдай 🤓'
    if selected_option == 'kaz':
        result_gpa_higher2 = 'Керемет көрсеткіш! \nҮлгі болатын жағдай 🤓'
    elif selected_option == 'rus':
        result_gpa_higher2 = 'Прекрасный показатель! \nЭтим нужно гордиться 🤓'
    elif selected_option == 'eng':
        result_gpa_higher2 = 'Excellent work! \nYou are the best, good job 🤓'
    label_gpa_tips = tk.Label(frame_tips, text=f'{result_gpa_higher2}', font=('Arial', 15))
    label_gpa_tips.pack(side='top', anchor='w', pady=10)
elif float(result_user_id[6]) == 4.0:
    result_gpa_highest = 'Сіздің gpa 4.0?! \nСіз құбыжықсыз, керемет жұмыс 🤓'
    if selected_option == 'kaz':
        result_gpa_highest = 'Сіздің gpa 4.0?! \nСіз құбыжықсыз, керемет жұмыс 🤓'
    elif selected_option == 'rus':
        result_gpa_highest = 'Ваш gpa 4.0?! \nВы монстр, хорошая работа 🤓'
    elif selected_option == 'eng':
        result_gpa_highest = 'Your gpa is 4.0?! \nYou are monster, good job 🤓'
    label_gpa_tips = tk.Label(frame_tips, text=f'{result_gpa_highest}', font=('Arial', 15))
    label_gpa_tips.pack(side='top', anchor='w', pady=10)
else:
    print('Error')
if float(result_user_id[7]) >= 1.90:
    result_height_high = 'Are you play basketball(. ❛ ᴗ ❛.)?'
    if selected_option == 'kaz':
        result_height_high = 'Сіз баскетбол ойнайсыз ба(. ❛ ᴗ ❛.)?'
    elif selected_option == 'rus':
        result_height_high = 'Вы играете в баскетбол(. ❛ ᴗ ❛.)?'
    elif selected_option == 'eng':
        result_height_high = 'Are you play basketball(. ❛ ᴗ ❛.)?'
    label_height_tips = tk.Label(frame_tips, text=f'{result_height_high}', font=('Arial', 15))
    label_height_tips.pack(side='top', anchor='w', pady=10)
else:
    result_height_tip = 'Have you heard about \nexam without pain?'
    if selected_option == 'kaz':
        result_height_tip = 'Оңай емтихан туралы \nаңызды естіп пе едіңіз?'
    elif selected_option == 'rus':
        result_height_tip = 'Вы слышали легенду про \n легкий экзамен?'
    elif selected_option == 'eng':
        result_height_tip = 'Have you heard about \nexam without pain?'
    label_height_tips = tk.Label(frame_tips, text=f'{result_height_tip}', font=('Arial', 15))
    label_height_tips.pack(side='top', anchor='w', pady=10)

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

window.mainloop()