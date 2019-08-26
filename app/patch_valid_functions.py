from datetime import datetime,date
from collections import Counter
from time import time
import json

def apartment_valid_value(t):
    if not 'apartment' in t:
        return True
    if isinstance(t['apartment'],int):
        if t['apartment']>=0:
            return True
    return False

def gender_valid_value(t):
    if not 'gender' in t:
        return True
    if isinstance(t['gender'],str):
        if t['gender'] in ['male','female']:
            return True
    return False


def birth_date_valid_value(t):
    if not 'birth_date' in t:
        return True
    if isinstance(t['birth_date'],str):
        if len(t['birth_date'])>0:
            try:
                t = datetime.strptime(t['birth_date'], "%d.%m.%Y")
                # ПРОВЕРКА НА ТО, ЧТО ВОЗРАСТ БОЛЬШЕ ТЕКУЩЕЙ ДАТЫ
                if t >= datetime.now():
                    return False
                return True
            except:
                return False
            
    return False

def building_valid_value(t):
    if not 'building' in t:
        return True
    if isinstance(t['building'],str):
        if len(t['building'])>0 and len(t['building'])<=256:
            return True
    return False

def name_valid_value(t):
    if not 'name' in t:
        return True
    if isinstance(t['name'],str):
        if len(t['name'])>0 and len(t['name'])<=256:
            return True
    return False

def street_valid_value(t):
    if not 'street' in t:
        return True
    if isinstance(t['street'],str):
        if len(t['street'])>0 and len(t['street'])<=256:
            return True
    return False

def town_valid_value(t):
    if not 'town' in t:
        return True
    if isinstance(t['town'],str):
        if len(t['town'])>0 and len(t['town'])<=256:
            return True
    return False


def relatives_valid_value(t,citizen_id):
    if not 'relatives' in t:
        return True
    if isinstance(t['relatives'],list):
        if len(t['relatives'])>=0:
            # ПРОВЕРКА НА ТО, ЧТО СРЕДИ РОДСТВЕННИКОВ НЕТ ДУБ
            if len(t['relatives'])!=len(set(t['relatives'])):
                return False
            for x in t['relatives']:
                if not isinstance(x,int):
                    return False
            for x in t['relatives']:
                if x==citizen_id:
                    return False
            return True
    return False

def excess_fields_value(t):
    # ПРОВЕРКА НА ТО, ЧТО ОТСУТСТВУЮТ ЛИШНИЕ ПОЛЯ
    columns = set(['apartment', 'building', 'name', 'relatives', 'street', 'town','birth_date','gender'])
    for x in t.keys():
        if x not in columns:
            return False
#     if len(t.keys())!=len(set(columns)):
#         return False
    return True