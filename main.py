import telebot
from telebot import types
import calendar
from datetime import datetime
from threading import Thread
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP



def schedule_returner(choise):#returns the schedule for a day/week
    datee=datetime.now()
    day_now=datee.day    
    data_1 = {
        'Понедельник': [
            {1:'Компьютерные языки разметки(лекция)'},
            {2:'Физическая культура'},
            {3:'Основы алгоритмизации и программирования(лаба)'},
            {4:'Линейная алгебра и аналитическая геометрия(практа)'}
        ],    
        'Вторник': [
            {1:'Компьютерные языки разметки.(лаба)'},
            {2:'Основы алгоритмизации и программирования(лаба)'},
            {3:'Технологии разработки программного обеспечения'}            
        ],
        'Среда': [
            {1:'Скриптовые языки программирования(лаба).'},
            {2:'Математический анализ(лаба)'},
            {3:'Линейная алгебра и аналитическая геометрия'}
            
        ],        
        'Четверг': [
            {1:'Основы алгоритмизации и программирования'},
            {2:'Физическая культура'},
            {3:'Скриптовые языки программирования'},
            {4:'Математический анализ(практа)'}
           
        ],        
        'Пятница': [
            {1:'Арифметико-логические основы вычислительных систем'},
            {2:'Английский(практа)'},
            {3:'Арифметико-логические основы вычислительных систем(практа)'}
            
        ],
        'Суббота': [
            {1:'Технологии разработки программного обеспечения(лаба)'},
            {2:'Математический анализ'}
            
        ]
        }

     

    data_2 = {
        'Понедельник': [
            {1:'Компьютерные языки разметки(лекция)'},
            {2:'Физическая культура'},
            {3:'Основы алгоритмизации и программирования(лаба)'},
            {4:'Линейная алгебра и аналитическая геометрия(практа)'}
        ],    
        'Вторник': [
            {1:'Компьютерные языки разметки.(лаба)'},
            {2:'Технологии разработки программного обеспечения'},
            
        ],
        'Среда': [
            {1:'Скриптовые языки программирования(лаба).'},
            {2:'Математический анализ(практа)'},
            {3:'Линейная алгебра и аналитическая геометрия'}
            
        ],        
        'Четверг': [
            {1:'Основы алгоритмизации и программирования'},
            {2:'Физическая культура'},
            {3:'Математический анализ'}
            
           
        ],        
        'Пятница': [
            {1:'Арифметико-логические основы вычислительных систем'},
            {2:'Английский(практа)'}
            
        ],
        'Суббота': [
            {1:'Технологии разработки программного обеспечения(лаба)'},
            {2:'Математический анализ'}
            
        ]
        }
            
    def returner_sch(day,index):#вывод дня
        returning_list_nums=[]
        returning_list_less=[]
        result=f'Расписание на\n'
        if index==1:
            for dicts in data_1.get(day):
                for key in dicts.keys():
                    returning_list_nums.append(key)

                for item in dicts.values():
                    returning_list_less.append(item)
                    
        elif index==2:
            for dicts in data_2.get(day):
                for key in dicts.keys():
                    returning_list_nums.append(key)
        

                for item in dicts.values():
                    returning_list_less.append(item)
                    
        for log in range(len(returning_list_nums)):
            result+=f'{returning_list_nums[log]} урок: {returning_list_less[log]}\n'
                                
        return result
    
    def returner_sch_week(index):#not even beautiful def(doesn't affect)вывод недели
        week_result='Расписание на неделю: \n'
        returning_list_nums=[]
        returning_list_less=[]
        result=''
        if index==1:
            for dicts in data_1.get("Понедельник"):
                for key in dicts.keys():
                    returning_list_nums.append(key)

                for item in dicts.values():
                    returning_list_less.append(item)
                    
        elif index==2:
            for dicts in data_2.get("Понедельник"):
                for key in dicts.keys():
                    returning_list_nums.append(key)

                for item in dicts.values():
                    returning_list_less.append(item)
            
        for log in range(len(returning_list_nums)):
            result+=f'{returning_list_nums[log]} урок: {returning_list_less[log]}\n'
        week_result+=f'Понедельник:\n {result}\n'
        
        ############################
        returning_list_nums=[]
        returning_list_less=[]
        result=''
        if index==1:
            for dicts in data_1.get("Вторник"):
                for key in dicts.keys():
                    returning_list_nums.append(key)

                for item in dicts.values():
                    returning_list_less.append(item)
                    
        elif index==2:
            for dicts in data_2.get("Вторник"):
                for key in dicts.keys():
                    returning_list_nums.append(key)

                for item in dicts.values():
                    returning_list_less.append(item)

        for log in range(len(returning_list_nums)):
            result+=f'{returning_list_nums[log]} урок: {returning_list_less[log]}\n'
        week_result+=f'Вторник:\n {result}\n'
        ############################
        returning_list_nums=[]
        returning_list_less=[]
        result=''
        if index==1:
            for dicts in data_1.get("Среда"):
                for key in dicts.keys():
                    returning_list_nums.append(key)

                for item in dicts.values():
                    returning_list_less.append(item)
                    
        elif index==2:
            for dicts in data_2.get("Среда"):
                for key in dicts.keys():
                    returning_list_nums.append(key)

                for item in dicts.values():
                    returning_list_less.append(item)
        for log in range(len(returning_list_nums)):
            result+=f'{returning_list_nums[log]} урок: {returning_list_less[log]}\n'
        week_result+=f'Среда:\n {result}\n'
        ##############################
        returning_list_nums=[]
        returning_list_less=[]
        result=''

        if index==1:
            for dicts in data_1.get("Четверг"):
                for key in dicts.keys():
                    returning_list_nums.append(key)

                for item in dicts.values():
                    returning_list_less.append(item)
                    
        elif index==2:
            for dicts in data_2.get("Четверг"):
                for key in dicts.keys():
                    returning_list_nums.append(key)

                for item in dicts.values():
                    returning_list_less.append(item)

        for log in range(len(returning_list_nums)):
            result+=f'{returning_list_nums[log]} урок: {returning_list_less[log]}\n'
        week_result+=f'Четверг:\n {result}\n'
        ##############################
        returning_list_nums=[]
        returning_list_less=[]
        result=''
        if index==1:
            for dicts in data_1.get("Пятница"):
                for key in dicts.keys():
                    returning_list_nums.append(key)

                for item in dicts.values():
                    returning_list_less.append(item)
                    
        elif index==2:
            for dicts in data_2.get("Пятница"):
                for key in dicts.keys():
                    returning_list_nums.append(key)

                for item in dicts.values():
                    returning_list_less.append(item)

        for log in range(len(returning_list_nums)):
            result+=f'{returning_list_nums[log]} урок: {returning_list_less[log]}\n'
        week_result+=f'Пятница:\n {result}\n'
        #############################
        returning_list_nums=[]
        returning_list_less=[]
        result=''
        if index==1:
            for dicts in data_1.get("Суббота"):
                for key in dicts.keys():
                    returning_list_nums.append(key)

                for item in dicts.values():
                    returning_list_less.append(item)
                    
        elif index==2:
            for dicts in data_2.get("Суббота"):
                for key in dicts.keys():
                    returning_list_nums.append(key)

                for item in dicts.values():
                    returning_list_less.append(item)

        for log in range(len(returning_list_nums)):
            result+=f'{returning_list_nums[log]} урок: {returning_list_less[log]}\n'
        week_result+=f'Суббота:\n {result}\n'
                
        return week_result

    
    if choise == "for_a_day":#prints schedule for a week
        day_now_in_week=datetime.today().isoweekday()
        if day_now_in_week == 1:
            return returner_sch("Понедельник",week_index)

        elif day_now_in_week == 2:
            return returner_sch("Вторник",week_index)
                
        elif day_now_in_week == 3:
            return returner_sch("Среда",week_index)
        
        elif day_now_in_week == 4:
            return returner_sch("Четверг",week_index)
        
        elif day_now_in_week == 5:
            return returner_sch("Пятница",week_index)
        
        elif day_now_in_week == 6:
            return returner_sch("Суббота",week_index)
        
        else:
            return "На выходние дни люди отдыхают(кроме тебя)"

    if choise == "for_a_week":#prints schedule for a week
        return returner_sch_week(week_index)
    
    

