
# coding: utf-8

# In[177]:


import requests
import simplejson
from flask import Flask, jsonify, abort, request
import json
from datetime import datetime
import pymysql


# In[201]:


schema = 'new_schema'
table = 'data'
password = 'Make17'
main_url = "http://127.0.0.1:5000"


# In[202]:


def delete_all_rows_from_mysql_table():
    global password,schema,table
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=password, db='sys',autocommit=True)
    cur = conn.cursor()
    sql = f"DELETE FROM {schema}.{table} WHERE IMPORT_ID>0"
    cur.execute(sql)


# In[203]:


delete_all_rows_from_mysql_table()


# # main

# In[181]:


r = requests.get(main_url)
print(r.text)


# # get

# In[182]:


url = main_url + "/exports"
r = requests.get(url)
print(r.text[0:100])


# In[183]:


data = {
"citizens": [
{
"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [2]
},
{
"citizen_id": 2,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 7,
"name": "Иванов Сергей Иванович",
"birth_date": "17.04.1997",
"gender": "male",
"relatives": [1,3]
},
{
"citizen_id": 3,
"town": "Керчь",
"street": "Иосифа Бродского",
"building": "2",
"apartment": 11,
"name": "Романова Мария Леонидовна",
"birth_date": "23.11.1986",
"gender": "female",
"relatives": [2]
},
{
"citizen_id": 5,
"town": "Керчь",
"street": "Иосифа Бродского",
"building": "2",
"apartment": 11,
"name": "Романова Мария Леонидовна",
"birth_date": "23.11.1986",
"gender": "female",
"relatives": []
}
]}


# # Get all with params

# In[186]:


url = main_url + "/imports/0/citizens"
r = requests.get(url)
print(r.status_code, r.reason,
#       r.text
     )


# # post

#     БОЛЬШОЙ ЗАПРОС

# In[187]:


get_ipython().run_cell_magic('time', '', 'l = []\n# size_not_odd\nsize = 10001\nfor i in range(1,size):\n    t = {\n"citizen_id": i,\n"town": "Москва",\n"street": "Льва Толстого",\n"building": "jhg",\n"apartment": 126,\n"name": "Иванов Иван Иванович",\n"birth_date": "26.12.1986",\n"gender": "male",\n"relatives": [size - i]\n    }\n    l.append(t)\n    \ndata_size_valid = {\'citizens\' : l}\n    \napi_url = main_url + \'/imports\'\nr = requests.post(url=api_url, json=data_size_valid)\nprint(r.status_code, r.reason,r.text)')


#     ОБЫЧНЫЙ

# In[188]:


data_not_valid = {
"citizens": [
{
"citizen_id": 1,
"town": "Москва",
"street": "Льва Толстого",
"building": "jhg",
"apartment": 12,
"name": "Иванов Иван Иванович",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [2,3]
},
{
"citizen_id": 2,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 2,
"name": "s",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [4,8,1]
},
{
"citizen_id": 3,
"town": "Москва",
"street": "Льва Толстого",
"building": "16к7стр5",
"apartment": 2,
"name": "s",
"birth_date": "26.12.1986",
"gender": "male",
"relatives": [1]
}
]}



api_url = main_url + '/imports'
r = requests.post(url=api_url, json=data_not_valid)
print(r.status_code, r.reason,r.text)


# # patch

# In[189]:


get_ipython().run_cell_magic('time', '', "test_patch = {'apartment': 111,\n 'birth_date': '26.11.1986',\n 'building': '16к7стр5',\n 'gender': 'male',\n 'name': 'Иванов Иван Иванович',\n 'relatives': [2,3,4,5],\n 'street': 'Льва Толстого',\n 'town': 'saddsd'}\n\napi_url = main_url + '/imports/1/citizens/1'\nr = requests.patch(url=api_url, json=test_patch)\nprint(r.status_code, r.reason)")


# # patch big big

# In[190]:


