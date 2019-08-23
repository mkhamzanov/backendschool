from datetime import datetime,date
from collections import Counter
from time import time
import json

def apartment_valid(t):
    for x in t['citizens']:
        if x['apartment']<0:
            return False
    return True

def citizen_id_valid(t):
    for x in t['citizens']:
        if x['citizen_id']<0:
            return False
    tmp = [x['citizen_id'] for x in t['citizens']]
    return len(set(tmp))==len(tmp)

def gender_valid(t):
    for x in t['citizens']:
        if x['gender'] not in ['male','female']:
            return False
    return True

def string_valid(t):
    for x in t['citizens']:
        if len(x['building'])==0 or len(x['name'])==0 or len(x['street'])==0 or len(x['town'])==0:
            return False
    return True

def relatives_valid(t):
    d_tmp = {}
    for x in t['citizens']:
        
        # ПРОВЕРКА НА ТО ЧТО КЛИЕНТ САМ У СЕБЯ В РОДСТВЕННИКАХ НЕ ИМЕЕТСЯ
        if x['citizen_id'] in x['relatives']:
            return False
        # ПРОВЕРКА НА ТО, ЧТО ДУБЛЕЙ НЕТ В РОДСТВЕННИКАХ
        if len(x['relatives'])!=len(set(x['relatives'])):
            return False
        d_tmp[x['citizen_id']]=x['relatives']
    for x in d_tmp:
        for y in d_tmp[x]:
            if y in d_tmp.keys():
                if x not in d_tmp[y]:
                    return False
    return True

def birth_date_valid(t):
    for x in t['citizens']:
        try:
            datetime.strptime(x['birth_date'], "%d.%m.%Y")
        except:
            return False
        # ПРОВЕРКА ЕСЛИ ДАТА РОЖДЕНИЯ БОЛЬШЕ ТЕКУЩЕЙ
        if datetime.strptime(x['birth_date'], "%d.%m.%Y") >= datetime.now():
            return False
    return True

def excess_fields(t):
    # ПРОВЕРКА НА ТО, ЧТО ОТСУТСТВУЮТ ЛИШНИЕ ПОЛЯ
    columns = set(['apartment', 'birth_date', 'building', 'citizen_id', 'gender', 'name', 'relatives', 'street', 'town'])
    for x in t['citizens']:
        if len(set(x.keys())) > len(columns):
            return False
    return True