def hours_returner(choise):
    data_1 = {
        'Понедельник': [
            {'14:40-16:00':'Компьютерные языки разметки'},
            {'16:30-17:50':'Физическая культура'},
            {'18:05-19:25':'Основы алгоритмизации и программирования(лаба)'},
            {'19:40-21:00':'Линейная алгебра и аналитическая геометрия(практа)'}
        ],    
        'Вторник': [
            {'14:40-16:00':'Компьютерные языки разметки(лаба)'},
            {'16:30-17:50':'Основы алгоритмизации и программирования(лаба)'},
            {'18:05-19:25':'Технологии разработки программного обеспечения'}
        ],
        'Среда': [
            {'14:40-16:00':'Скриптовые языки программирования(лаба).'},
            {'16:30-17:50':'Математический анализ(лаба)'},
            {'18:05-19:25':'Линейная алгебра и аналитическая геометрия'}
        ],        
        'Четверг': [
            {'14:40-16:00':'Основы алгоритмизации и программирования'},
            {'16:30-17:50':'Физическая культура'},
            {'18:05-19:25':'Скриптовые языки программирования'},
            {'19:40-21:00':'Математический анализ(практа)'}
        ],        
        'Пятница': [
            {'14:40-16:00':'Арифметико-логические основы вычислительных систем'},
            {'16:30-17:50':'Английский(практа)'},
            {'18:05-19:25':'Арифметико-логические основы вычислительных систем(практа)'}
        ],
        'Суббота': [
            {'13:00-14:20':'Технологии разработки программного обеспечения(лаба)'},
            {'14:00-16:00':'Математический анализ'}
        ]
        } 

    data_2 = {
        'Понедельник': [
            {'14:40-16:00':'Компьютерные языки разметки(лекция)'},
            {'16:30-17:50':'Физическая культура'},
            {'18:05-19:25':'Основы алгоритмизации и программирования(лаба)'},
            {'19:40-21:00':'Линейная алгебра и аналитическая геометрия(практа)'}
        ],    
        'Вторник': [
            {'16:30-17:50':'Компьютерные языки разметки(лаба)'},
            {'18:05-19:25':'Технологии разработки программного обеспечения'}
        ],
        'Среда': [
            {'14:40-16:00':'Скриптовые языки программирования(лаба)'},
            {'16:30-17:50':'Математический анализ(практа)'},
            {'18:05-19:25':'Линейная алгебра и аналитическая геометрия'}
        ],        
        'Четверг': [
            {'14:40-16:00':'Основы алгоритмизации и программирования'},
            {'16:30-17:50':'Физическая культура'},
            {'18:05-19:25':'Математический анализ'}
        ],        
        'Пятница': [
            {'14:40-16:00':'Арифметико-логические основы вычислительных систем'},
            {'16:30-17:50':'Английский(практа)'}
        ],
        'Суббота': [
            {'13:00-14:20':'Технологии разработки программного обеспечения(лаба)'},
            {'14:00-16:00':'Математический анализ'}
        ]
        }

    def time_returner(hour_now, minutes_now):
        day_now_in_week=datetime.today().isoweekday()
        if day_now_in_week == 1:
            returning_list_nums=[]
            week_result=''
            result=''
            if week_index==1:
                for dicts in data_1.get("Понедельник"):
                    for key in dicts.keys():
                        returning_list_nums.append(key)
                        
            if week_index==2:
                for dicts in data_2.get("Понедельник"):
                    for key in dicts.keys():
                        returning_list_nums.append(key)
                        
            datee=datetime.now()            
            result=returning_list_nums[len(returning_list_nums)-1]
            time_spl=result.split('-')[1]
            hours_split=time_spl.split(':')[0]
            mins_split=time_spl.split(':')[1]
            date=datetime(2022,9,13,19,7)
            date_now=datetime(datee.year,datee.month,datee.day,datee.hour,datee.minute)
            point=datetime(datee.year,datee.month,datee.day,int(hours_split),int(mins_split))
            rez=point-date_now
            hours = str(abs(rez)).split(":")[0]
            mins = str(abs(rez)).split(":")[1].split(":")[0]
            week_result+=f'Конец пар в:\n {result}\n Конец через {hours} hours {mins} mins'
            return week_result
        
        if day_now_in_week == 2:#here it works
            returning_list_nums=[]
            week_result=''
            result=''
            if week_index==1:
                for dicts in data_1.get("Вторник"):
                    for key in dicts.keys():
                        returning_list_nums.append(key)
                        
            if week_index==2:
                for dicts in data_2.get("Вторник"):
                    for key in dicts.keys():
                        returning_list_nums.append(key)

            datee=datetime.now()            
            result=returning_list_nums[len(returning_list_nums)-1]
            time_spl=result.split('-')[1]
            hours_split=time_spl.split(':')[0]
            mins_split=time_spl.split(':')[1]
            date=datetime(2022,9,13,19,7)
            date_now=datetime(datee.year,datee.month,datee.day,datee.hour,datee.minute)
            point=datetime(datee.year,datee.month,datee.day,int(hours_split),int(mins_split))
            rez=point-date_now
            hours = str(abs(rez)).split(":")[0]
            mins = str(abs(rez)).split(":")[1].split(":")[0]
            week_result+=f'Конец пар в:\n {result}\n Конец через {hours} hours {mins} mins'
            return week_result
        
        if day_now_in_week == 3:
            returning_list_nums=[]
            week_result=''
            result=''
            if week_index==1:
                for dicts in data_1.get("Среда"):
                    for key in dicts.keys():
                        returning_list_nums.append(key)
                        
            if week_index==2:
                for dicts in data_2.get("Среда"):
                    for key in dicts.keys():
                        returning_list_nums.append(key)
                        
            datee=datetime.now()            
            result=returning_list_nums[len(returning_list_nums)-1]
            time_spl=result.split('-')[1]
            hours_split=time_spl.split(':')[0]
            mins_split=time_spl.split(':')[1]
            date=datetime(2022,9,13,19,7)
            date_now=datetime(datee.year,datee.month,datee.day,datee.hour,datee.minute)
            point=datetime(datee.year,datee.month,datee.day,int(hours_split),int(mins_split))
            rez=point-date_now
            hours = str(abs(rez)).split(":")[0]
            mins = str(abs(rez)).split(":")[1].split(":")[0]
            week_result+=f'Конец пар в:\n {result}\n Конец через {hours} hours {mins} mins'
            return week_result
        
        if day_now_in_week == 4:
            returning_list_nums=[]
            week_result=''
            result=''
            if week_index==1:
                for dicts in data_1.get("Четверг"):
                    for key in dicts.keys():
                        returning_list_nums.append(key)
                        
            if week_index==2:
                for dicts in data_2.get("Четверг"):
                    for key in dicts.keys():
                        returning_list_nums.append(key)
                        
            datee=datetime.now()            
            result=returning_list_nums[len(returning_list_nums)-1]
            time_spl=result.split('-')[1]
            hours_split=time_spl.split(':')[0]
            mins_split=time_spl.split(':')[1]
            date=datetime(2022,9,13,19,7)
            date_now=datetime(datee.year,datee.month,datee.day,datee.hour,datee.minute)
            point=datetime(datee.year,datee.month,datee.day,int(hours_split),int(mins_split))
            rez=point-date_now
            hours = str(abs(rez)).split(":")[0]
            mins = str(abs(rez)).split(":")[1].split(":")[0]
            week_result+=f'Конец пар в:\n {result}\n Конец через {hours} hours {mins} mins'
            return week_result

        if day_now_in_week == 5:
            returning_list_nums=[]
            week_result=''
            result=''
            if week_index==1:
                for dicts in data_1.get("Пятница"):
                    for key in dicts.keys():
                        returning_list_nums.append(key)
                        
            if week_index==2:
                for dicts in data_2.get("Пятница"):
                    for key in dicts.keys():
                        returning_list_nums.append(key)
                        
            datee=datetime.now()            
            result=returning_list_nums[len(returning_list_nums)-1]
            time_spl=result.split('-')[1]
            hours_split=time_spl.split(':')[0]
            mins_split=time_spl.split(':')[1]
            date=datetime(2022,9,13,19,7)
            date_now=datetime(datee.year,datee.month,datee.day,datee.hour,datee.minute)
            point=datetime(datee.year,datee.month,datee.day,int(hours_split),int(mins_split))
            rez=point-date_now
            hours = str(abs(rez)).split(":")[0]
            mins = str(abs(rez)).split(":")[1].split(":")[0]
            week_result+=f'Конец пар в:\n {result}\n Конец через {hours} hours {mins} mins'
            return week_result
        
        if day_now_in_week == 6:
            returning_list_nums=[]
            week_result=''
            result=''
            if week_index==1:
                for dicts in data_1.get("Суббота"):
                    for key in dicts.keys():
                        returning_list_nums.append(key)
                        
            if week_index==2:
                for dicts in data_2.get("Суббота"):
                    for key in dicts.keys():
                        returning_list_nums.append(key)
                        
            datee=datetime.now()            
            result=returning_list_nums[len(returning_list_nums)-1]
            time_spl=result.split('-')[1]
            hours_split=time_spl.split(':')[0]
            mins_split=time_spl.split(':')[1]
            date=datetime(2022,9,13,19,7)
            date_now=datetime(datee.year,datee.month,datee.day,datee.hour,datee.minute)
            point=datetime(datee.year,datee.month,datee.day,int(hours_split),int(mins_split))
            rez=point-date_now
            hours = str(abs(rez)).split(":")[0]
            mins = str(abs(rez)).split(":")[1].split(":")[0]
            week_result+=f'Конец пар в:\n {result}\n Конец через {hours} hours {mins} mins'
            return week_result
        
    def week_and_education_terurner(status):
        day_now_in_week=datetime.today().isoweekday()
        datee=datetime.now()
        day_now=datee.day
        weeks_in_month=calendar.monthcalendar(datee.year,datee.month)
        for week in weeks_in_month:
            if day_now in week:
                cache_num=1
                while week[len(week)-cache_num] == 0:
                    cache_num=cache_num+1
                    
                last_week_day=week[len(week)-cache_num]

        datetime_now=datetime.today()
        if status=='week':
            point=datetime(datee.year,datee.month,last_week_day)#конец недели
            
        elif status=='education':
            point=datetime(2026,6,30)
            
        until_time=point-datetime_now
        mm,ss=divmod(until_time.seconds,60)
        hh,mm=divmod(mm,60)
        return 'до даты {} осталось: {} дней, {} часов, {} минут, {} секунд'.format(point,abs(until_time.days),abs(hh),abs(mm),abs(ss))

               
    if choise=="until_day":
        time_now_hours=datetime.now().hour
        time_now_minutes=datetime.now().minute
        return time_returner(time_now_hours,time_now_minutes)
    
    if choise=="until_week":
        return week_and_education_terurner('week')

    if choise=="until_education":
        return week_and_education_terurner('education')
    
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
bot=telebot.TeleBot("5214184582:AAEP_U-5JSyRj6sS9_MW64VROTtljklZQfg")
@bot.message_handler(commands=["start"])
def start(message):
    if message.from_user.last_name != None: 
        mess=f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>, я попытаюсь помочь тебе с учёбой. Слева есть меню, там ты найдёшь всё самое нужное'
    elif message.from_user.last_name == None:
        mess=f'Привет, <b>{message.from_user.first_name} </b>, я попытаюсь помочь тебе с учёбой. Слева есть меню, там ты найдёшь всё самое нужное'
    else:
        mess=f'Привет, я попытаюсь помочь тебе с учёбой. Слева есть меню, там ты найдёшь всё самое нужное'
              
    bot.send_message(message.chat.id,mess,parse_mode="html")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
