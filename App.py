import telebot, os, time
from pathlib import Path
import School_Class as sc
import School_Report as Report
from telebot import types
from collections import Counter

path_to_file = 'teachers-report.txt'
path = Path(path_to_file)
bot = telebot.TeleBot("5814739213:AAGjeT3JjweoravR157OWEjPoDVI-lX3Iuw")
teachers = []

def var_zero(chat_id,user_message,user_id,user_id_number,first_class_name,second_class_name,class_from_sc_one,class_from_sc_two):
    src = user_message
    z = src.replace(" ","")
    if user_message  == first_class_name and user_id == user_id_number:
        for k,v in class_from_sc_one.items():
            bot.send_message(chat_id, text= f"{k} — {v}")
    elif user_message  == second_class_name and user_id == user_id_number:
        for k,v in class_from_sc_two.items():
            bot.send_message(chat_id, text= f"{k} — {v}")
    elif user_message != first_class_name and user_message != second_class_name and user_id == user_id_number:
        if src[:2].upper() == first_class_name or src[:3].upper() == first_class_name:
            for k,v in class_from_sc_one.items():
                try:
                    if isinstance(int(z[2:4]), int):
                        formated_answer = z[2:4]+" "+z[4::]
                        if formated_answer[:2].replace(" ","") == str(k) or src[3:6].replace(" ","") == str(k):
                            with open(f"teachers-report.txt", "a", encoding="utf-8") as file:
                                file.write(f"{v}{formated_answer[2::]}\n")
                except:
                    formated_answer = z[2]+" "+z[3::]
                    if formated_answer[:1].replace(" ","") == str(k) or src[3:6].replace(" ","") == str(k):
                        with open(f"teachers-report.txt", "a", encoding="utf-8") as file:
                            file.write(f"{v}{formated_answer[1::]}\n")
        elif src[:2].upper() == second_class_name or src[:3].upper() == second_class_name:
            for k,v in class_from_sc_two.items():
                try:
                    if isinstance(int(z[2:4]), int):
                        formated_answer = z[2:4]+" "+z[4::]
                        if formated_answer[:2].replace(" ","") == str(k) or src[3:6].replace(" ","") == str(k):
                            with open(f"teachers-report.txt", "a", encoding="utf-8") as file:
                                file.write(f"{v}{formated_answer[2::]}\n")
                except:
                    formated_answer = z[2]+" "+z[3::]
                    if formated_answer[:1].replace(" ","") == str(k) or src[3:6].replace(" ","") == str(k):
                        with open(f"teachers-report.txt", "a", encoding="utf-8") as file:
                            file.write(f"{v}{formated_answer[1::]}\n")
        else:
            bot.send_message(chat_id, text= f"Укажите свой класс перед порядковым номером\nНапример: {first_class_name} 23 грипп")

######### УЧИТЕЛЯ С 1 КЛАССОМ
def show_info(chat_id,user_class):
    for k,v in user_class.items():
                bot.send_message(chat_id, text=f"{k} {v}")
