import pymysql
import json
from datetime import datetime,date

password = 'Test11'
schema = 'new_schema'
table = 'data'

def calculate_age(born):
    today = datetime.utcnow()
    year =  today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return year

def get_data_from_mysql_table_by_import_id(import_id):
    global password,schema,table
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=password, db='sys',autocommit=True)
    cur = conn.cursor()
    sql = f"select * from {schema}.{table} where import_id={import_id}"
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
    global password,schema,table
    data = data['citizens']
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=password, db='sys',autocommit=True)
    cur = conn.cursor()
    
    rows = [(import_id,x['citizen_id'],x['town'],x['street'],x['building'],
      x['apartment'],x['name'],x['birth_date'],x['gender'],json.dumps(x['relatives'])) for x in data]
    
    values = ', '.join(map(str, rows))
    sql = f"INSERT INTO {schema}.{table} VALUES {values}"
    cur.execute(sql)
    
def change_mysql_table_by_improt_id(data,import_id):
    global password,schema,table
    data = data['citizens']
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=password, db='sys',autocommit=True)
    cur = conn.cursor()
    sql_delete = f"DELETE FROM {schema}.{table} WHERE IMPORT_ID={import_id}"
    cur.execute(sql_delete)
    
    rows = [(import_id,x['citizen_id'],x['town'],x['street'],x['building'],
      x['apartment'],x['name'],x['birth_date'],x['gender'],json.dumps(x['relatives'])) for x in data]
    values = ', '.join(map(str, rows))
    sql_insert = f"INSERT INTO new_schema.data VALUES {values}"
    cur.execute(sql_insert)
    
    
def get_maximum_import_id_from_mysql_table():
    global password,schema,table
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=password, db='sys',autocommit=True)
    cur = conn.cursor()
    sql = f"SELECT MAX(IMPORT_ID) FROM {schema}.{table}"
    cur.execute(sql)
    return cur.fetchall()[0][0]
    

def get_data_from_mysql_table():
    global password,schema,table
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=password, db='sys',autocommit=True)
    cur = conn.cursor()
    sql = f"select * from {schema}.{table}"
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


