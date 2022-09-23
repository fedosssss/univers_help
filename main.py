import telebot
from telebot import types
import calendar
from datetime import datetime
from threading import Thread


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
        result=f'{day}:\n'
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
        week_result=''
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
            print(week_index)
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
    datee=datetime.now()
    day_now=datee.day
    weeks_in_month=calendar.monthcalendar(datee.year,datee.month)
    for week in weeks_in_month:
        if day_now in week:
            week_index=int(weeks_in_month.index(week))+1
            if week_index%2==0:
                week_index=2
            else:
                week_index=1



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
            {'16:30-17:50':'Компьютерные языки разметки.(лаба)'},
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

    def time_returner(hour_now,minutes_now,day_now,week_index):
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
                        
            hour_now=datetime.now().hour
            mins_now=datetime.now().minute
            result=returning_list_nums[len(returning_list_nums)-1]
            time_spl=result.split('-')[1]
            hours_split=time_spl.split(':')[0]
            mins_split=time_spl.split(':')[1]
            if time_spl.find('0')==0:
                time_spl=time.split('-')[1].split(':')[1].replace("0",'')

            last_hours=int(hours_split)-int(hour_now)
            last_mins=int(mins_split)-int(mins_now)
            week_result+=f'Конец пар в:\n {result}\n Конец через {abs(last_hours)} hours {abs(last_mins)} mins'
            return week_result
        
        if day_now_in_week == 2:
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
            print(rez.strftime("%H")) 
            week_result+=f'Конец пар в:\n {result}\n Конец через {hourss} hours {minss} mins'
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
                        
            hour_now=datetime.now().hour
            mins_now=datetime.now().minute
            result=returning_list_nums[len(returning_list_nums)-1]
            time_spl=result.split('-')[1]
            hours_split=time_spl.split(':')[0]
            mins_split=time_spl.split(':')[1]
            if time_spl.find('0')==0:
                time_spl=time.split('-')[1].split(':')[1].replace("0",'')

            last_hours=int(hours_split)-int(hour_now)
            last_mins=int(mins_split)-int(mins_now)
            week_result+=f'Конец пар в:\n {result}\n Конец через {abs(last_hours)} hours {abs(last_mins)} mins'
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
                        
            hour_now=datetime.now().hour
            mins_now=datetime.now().minute
            result=returning_list_nums[len(returning_list_nums)-1]
            time_spl=result.split('-')[1]
            hours_split=time_spl.split(':')[0]
            mins_split=time_spl.split(':')[1]
            if time_spl.find('0')==0:
                time_spl=time.split('-')[1].split(':')[1].replace("0",'')

            last_hours=int(hours_split)-int(hour_now)
            last_mins=int(mins_split)-int(mins_now)
            week_result+=f'Конец пар в:\n {result}\n Конец через {abs(last_hours)} hours {abs(last_mins)} mins'
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
                        
            hour_now=datetime.now().hour
            mins_now=datetime.now().minute
            result=returning_list_nums[len(returning_list_nums)-1]
            time_spl=result.split('-')[1]
            hours_split=time_spl.split(':')[0]
            mins_split=time_spl.split(':')[1]
            if time_spl.find('0')==0:
                time_spl=time.split('-')[1].split(':')[1].replace("0",'')
                

            last_hours=int(hours_split)-int(hour_now)
            last_mins=int(mins_split)-int(mins_now)
            week_result+=f'Конец пар в:\n {result}\n Конец через {abs(last_hours)} hours {abs(last_mins)} mins'
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
                        
            hour_now=datetime.now().hour
            mins_now=datetime.now().minute
            result=returning_list_nums[len(returning_list_nums)-1]
            time_spl=result.split('-')[1]
            hours_split=time_spl.split(':')[0]
            mins_split=time_spl.split(':')[1]
            if time_spl.find('0')==0:
                time_spl=time.split('-')[1].split(':')[1].replace("0",'')

            last_hours=int(hours_split)-int(hour_now)
            last_mins=int(mins_split)-int(mins_now)
            week_result+=f'Конец пар в:\n {result}\n Конец через {abs(last_hours)} hours {abs(last_mins)} mins'
            return week_result
        
    def week_and_education_terurner(status):
        day_now_in_week=datetime.today().isoweekday()
        datee=datetime.now()
        day_now=datee.day
        weeks_in_month=calendar.monthcalendar(datee.year,datee.month)
        for week in weeks_in_month:
            if day_now in week:
                last_week_day=week[len(week)-1]

        datetime_now=datetime.today()
        if status=='week':
            point=datetime(datee.year,datee.month,last_week_day)#конец недели
            
        elif status=='education':
            point=datetime(2026,6,30)#конец недели
            
        until_week_time=point-datetime_now
        mm,ss=divmod(until_week_time.seconds,60)
        hh,mm=divmod(mm,60)
        print('до даты (point) осталось: {} дней, {} часов, {} минут, {} секунд'.format(d.days,hh,mm,ss))
        return 'до даты (point) осталось: {} дней, {} часов, {} минут, {} секунд'.format(d.days,hh,mm,ss)

        
        
    datee=datetime.now()
    day_now=datee.day
    weeks_in_month=calendar.monthcalendar(datee.year,datee.month)
    for week in weeks_in_month:
        if day_now in week:
            week_index=int(weeks_in_month.index(week))+1
            if week_index%2==0:
                week_index=2
            else:
                week_index=1
                
            
            
    if choise=="until_day":
        time_now_hours=datetime.now().hour
        time_now_minutes=datetime.now().minute
        return time_returner(time_now_hours,time_now_minutes,day_now,week_index)
    
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

