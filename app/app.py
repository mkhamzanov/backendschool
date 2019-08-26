import json as json_from_json
import numpy as np

from datetime import datetime,date
from collections import Counter
from time import time


from flask import Flask, jsonify,abort,json,request


from database_functions import *
from get_import_valid_functions import *
from patch_valid_functions import *

app = Flask(__name__)
@app.route('/imports', methods=['POST'])
def mm1():
    import_id = get_maximum_import_id_from_mysql_table() + 1
    t1 = time()
    t = request.json
    
    if not excess_fields(t):
        abort(400)
    
    cond = (apartment_valid(t) and 
            citizen_id_valid(t) and 
            gender_valid(t) and 
            string_valid(t) and  
            relatives_valid(t) and 
            birth_date_valid(t))    
    if cond:
        insert_dict_into_mysql_table(t, import_id)
        t2 = time()
        return json_from_json.dumps({'data' : {'import_id' : import_id}}), 201
    return abort(400)


@app.route('/imports/<int:import_id>/citizens/<int:citizen_id>', methods=['PATCH'])
def mm2(import_id,citizen_id):
    if citizen_id<0:
        abort(404)
    
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
            
    cond = (apartment_valid_value(t) & building_valid_value(t) & gender_valid_value(t) & birth_date_valid_value(t) &
            name_valid_value(t) & street_valid_value(t) & town_valid_value(t) &
            relatives_valid_value(t,citizen_id) & excess_fields_value(t))

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
            age = calculate_age(born)    
            
            if item['town'] in city_age:
                city_age[item['town']].append(age)
            else:
                city_age[item['town']]=[age]
        output = []
        for x in city_age:
            tmp = {"town": x,
                "p50": round(np.percentile(city_age[x], q = 50,interpolation='linear'),2),
                "p75": round(np.percentile(city_age[x], q = 75,interpolation='linear'),2),
                "p99": round(np.percentile(city_age[x], q = 99,interpolation='linear'),2)}
            output.append(tmp)
        
        return json_from_json.dumps({'data' : output}, ensure_ascii=False)
    
if __name__ == '__main__':
    app.run()
    app.run(debug=True, threaded=True)