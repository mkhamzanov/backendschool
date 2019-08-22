import json
import pandas as pd
from datetime import datetime,date
from collections import Counter
import numpy as np
import pymysql

def calculate_age_decimal(born):
    now = datetime.utcnow()
    return abs((now - born).days)/365.2425


def get_data_from_mysql_table_by_import_id(import_id):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Make17', db='sys',autocommit=True)
    cur = conn.cursor()
    sql = f"select * from new_schema.dataset where import_id={import_id}"
    cur.execute(sql)
    data = cur.fetchall()
    if len(data)>0:
        return {'citizens' : [{'citizen_id' : x[1],
                 'town' : x[2],
                 'street' : x[3],
                 'building' : x[4],
                 'apartment' : x[5],
                 'name' : x[6],
                 'birth_date' : x[7],
                 'gender' : x[8],
                 'relatives' : json.loads(x[9])} for x in data]}
    return False
def insert_dict_into_mysql_table(data, import_id):
    data = data['citizens']
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Make17', db='sys',autocommit=True)
    cur = conn.cursor()
    
    rows = [(import_id,x['citizen_id'],x['town'],x['street'],x['building'],
      x['apartment'],x['name'],x['birth_date'],x['gender'],json.dumps(x['relatives'])) for x in data]
    
    values = ', '.join(map(str, rows))
    sql = f"INSERT INTO new_schema.dataset VALUES {values}"
    cur.execute(sql)
def change_mysql_table_by_improt_id(data,import_id):
    data = data['citizens']
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Make17', db='sys',autocommit=True)
    cur = conn.cursor()
    sql_delete = f"DELETE FROM new_schema.dataset WHERE IMPORT_ID={import_id}"
    cur.execute(sql_delete)
    
    rows = [(import_id,x['citizen_id'],x['town'],x['street'],x['building'],
      x['apartment'],x['name'],x['birth_date'],x['gender'],json.dumps(x['relatives'])) for x in data]
    values = ', '.join(map(str, rows))
    sql_insert = f"INSERT INTO new_schema.dataset VALUES {values}"
    cur.execute(sql_insert)
def get_maximum_import_id_from_mysql_table():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Make17', db='sys',autocommit=True)
    cur = conn.cursor()
    sql = f"SELECT MAX(IMPORT_ID) FROM new_schema.dataset"
    cur.execute(sql)
    return cur.fetchall()[0][0]



def apartment_valid_value(t):
    if not 'apartment' in t:
        return True
    if isinstance(t['apartment'],int):
        if t['apartment']>=0:
            return True
    return False

def citizen_id_valid_value(t):
    if not 'citizen_id' in t:
        return True
    if isinstance(t['citizen_id'],int):
        if t['citizen_id']>=0:
            return True
    return False

def gender_valid_value(t):
    if not 'gender' in t:
        return True
    if isinstance(t['gender'],str):
        if t['gender'] in ['male','female']:
            return True
    return False

def building_valid_value(t):
    if not 'building' in t:
        return True
    if isinstance(t['building'],str):
        if len(t['building'])>0:
            return True
    return False

def name_valid_value(t):
    if not 'name' in t:
        return True
    if isinstance(t['name'],str):
        if len(t['name'])>0:
            return True
    return False

def street_valid_value(t):
    if not 'name' in t:
        return True
    if isinstance(t['street'],str):
        if len(t['street'])>0:
            return True
    return False

def town_valid_value(t):
    if not 'town' in t:
        return True
    if isinstance(t['town'],str):
        if len(t['town'])>0:
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
    columns = set(['apartment', 'birth_date', 'building', 'citizen_id', 'gender', 'name', 'relatives', 'street', 'town'])
    for x in t.keys():
        if x not in columns:
            return False
    return True



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


from time import time
from flask import Flask, jsonify
from flask import abort
from flask import json
from flask import request
import json as json_from_json

d = {}
import_id = 0

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/exports', methods=['GET'])
def get_tasks():
    global d
    return json_from_json.dumps(d,ensure_ascii=False)
    
@app.route('/imports', methods=['POST'])
def mm1():
    import_id = get_maximum_import_id_from_mysql_table() + 1
    t1 = time()
    t = request.json
    cond = (apartment_valid(t) and 
            citizen_id_valid(t) and 
            gender_valid(t) and 
            string_valid(t) and  
            relatives_valid(t) and 
            birth_date_valid(t) and
            excess_fields(t))    
    if cond:
        insert_dict_into_mysql_table(t, import_id)
        t2 = time()
        return json_from_json.dumps({'data' : {'import_id' : import_id}}), 201
    return abort(400)


@app.route('/imports/<int:import_id>/citizens/<int:citizen_id>', methods=['PATCH'])
def mm2(import_id,citizen_id):
    # ПРОВЕРКА НА ТО, ЧТО ДАННЫЙ ОТЧЕТ СУЩЕСТВУЕТ
    if import_id > get_maximum_import_id_from_mysql_table():
        abort(400)
    d = get_data_from_mysql_table_by_import_id(import_id)
    # ПРОВЕРКА НА ТО, ЧТО В ДАННОМ ОТЧЕТЕ ЕСТЬ ИНФОРМАЦИЯ О ДАННОМ ПОЛЬЗОВАТЕЛЕ
    if import_id > get_maximum_import_id_from_mysql_table():
        if citizen_id not in [x['citizen_id'] for x in d['citizens']]:
            abort(404)
    # СЧИТЫВАЕМ ДАННЫЕ     
    t = request.json