@bot.message_handler(commands=["laba_list"])
def labs_sender(message):#[['Основы алго', '1', 'no data', 'no message'], ['Основы алго', datetime.date(2022, 9, 22), 'Тест']]
    if len(labs_massive) == 0:
        bot.send_message(message.chat.id,"Текущих лаб нет😆")
        

    else:#[name, num, date, message]
        labs_result = ''
        for data_mass in labs_massive:
            labs_result+=f"\n\nЛабораторная работа №{labs_massive.index(data_mass)+1}\n"
            for i in range(len(data_mass)):
                if data_mass[i-1] == None:
                    print(labs_result)
                    pass
                
                else:
                    labs_result+=str(data_mass[i-1])
                    print(labs_result)
        print(labs_result)
        bot.send_message(message.chat.id,str(labs_result))

    
@bot.message_handler(commands=["schedule"])#check markup
def schedule(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='На день', callback_data="for_a_day"))
    markup.add(telebot.types.InlineKeyboardButton(text='На неделю', callback_data="for_a_week"))
    bot.send_message(message.chat.id, text="Выберите вариант:", reply_markup=markup)

@bot.message_handler(commands=["hours"])
def hours(message):
    now_hour = datetime.now().hour
    now_minute = datetime.now().minute    
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='До конца пар', callback_data="until_day"))
    markup.add(telebot.types.InlineKeyboardButton(text='До конца недели', callback_data="until_week"))
    markup.add(telebot.types.InlineKeyboardButton(text='До конца обучения', callback_data="until_education"))
    bot.send_message(message.chat.id, text="Выберите вариант:", reply_markup=markup)

    