@bot.message_handler(commands=["schedule"])#output of schedule on a day or week
def schedule(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='На день', callback_data="for_a_day"))
    markup.add(telebot.types.InlineKeyboardButton(text='На неделю', callback_data="for_a_week"))
    bot.send_message(message.chat.id, text="Выберите вариант:", reply_markup=markup)

@bot.message_handler(commands=["new_laba"])#output of schedule on a day or week
def add_laba(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Да, сегодня")
    item2=types.KeyboardButton("Нет, в другой день")
    markup.add(item1, item2)
    bot.send_message(message.chat.id,'Лабараторная была сегодня?',reply_markup=markup)

    

        
@bot.message_handler(content_types=["text"])
def static_reply(message):
    print("active reply")
    global laba_status
    if message.text == 'Да, сегодня':
        laba_status = "today"
        bot.send_message(message.chat.id,'Введите название')
        

    elif message.text == 'Нет, в другой день':
        laba_status = "another_day"
        bot.send_message(message.chat.id,'Bведите название')

    elif laba_status == "today" and message.text:
        print(message.text)
        laba_status = None

        
    
    #bot.send_message(message.chat.id,'Выберите корректный вариант ответа!')
        



@bot.message_handler(content_types='text')#works with add_laba def
def message_reply(message):
    if message.text=="Кнопка":
        bot.send_message(message.chat.id,"https://habr.com/ru/users/lubaznatel/")

        
    
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
        answer = "no data"
        
    '''elif call.data == 'laba_today':
        ansver
        


    
    elif call.data == 'laba_another_day':
        answer = "no data"'''

    bot.send_message(call.message.chat.id, answer)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
@bot.message_handler(commands=["hours"])
def hours(message):
    now_hour = datetime.now().hour
    now_minute = datetime.now().minute    
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='До конца пар', callback_data="until_day"))
    markup.add(telebot.types.InlineKeyboardButton(text='До конца недели', callback_data="until_week"))
    markup.add(telebot.types.InlineKeyboardButton(text='До конца обучения', callback_data="until_education"))
    bot.send_message(message.chat.id, text="Выберите вариант:", reply_markup=markup)



    
def week_index_pool():#thread week poll
    global week_index
    cache_now=0
    week_cache=0#input info
    week_index=2#input info
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
            
laba_status=None          
th1=Thread(target=week_index_pool)#thread settings
th1.start()#week_index thread polling
bot.polling(none_stop=True)#bot work
    