#     В запросе должно быть указано хотя бы одно поле
    if len(t)==0:
        abort(400)
    
    cond = (apartment_valid_value(t) & gender_valid_value(t) & building_valid_value(t) &
            name_valid_value(t) & street_valid_value(t) & town_valid_value(t) &
            relatives_valid_value(t,citizen_id) & birth_date_valid_value(t) & excess_fields_value(t))

#     ПРОВЕРКА НА ВАЛИДНОСТЬ ВХОДНЫХ ПАРАМЕТРОВ        
    if not cond:
            abort(400)

# ВСЕ ДАННЫЕ ПО-ИТОГУ ВАЛИДНЫЕ 
    data = d['citizens']
    
#     ИНДЕКС ПОЛЬЗОВАТЕЛЯ В СПИСКЕ(ОТЧЕТ)
    for i in range(len(data)):
        if data[i]['citizen_id']==citizen_id:
            index = i

    if 'relatives' in t.keys():
        
        #СТАРЫЙ СПИСОК СВЯЗЕЙ
        old_relatives = [x['relatives'] for x in data if x['citizen_id']==citizen_id][0]
        
        #НОВЫЙ СПИСОК СВЯЗЕЙ
        new_relatives = t['relatives']
        
        #СПИСОК ПОЛЬЗОВАТЕЛЕЙ, КОТОРЫХ НУЖНО УДАЛИТЬ У ВЫБРАННОГО КЛИЕНТА ИЗ ПОЛЯ relatives 
        delete = list(set(old_relatives) - set(new_relatives))
        
        #СПИСОК ПОЛЬЗОВАТЕЛЕЙ, КОТОРЫМ НУЖНО ДОБАВИТЬ В ПОЛЕ relatives ТЕКУЩЕГО ПОЛЬЗОВАТЕЛЯ
        add = list(set(new_relatives) - set(old_relatives))          
        
        for i in range(len(data)):        
            if data[i]['citizen_id'] in delete:
                array = data[i]['relatives']
                array.remove(citizen_id)
                data[i]['relatives'] = array
            if data[i]['citizen_id'] in add:
                array = data[i]['relatives']
                array.append(citizen_id)
                data[i]['relatives'] = array
                
# ЗАМЕНА СУЩЕСТВУЮШИХ ЗНАЧЕНИЙ
    for col in t.keys():
        data[index][col] = t[col]
    
    change_mysql_table_by_improt_id(d,import_id)
    
    return json_from_json.dumps({'data' : d}, ensure_ascii=False)


@app.route('/imports/<int:import_id>/citizens', methods=['GET'])
def mm3(import_id):
    if import_id > get_maximum_import_id_from_mysql_table():
        abort(400)
    else:
        return json_from_json.dumps({'data' : get_data_from_mysql_table_by_import_id(import_id)['citizens']},
                                    ensure_ascii=False)

@app.route('/imports/<int:import_id>/citizens/birthdays', methods=['GET'])
def mm4(import_id):
    if import_id > get_maximum_import_id_from_mysql_table():
        abort(400)
    else:
        
        data = get_data_from_mysql_table_by_import_id(import_id)['citizens']
        birth_month = {}
        for item in data:
            birth_month[item['citizen_id']] = datetime.strptime(item['birth_date'], "%d.%m.%Y").month
        
        output = {str(key) : [] for key in range(1,13)}
        
        for item in data:
            array = [birth_month[x] for x in item['relatives'] if x in birth_month]
            cnt = Counter(array)
            for x in cnt:
                output[str(x)].append({'citizen_id' : item['citizen_id'], 'relatives' : cnt[x]})
        return json_from_json.dumps({'data' : output}, ensure_ascii=False)

    
@app.route('/imports/<int:import_id>/towns/stat/percentile/age', methods=['GET'])
def mm5(import_id):
    if import_id > get_maximum_import_id_from_mysql_table():
        abort(400)
    else:
        data = get_data_from_mysql_table_by_import_id(import_id)['citizens']
        city_age = {}
        for item in data:
            
            born = datetime.strptime(item['birth_date'], "%d.%m.%Y")
            age = calculate_age_decimal(born)    
            
            if item['town'] in city_age:
                city_age[item['town']].append(age)
            else:
                city_age[item['town']]=[age]
        output = []
        for x in city_age:
            tmp = {"town": x,
                "p50": np.percentile(city_age[x], q = 50,interpolation='linear'),
                "p75": np.percentile(city_age[x], q = 75,interpolation='linear'),
                "p99": np.percentile(city_age[x], q = 99,interpolation='linear')}
            output.append(tmp)
        
        return json_from_json.dumps({'data' : output}, ensure_ascii=False)
    
if __name__ == '__main__':
    app.run()
    app.run(debug=True, threaded=True)