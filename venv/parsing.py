import requests
from bs4 import BeautifulSoup
import datetime
import db
week = ['Понедельник', 'Вторник ', 'Среда' , 'Четверг ' , 'Пятница' , 'Суббота ' , 'Воскрсенье ']
#XUY
faculty = 3
kind = 2
group = 3
def type_week(name_group,day):
    faculty = db.find_number_group_for_parsing(name_group)[0]
    kind = db.find_number_group_for_parsing(name_group)[1]
    group = db.find_number_group_for_parsing(name_group)[2]
    res = requests.post('https://rsue.ru/raspisanie/', data={'f': faculty, 'k': kind, 'g': group})
    result = res.text
    soup = BeautifulSoup(result, 'lxml')
    # today = week[day]
    rasp = soup.find_all('div', {'class': 'col-lg-2 col-md-2 col-sm-2'})
    type_week = soup.find('h1', {'class': 'ned'})
    # return type_week.text
    return 'Нечетная неделя'
def rasp_day(name_group,day):
    faculty = db.find_number_group_for_parsing(name_group)[0]
    kind = db.find_number_group_for_parsing(name_group)[1]
    group = db.find_number_group_for_parsing(name_group)[2]
    res = requests.post('https://rsue.ru/raspisanie/',data={'f': faculty, 'k': kind, 'g': group})
    result = res.text
    soup = BeautifulSoup(result, 'lxml')
    # today = week[day]
    rasp = soup.find_all('div', {'class': 'col-lg-2 col-md-2 col-sm-2'})
    type_week = soup.find('h1',{'class':'ned'})
    if (len(rasp) / 2) <= day:
        return 'Пар нет'
    rasp = rasp[day+int((len(rasp)/2))]
    name_lesson = rasp.find_all('span', {'class': 'lesson'})
    name_lesson = [i.text for i in name_lesson]
    type_lesson = rasp.find_all('span', {'class': 'type'})
    type_lesson = [i.text for i in type_lesson]
    aud_lesson = rasp.find_all('span', {'class': 'aud'})
    aud_lesson = [i.text for i in aud_lesson]
    for i in aud_lesson:
        if i == '':
            aud_lesson.remove(i)
    time_lesson = rasp.find_all('span', {'class': 'time'})
    time_lesson = [i.text for i in time_lesson]
    prepod_lesson = rasp.find_all('span', {'class': 'prepod'})
    prepod_lesson = [i.text for i in prepod_lesson]
    number_lesson = 1
    lesson = {}
    for i in range(len(name_lesson)):
        lesson[f"lesson№{number_lesson}"] = {}
        lesson[f"lesson№{number_lesson}"]['name'] = name_lesson[i]
        lesson[f"lesson№{number_lesson}"]['type'] = type_lesson[i]
        lesson[f"lesson№{number_lesson}"]['aud'] = aud_lesson[i]
        lesson[f"lesson№{number_lesson}"]['time'] = time_lesson[i]
        lesson[f"lesson№{number_lesson}"]['prepod'] = prepod_lesson[i]
        number_lesson = number_lesson +1
    return lesson
rasp_day('ПРИ-321',0)
# def rasp_tomorow(name_group):
#     day = datetime.datetime.today().weekday() + 1
#     print (day)
#     if day > 6 :
#         day = day - 7
#     print(day)
#     faculty = db.find_number_group_for_parsing(name_group)[0]
#     kind = db.find_number_group_for_parsing(name_group)[1]
#     group = db.find_number_group_for_parsing(name_group)[2]
#     res = requests.post('https://rsue.ru/raspisanie/', data={'f': faculty, 'k': kind, 'g': group})
#     result = res.text
#     soup = BeautifulSoup(result, 'lxml')
#     today = week[day]
#     rasp = soup.find_all('div', {'class': 'col-lg-2 col-md-2 col-sm-2'})
#     rasp = rasp[day]
#     name_lesson = rasp.find_all('span', {'class': 'lesson'})
#     name_lesson = [i.text for i in name_lesson]
#     type_lesson = rasp.find_all('span', {'class': 'type'})
#     type_lesson = [i.text for i in type_lesson]
#     aud_lesson = rasp.find_all('span', {'class': 'aud'})
#     aud_lesson = [i.text for i in aud_lesson]
#     for i in aud_lesson:
#         if i == '':
#             aud_lesson.remove(i)
#     time_lesson = rasp.find_all('span', {'class': 'time'})
#     time_lesson = [i.text for i in time_lesson]
#     prepod_lesson = rasp.find_all('span', {'class': 'prepod'})
#     prepod_lesson = [i.text for i in prepod_lesson]
#     number_lesson = 1
#     lesson = {}
#     for i in range(len(name_lesson)):
#         lesson[f"lesson№{number_lesson}"] = {}
#         lesson[f"lesson№{number_lesson}"]['name'] = name_lesson[i]
#         lesson[f"lesson№{number_lesson}"]['type'] = type_lesson[i]
#         lesson[f"lesson№{number_lesson}"]['aud'] = aud_lesson[i]
#         lesson[f"lesson№{number_lesson}"]['time'] = time_lesson[i]
#         lesson[f"lesson№{number_lesson}"]['prepod'] = prepod_lesson[i]
#         number_lesson = number_lesson + 1
#     return lesson

def group(x):
    groups = []
    groups_nice = {}
    f1 = 1
    for f in range (7):
        f = f + 1
        groups_nice[f] = {}
        if f == 1 or f == 6 or f == 2 :
            k1 = 5
        else :
            k1 = 4
        for k in range(k1):
            k = k + 1
            groups_nice[f][k] = {}
            for g in range (10):
                g = g + 1
                res = requests.post('https://rsue.ru/raspisanie/',data={'f': f, 'k': k, 'g':g })
                result = res.text
                soup = BeautifulSoup(result, 'lxml')
                group = soup.find('h1')
                if group != None:
                    groups.append(group.text)
                    groups_nice[f][k][g] = group.text
                    # groups_nice[f][f"{k},{g}"] = group.text

        groups.pop(-1)
        print(f"{groups}")