def add_info(user_message,user_class):
    src = user_message
    z = src.replace(" ","")
    try:
        if isinstance(int(z[:2]), int):
            formated_answer = z[:2]+" "+z[2::]
    except:
        formated_answer = z[:1]+" "+z[1::]
    for k,v in user_class.items():
        try:
            if isinstance(int(z[:2]), int):
                formated_answer = z[:2]+" "+z[2::]
                if formated_answer[:2].replace(" ","") == str(k):
                    with open("teachers-report.txt", "a", encoding="utf-8") as file:
                        file.write(f"{v}{formated_answer[2::]}\n")
        except:
            formated_answer = z[:1]+" "+z[1::]
            if formated_answer[:1].replace(" ","") == str(k):
                with open("teachers-report.txt", "a", encoding="utf-8") as file:
                    file.write(f"{v}{formated_answer[1::]}\n")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,text = 'Выберите номер ученика, а затем напишите причину отсутствия\nНапример:\n\n23 Болеет (Нажимаем отправить)\n12 Грипп (Нажимаем отправить)\n29 сем.обст (Нажимаем отправить)\n')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,text = 'Добро пожаловать!\nБот посещаемости учеников СГОШ №2\n\nСоздатели: @it_Vega, @M_R_XPy\n\nНаберите /help для помощи!')
    ###### ОТЧЕТ ДЛЯ ЗАМДИРЕКТОРА ######
    if message.from_user.id == 1942368353:
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         btn1 = types.KeyboardButton("Не сдавшие посещаемость")
         markup.add(btn1)
         bot.send_message(message.chat.id, text="Здравствуйте, {0.first_name}!Нажмите на кнопку, чтобы получить отчет!".format(message.from_user), reply_markup=markup)
    if message.from_user.id == 298749338:
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         btn2 = types.KeyboardButton("🗃️ Получить список")
         markup.add(btn2)
         bot.send_message(message.chat.id, text="Здравствуйте, {0.first_name}!Нажмите на кнопку, чтобы получить отчет!".format(message.from_user), reply_markup=markup)
    ###### КОНЕЦ ######

    ###### Показ учеников ######
    elif message.from_user.id == 71153118: ###### 4Б | 4В ######
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("4Б")
        btn2 = types.KeyboardButton("4В")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id, text="Выберите класс!".format(message.from_user), reply_markup=markup)
    elif message.from_user.id == 1031865770: ###### 1А ######
        show_info(message.chat.id, sc.one_A)
    elif message.from_user.id == 460062213: ###### 1Б ######
        show_info(message.chat.id, sc.one_B)
    elif message.from_user.id == 388852587: ###### 1В ######
        show_info(message.chat.id, sc.one_V)
    elif message.from_user.id == 200609249: ###### 2Б ######
        show_info(message.chat.id, sc.two_B)
    elif message.from_user.id == 243317636: ###### 3Г ######
        show_info(message.chat.id, sc.three_G)
    elif message.from_user.id == 354762468: ###### 4А ######
        show_info(message.chat.id, sc.four_A)
    elif message.from_user.id == 694142501: ###### 8А ######
        show_info(message.chat.id, sc.eight_A)
    elif message.from_user.id == 285756001: ###### 8Б ######
        show_info(message.chat.id, sc.eight_B)
    elif message.from_user.id == 5765395735: ###### 8В ######
        show_info(message.chat.id, sc.eight_V)
    elif message.from_user.id == 103310686: ###### 8Г ######
        show_info(message.chat.id, sc.eight_G)
    elif message.from_user.id == 565703310: ###### 8Д ######
        show_info(message.chat.id, sc.eight_D)
    elif message.from_user.id == 82621662: ###### 8Е ######
        show_info(message.chat.id, sc.eight_E)
    elif message.from_user.id == 179016974: ###### 8Ж ######
        show_info(message.chat.id, sc.eight_J)
    elif message.from_user.id == 401618354: ###### 8З ######
        show_info(message.chat.id, sc.eight_Z)
    elif message.from_user.id == 650387315: ###### 8И ######
        show_info(message.chat.id, sc.eight_I)
    #########################################################
    elif message.from_user.id == 123722752: ###### 9А ######
        show_info(message.chat.id, sc.nine_A)
    elif message.from_user.id == 755265305: ###### 9Б ######
        show_info(message.chat.id, sc.nine_B)
    elif message.from_user.id == 1956518849: ###### 9В ######
        show_info(message.chat.id, sc.nine_V)
    elif message.from_user.id == 330066737: ###### 9Г ######
        show_info(message.chat.id, sc.nine_G)
    elif message.from_user.id == 748603631: ###### 9Д ######
        show_info(message.chat.id, sc.nine_D)
    elif message.from_user.id == 786370293: ###### 9Е ######
        show_info(message.chat.id, sc.nine_E)
    elif message.from_user.id == 112450053: ###### 9Ж ######
        show_info(message.chat.id, sc.nine_J)
    #########################################################
    elif message.from_user.id == 251049864: ###### 10А ######
        show_info(message.chat.id, sc.ten_A)
    elif message.from_user.id == 39230730: ###### 10Б ######
        show_info(message.chat.id, sc.ten_B)
    elif message.from_user.id == 347673223: ###### 10Г ######
        show_info(message.chat.id, sc.ten_G)
    elif message.from_user.id == 438904641: ###### 10Д ######
        show_info(message.chat.id, sc.ten_D)
    elif message.from_user.id == 85970790: ###### 10Е ######
        show_info(message.chat.id, sc.ten_E)
    #########################################################
    elif message.from_user.id == 382110891: ###### 11А ######
        show_info(message.chat.id, sc.elev_A)
    elif message.from_user.id == 612643199: ###### 11Б ######
        show_info(message.chat.id, sc.elev_B)
    elif message.from_user.id == 888299252: ###### 11В ######
        show_info(message.chat.id, sc.elev_V)
    elif message.from_user.id == 1145686672: ###### 11Д ######
        show_info(message.chat.id, sc.elev_D)
    else:
        bot.send_message(message.chat.id, text=f"Вы не являетесь работником нашей школы или отсутствуют данные вашего класса!\nОбратитесь к администратору - @it_Vega, @M_R_XPy.")
    ###### КОНЕЦ ######
######################################################################################################
                                     # ЗАПИСЬ УЧЕНИКОВ #