#########################################################################################################################################
@bot.message_handler(commands=["laba_new"])#output of schedule on a day or week
def add_laba_1(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 1
    item1=types.KeyboardButton("Основы алгоритмизации и программирования")
    item2=types.KeyboardButton("Скриптовые языки программирования")
    item3=types.KeyboardButton("Компьютерные языки разметки")
    item4=types.KeyboardButton("Технологии разработки программного обеспечения")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,'По какой дисциплине вы хотите добавить лабу?',reply_markup=markup)
    
@bot.message_handler(content_types=["text"])
def static_reply(message):
    print("active reply")
    global laba_status1, laba_status2, laba_status3, laba_status4, laba_status5, laba_status6, laba_name, number_laba, result
    if message.text == 'Основы алгоритмизации и программирования' and laba_status1 == None:#Основы алго
        print("way1 selected")
        laba_status2 = "way_1"
        laba_status1 = None
        
    elif message.text == 'Скриптовые языки программирования' and laba_status1 == None:
        print("way2 selected")
        laba_status2 = "way_2"
        laba_status1 = None

    elif message.text == 'Компьютерные языки разметки' and laba_status1 == None:
        print("way3 selected")
        laba_status2 = "way_3"
        laba_status1 = None

    elif message.text == 'Технологии разработки программного обеспечения' and laba_status1 == None:
        print("way4 selected")
        laba_status2 = "way_4"
        laba_status1 = None


        
    elif message.text == 'Продолжить без заметки' and laba_status4 == "active":#done
        bot.send_message(message.chat.id,f'Хорошо, лаба добавлена на {result} по дисциплине {laba_name} без заметки', reply_markup=types.ReplyKeyboardRemove())
        laba_message='no message'
        laba_massive_cache = [laba_name, number_laba, result, laba_message]
        labs_massive.append(laba_massive_cache)
        laba_massive_cache=[]
        laba_status1=None
        laba_status2=None
        laba_status3=None
        laba_status4=None
        laba_status5=None
        laba_status6=None



    elif message.text and laba_status4 == 'active':#done
        laba_message = message.text
        bot.send_message(message.chat.id,f'Хорошо, лаба добавлена на {result} по дисциплине {laba_name} и с вашим сообщением!', reply_markup=types.ReplyKeyboardRemove())
        laba_massive_cache = [laba_name, result, laba_message]
        labs_massive.append(laba_massive_cache)
        laba_massive_cache=[]
        laba_status1=None
        laba_status2=None
        laba_status3=None
        laba_status4=None
        laba_status5=None
        laba_status6=None
        
    elif message.text and laba_status5 == 'active':#done
        laba_status5 = None
        laba_status2 = None
        if message.text == 'Продолжить без номера лабы':
            number_laba = 'no number'

        else:
            number_laba = str(message.text)
            
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Добавить дату")
        item2 = types.KeyboardButton("Без даты")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Хотите ли Вы добавить дату для будущей лабы?', reply_markup=markup)
        laba_status6='active'

    elif message.text == 'Добавить дату' and laba_status6 == 'active':
        calendar, step = DetailedTelegramCalendar().build()
        bot.send_message(message.chat.id, 'Выберите дату', reply_markup=calendar)

    elif message.text == "Без даты" and laba_status6 == 'active':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Продолжить без заметки")
        markup.add(item1)
        bot.send_message(message.chat.id,'Введите заметку(имя препода, доп. задания и т.д. или отмените создание заметки)',reply_markup=markup)
        laba_status4 = 'active'
        laba_status2 = None
        result = 'no data'
             
    else: #laba_status1 != 'Основы алго' or laba_status1 != 'Скрипт язык' or laba_status1 != 'Языки разм' or laba_status1 != 'Технологии разраба'
        bot.send_message(message.chat.id,'Неверная команда или значение👺')
        laba_status1 = None

    
            
    #ways of going forward
    if laba_status2 == "way_1":
        print('way one continue')
        laba_name = 'Основы алго'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Продолжить без номера лабы")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Введите номер лабораторной!', reply_markup=markup)
        laba_status5 = 'active'
        laba_status1 = None




