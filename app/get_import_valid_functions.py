from datetime import datetime,date
from collections import Counter
from time import time
import json

def apartment_valid(t):
    for x in t['citizens']:
        if not isinstance(x['apartment'],int):
            return False
        if x['apartment']<0:
            return False
    return True

def citizen_id_valid(t):
    for x in t['citizens']:
        if not isinstance(x['citizen_id'],int):
            return False
        if x['citizen_id']<0:
            return False
    tmp = [x['citizen_id'] for x in t['citizens']]
    return len(set(tmp))==len(tmp)

def gender_valid(t):
    for x in t['citizens']:
        if not isinstance(x['gender'],str):
            return False
        if x['gender'] not in ['male','female']:
            return False
    return True

def string_valid(t):
    for x in t['citizens']:
        if not isinstance(x['building'],str) or not isinstance(x['name'],str) or not isinstance(x['street'],str) or not isinstance(x['town'],str):
            return False
        if len(x['building'])==0 or len(x['name'])==0 or len(x['street'])==0 or len(x['town'])==0:
            return False
        if len(x['building'])>256 or len(x['name'])>256 or len(x['street'])>256 or len(x['town'])>256:
            return False
    return True

def relatives_valid(t):
    d_tmp = {}
    l = 0
    for x in t['citizens']:
        if not isinstance(x['relatives'],list):
            return False
        
        # ПРОВЕРКА НА ТО ЧТО КЛИЕНТ САМ У СЕБЯ В РОДСТВЕННИКАХ НЕ ИМЕЕТСЯ
        if x['citizen_id'] in x['relatives']:
            return False
        # ПРОВЕРКА НА ТО, ЧТО ДУБЛЕЙ НЕТ В РОДСТВЕННИКАХ
        if len(x['relatives'])!=len(set(x['relatives'])):
            return False
        l+=len(x['relatives'])
        d_tmp[x['citizen_id']]=x['relatives']
    if l==0:
        return True
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
        if len(set(columns) - set(x.keys()))>0:
            return False
    return True