######################################################################################################
@bot.message_handler(content_types=['text'])
def get_text_msg(message):
    if message.from_user.id == 71153118: ###### 4Б | 4В ######
        var_zero(message.chat.id, message.text, message.from_user.id, 71153118, "4Б", "4В", sc.four_B, sc.four_V)
    elif message.from_user.id == 1031865770: ###### 1А ######
        add_info(message.text, sc.one_A)
    elif message.from_user.id == 460062213: ###### 1Б ######
        add_info(message.text, sc.one_B)
    elif message.from_user.id == 388852587: ###### 1В ######
        add_info(message.text, sc.one_V)
    elif message.from_user.id == 243317636: ###### 3Г ######
        add_info(message.text, sc.three_G)
    elif message.from_user.id == 200609249: ###### 2Б ######
        add_info(message.text, sc.two_B)
    elif message.from_user.id == 354762468: ###### 4А ######
        add_info(message.text, sc.four_A)
    elif message.from_user.id == 694142501: ###### 8А ######
        add_info(message.text, sc.eight_A)
    elif message.from_user.id == 285756001: ###### 8Б ######
        add_info(message.text, sc.eight_B)
    elif message.from_user.id == 5765395735: ###### 8В ######
        add_info(message.text, sc.eight_V)
    elif message.from_user.id == 103310686: ###### 8Г ######
        add_info(message.text, sc.eight_G)
    elif message.from_user.id == 565703310: ###### 8Д ######
        add_info(message.text, sc.eight_D)
    elif message.from_user.id == 82621662: ###### 8Е ######
        add_info(message.text, sc.eight_E)
    elif message.from_user.id == 179016974: ###### 8Ж ######
        add_info(message.text, sc.eight_J)
    elif message.from_user.id == 401618354: ###### 8З ######
        add_info(message.text, sc.eight_Z)
    elif message.from_user.id == 650387315: ###### 8И ######
        add_info(message.text, sc.eight_I)
    #########################################################
    elif message.from_user.id == 123722752: ###### 9А ######
        add_info(message.text, sc.nine_A)
    elif message.from_user.id == 755265305: ###### 9Б ######
        add_info(message.text, sc.nine_B)
    elif message.from_user.id == 1956518849: ###### 9В ######
        add_info(message.text, sc.nine_V)
    elif message.from_user.id == 330066737: ###### 9Г ######
        add_info(message.text, sc.nine_G)
    elif message.from_user.id == 748603631: ###### 9Д ######
        add_info(message.text, sc.nine_D)
    elif message.from_user.id == 786370293: ###### 9Е ######
        add_info(message.text, sc.nine_E)
    elif message.from_user.id == 112450053: ###### 9Ж ######
        add_info(message.text, sc.nine_J)
    #########################################################
    elif message.from_user.id == 251049864: ###### 10А ######
        add_info(message.text, sc.ten_A)
    elif message.from_user.id == 39230730: ###### 10Б ######
        add_info(message.text, sc.ten_B)
    elif message.from_user.id == 347673223: ###### 10Г ######
        add_info(message.text, sc.ten_G)
    elif message.from_user.id == 438904641: ###### 10Д ######
        add_info(message.text, sc.ten_D)
    elif message.from_user.id == 85970790: ###### 10Е ######
        add_info(message.text, sc.ten_E)
    #########################################################
    elif message.from_user.id == 382110891: ###### 11А ######
        add_info(message.text, sc.elev_A)
    elif message.from_user.id == 612643199: ###### 11Б ######
        add_info(message.text, sc.elev_B)
    elif message.from_user.id == 888299252: ###### 11В ######
        add_info(message.text, sc.elev_V)
    elif message.from_user.id == 1145686672: ###### 11Д ######
        add_info(message.text, sc.elev_D)

######################################################################################################
                                        # АДМИНКА #
######################################################################################################
    elif message.from_user.id == 1942368353 and message.text == 'Не сдавшие посещаемость':
        if path.is_file():
            bot.send_message(message.chat.id, text="ПОСЕЩАЕМОСТЬ НЕ СДАЛИ!")
            with open("teachers-report.txt", "r", encoding="utf-8") as file:
                src = file.readlines()
                for i in src:
                    teachers.append(i[:3].replace(" ",""))
                for k,v in sc.teachers.items():
                    if k not in teachers:
                        bot.send_message(message.chat.id, text=v)
            bot.send_message(message.chat.id, text="#### Отчет по отсутствующим! ####")
            if os.stat(path).st_size == 0:
                bot.send_message(message.chat.id, text="Новых данных нет.")
            else:
                numbers_of_abs = []
                for k,v in Counter(teachers).items():
                    bot.send_message(message.chat.id, text=f"В {k} — отсутствует {v}")
                with open("teachers-report.txt", "r", encoding="utf-8") as file:
                    src = file.readlines()
                    for i in src:
                        numbers_of_abs.append(i[:3].replace(" ",""))
                    res = Counter(numbers_of_abs).values()
                bot.send_message(message.chat.id, text=f"Общее количество отсутствующих — {sum(res)}")
                teachers.clear()
        else:
            bot.send_message(message.chat.id, text="Нет данных")
    elif message.from_user.id == 298749338 and message.text == "🗃️ Получить список":
        if path.is_file():
            bot.send_message(message.chat.id, text="Получение списка! Ожидайте...")
            Report.compile_to_Excel()
            time.sleep(8)
            doc = open("Посещаемость.xlsx","rb")
            bot.send_document(298749338, doc)
            bot.send_message(message.chat.id, text="Готово!")
            #time.sleep(2)
            #os.remove('teachers-report.txt')
        else:
            error_msg = Report.compile_to_Excel()
            bot.send_message(message.chat.id, text=error_msg)
######################################################################################################
print("******************************\n******* СЕРВЕР ЗАПУЩЕН *******\n******************************")


bot.polling(none_stop=True, interval=0)