get_ipython().run_cell_magic('time', '', "test_patch = {'apartment': 111,\n 'birth_date': '26.11.1986',\n 'building': '16к7стр5',\n 'gender': 'male',\n 'name': 'Иванов Иван Иванович',\n 'relatives': list(range(2,10000)),\n 'street': 'Льва Толстого',\n 'town': 'saddsd'}\n\napi_url = main_url + '/imports/1/citizens/1'\nr = requests.patch(url=api_url, json=test_patch)\nprint(r.status_code, r.reason)")


# # birthdays

# In[191]:


data_for_birthday = {
"citizens": [{'apartment': 111,
  'birth_date': '26.02.1986',
  'building': '16к7стр5',
  'citizen_id': 1,
  'gender': 'male',
  'name': 'Иванов Иван Иванович',
  'relatives': [2],
  'street': 'Льва Толстого',
  'town': 'saddsd'},
 {'apartment': 111,
  'birth_date': '26.07.1986',
  'building': '16к7стр5',
  'citizen_id': 2,
  'gender': 'male',
  'name': 'Иванов Иван Иванович',
  'relatives': [1,3,4],
  'street': 'Льва Толстого',
  'town': 'saddsd'},
        
 {'apartment': 111,
  'birth_date': '26.02.1986',
  'building': '16к7стр5',
  'citizen_id': 3,
  'gender': 'male',
  'name': 'Иванов Иван Иванович',
  'relatives': [2],
  'street': 'Льва Толстого',
  'town': 'saddsd'},
        
 {'apartment': 111,
  'birth_date': '26.02.1986',
  'building': '16к7стр5',
  'citizen_id': 4,
  'gender': 'male',
  'name': 'Иванов Иван Иванович',
  'relatives': [2,55],
  'street': 'Льва Толстого',
  'town': 'saddsd'}        
        
       ]}


# In[192]:


api_url = main_url + '/imports'
r = requests.post(url=api_url, json=data_for_birthday)
print(r.status_code, r.reason,r.text)


# In[193]:


get_ipython().run_cell_magic('time', '', "api_url = main_url + '/imports/1/citizens/birthdays'\nr = requests.get(url=api_url)\nprint(r.status_code, r.reason,\n#       r.text\n     )")


# In[194]:


get_ipython().run_cell_magic('time', '', "api_url = main_url + '/imports/1/citizens/birthdays'\nr = requests.get(url=api_url)\nprint(r.status_code, r.reason,\n#       r.text\n     )\n")


# # percentiles

# In[195]:


data_for_percentiles = {
"citizens": [{'apartment': 111,
  'birth_date': '26.01.1956',
  'building': '16к7стр5',
  'citizen_id': 1,
  'gender': 'male',
  'name': 'Иванов Иван Иванович',
  'relatives': [2],
  'street': 'Льва Толстого',
  'town': 'qweqeqweqwe'},
 {'apartment': 111,
  'birth_date': '26.07.1986',
  'building': '16к7стр5',
  'citizen_id': 2,
  'gender': 'male',
  'name': 'Иванов Иван Иванович',
  'relatives': [1,3,4],
  'street': 'Льва Толстого',
  'town': 'qweqeqweqwe'},
        
 {'apartment': 111,
  'birth_date': '26.02.1986',
  'building': '16к7стр5',
  'citizen_id': 3,
  'gender': 'male',
  'name': 'Иванов Иван Иванович',
  'relatives': [2],
  'street': 'Льва Толстого',
  'town': 'wwwweqe'},
        
 {'apartment': 111,
  'birth_date': '26.02.1986',
  'building': '16к7стр5',
  'citizen_id': 4,
  'gender': 'male',
  'name': 'Иванов Иван Иванович',
  'relatives': [2,55],
  'street': 'Льва Толстого',
  'town': 'ewqeqwe'}        
        
       ]}
data = data_for_percentiles['citizens']


# In[196]:


api_url = main_url + '/imports'
r = requests.post(url=api_url, json=data_for_percentiles)
print(r.status_code, r.reason,r.text)


# In[197]:


get_ipython().run_cell_magic('time', '', "api_url = main_url + '/imports/1/towns/stat/percentile/age'\nr = requests.get(url=api_url)\nprint(r.status_code, r.reason,r.text)")