@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def cal(c):
    global laba_status3, laba_status2, laba_status4, result
    result, key, step = DetailedTelegramCalendar().process(c.data)
    if not result and key:
        bot.edit_message_text('Выберите дату: 🧭', c.message.chat.id, c.message.message_id, reply_markup=key)
        
    elif result or c.message:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Продолжить без заметки")
        markup.add(item1)
        bot.edit_message_text(f"Вы выбрали {result}", c.message.chat.id, c.message.message_id)
        bot.send_message(c.message.chat.id,'Введите заметку(имя препода, доп. задания и т.д. или отмените создание заметки',reply_markup=markup)
        laba_status4 = 'active'
        laba_status2 = None
        
    
#########################################################################################################################################
        

'''

@bot.message_handler(content_types='text')#works with add_laba def
def message_reply(message):
    if message.text=="Кнопка":
        bot.send_message(message.chat.id,"https://habr.com/ru/users/lubaznatel/")
'''
    
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    #bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    answer = ''
    if call.data == 'for_a_day':
        answer = schedule_returner("for_a_day")
        
    elif call.data == 'for_a_week':
        answer = schedule_returner("for_a_week")
        
    elif call.data == 'until_day':#pro
        answer = hours_returner("until_day")
        
    elif call.data == 'until_week':
        answer = hours_returner("until_week")
        
    elif call.data == 'until_education':
        answer = hours_returner("until_education")
        
    bot.send_message(call.message.chat.id, answer)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    
def week_index_pool():#thread week poll
    global week_index, datee
    cache_now=0
    week_cache=0#input info maybe isoweekday module 
    week_index=1#input info
    while True:
        datee=datetime.now()
        day_now=datee.day
        if day_now!=cache_now:
            cache_now=day_now
            week_cache+=1
            
        if week_cache==8:
            week_cache=1#or 0 , maybe 1:(
            week_index+=1
            
        if week_index==3:
            week_index=1

laba_status1 = None
laba_status2 = None
laba_status3 = None
laba_status4 = None
laba_status5 = None
laba_status6 = None
result= ''
laba_name = ""
number_laba = ''
labs_massive = []
laba_massive_cache=[]
th1=Thread(target = week_index_pool)#thread settings
th1.start()#week_index thread polling
bot.polling(none_stop = True)#bot work
    
