import unittest
import requests
import datetime
from time import time
import json
class TestStringCalculator(unittest.TestCase):
    
    main_url = "http://127.0.0.1:5000"
    
    data = {
    "citizens": [{
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Иван Иванович",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [2]},
                {"citizen_id": 2,
                "town": "Москва",
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Сергей Иванович",
                "birth_date": "17.04.1997",
                "gender": "male",
                "relatives": [1,3]},
                    {"citizen_id": 3,
                    "town": "Керчь",
                    "street": "Иосифа Бродского",
                    "building": "2",
                    "apartment": 11,
                    "name": "Романова Мария Леонидовна",
                    "birth_date": "23.11.1986",
                    "gender": "female",
                    "relatives": [2]}]}    
    def test__server__runned(self):
        url = self.main_url
        r = requests.get(url)
        self.assertEqual(r.status_code, 200, 'Соединение установлено: код верный')    
# --------------------------------------------------------------------------------------
    def test_method__1__citizen_id__valid__true(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 201)
        
    def test_method__1__citizen_id__valid__false__less_than_null(self):
        data = self.data.copy()
        old = data['citizens'][1]['citizen_id']
        data['citizens'][1]['citizen_id']=0
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400) 
        data['citizens'][1]['citizen_id']=old

    def test_method__1__citizen_id__valid__false__not_unique(self):
        data = self.data.copy()
        old = data['citizens'][1]['citizen_id']
        data['citizens'][1]['citizen_id']=1 
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400)
        data['citizens'][1]['citizen_id']=old  
# --------------------------------------------------------------------------------------
    def test_method__1__town__valid__false__empty(self):
        data = self.data.copy()
        old = data['citizens'][1]['town']
        data['citizens'][1]['town']=''
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400)
        data['citizens'][1]['town']=old
        
    def test_method__1__town__valid__true(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 201)
        
    def test_method__1__town__valid__false__len_more_than_256(self):
        data = self.data.copy()
        old = data['citizens'][1]['town']
        data['citizens'][1]['town']='q'*258
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400)
        data['citizens'][1]['town']=old
# --------------------------------------------------------------------------------------
    def test_method__1__building__false(self):
        data = self.data.copy()
        old = data['citizens'][1]['building']
        data['citizens'][1]['building']=''
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400)
        data['citizens'][1]['building']=old
        
    def test_method__1__building__true(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 201)
        
    def test_method__1__building__valid__false__len_more_than_256(self):
        data = self.data.copy()
        old = data['citizens'][1]['building']
        data['citizens'][1]['building']='q'*258
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400)
        data['citizens'][1]['building']=old
# --------------------------------------------------------------------------------------
    def test_method__1__street__false(self):
        data = self.data.copy()
        old = data['citizens'][1]['street']
        data['citizens'][1]['street']=''
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400)
        data['citizens'][1]['street']=old
        
    def test_method__1__street__true(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 201)
        
    def test_method__1__street__valid__false__len_more_than_256(self):
        data = self.data.copy()
        old = data['citizens'][1]['street']
        data['citizens'][1]['street']='q'*258
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400)
        data['citizens'][1]['street']=old
# --------------------------------------------------------------------------------------
    def test_method__1__name__false(self):
        data = self.data.copy()
        old = data['citizens'][1]['name']
        data['citizens'][1]['name']=''
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400)
        data['citizens'][1]['name']=old
        
    def test_method__1__name__true(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 201)
        
    def test_method__1__name__valid__false__len_more_than_256(self):
        data = self.data.copy()
        old = data['citizens'][1]['name']
        data['citizens'][1]['name']='q'*258
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400)
        data['citizens'][1]['name']=old
# --------------------------------------------------------------------------------------
    def test_method__1__apartment__valid__true(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 201)
        
    def test_method__1__apartment__valid__false__less_than_null(self):
        data = self.data.copy()
        old = data['citizens'][1]['apartment']
        data['citizens'][1]['apartment']=0
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400) 
        data['citizens'][1]['apartment']=old
# --------------------------------------------------------------------------------------
    def test_method__1__birth__valid__true(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 201)
        
    def test_method__1__birth__valid__false__more_than_current_date(self):
        data = self.data.copy()
        old = data['citizens'][1]['birth_date']
        data['citizens'][1]['birth_date']='20.01.2100'
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400) 
        data['citizens'][1]['birth_date']=old
        
    def test_method__1__birth__valid__false___30_february(self):
        data = self.data.copy()
        old = data['citizens'][1]['birth_date']
        data['citizens'][1]['birth_date']='30.02.2018'
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400) 
        data['citizens'][1]['birth_date']=old
# --------------------------------------------------------------------------------------
    def test_method__1__relatives__valid__true(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 201)
        
    def test_method__1__relatives__valid__false__citizen_id_in_relatives(self):
        data = self.data.copy()
        old = data['citizens'][1]['relatives']
        data['citizens'][1]['relatives']=[2]
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400) 
        data['citizens'][1]['relatives']=old
        
    def test_method__1__relatives__valid__false__citizen_id_not_consists_in_relatives_of_own_relatives(self):
        data = self.data.copy()
        old = data['citizens'][1]['relatives']
        data['citizens'][1]['relatives']=[3]
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 400) 
        data['citizens'][1]['relatives']=old
        
    def test_method__1__relatives__valid__true__relatives_consist_citizen_id_that_not_in_import(self):
        data = self.data.copy()
        old = data['citizens'][1]['relatives']
        data['citizens'][1]['relatives']=old
        data['citizens'][1]['relatives'].extend([99,100])
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        self.assertEqual(r.status_code, 201) 
        data['citizens'][1]['relatives']=old
        
    def test_method__1__relatives__valid__true__all_relatives_list_is_emprty(self):
        tmp_data = {"citizens": [{
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Иван Иванович",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": []},
                {"citizen_id": 2,
                "town": "Москва",
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Сергей Иванович",
                "birth_date": "17.04.1997",
                "gender": "male",
                "relatives": []},
                    {"citizen_id": 3,
                    "town": "Керчь",
                    "street": "Иосифа Бродского",
                    "building": "2",
                    "apartment": 11,
                    "name": "Романова Мария Леонидовна",
                    "birth_date": "23.11.1986",
                    "gender": "female",
                    "relatives": []}]}
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=tmp_data)
        self.assertEqual(r.status_code, 201)
        
    def test_method__1__relatives__valid__true__all_citizen_id_is_relatives_between_themselves(self):
        tmp_data = {
    "citizens": [{
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Иван Иванович",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [2,3]},
                {"citizen_id": 2,
                "town": "Москва",
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Сергей Иванович",
                "birth_date": "17.04.1997",
                "gender": "male",
                "relatives": [1,3]},
                    {"citizen_id": 3,
                    "town": "Керчь",
                    "street": "Иосифа Бродского",
                    "building": "2",
                    "apartment": 11,
                    "name": "Романова Мария Леонидовна",
                    "birth_date": "23.11.1986",
                    "gender": "female",
                    "relatives": [1,2]}]}
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=tmp_data)
        self.assertEqual(r.status_code, 201)
# --------------------------------------------------------------------------------------
    def test_method__1__false__excess_field(self):
        tmp_data = {
    "citizens": [{
        "excess" : "test",
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Иван Иванович",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [2,3]},
                {"citizen_id": 2,
                "town": "Москва",
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Сергей Иванович",
                "birth_date": "17.04.1997",
                "gender": "male",
                "relatives": [1,3]},
                    {"citizen_id": 3,
                    "town": "Керчь",
                    "street": "Иосифа Бродского",
                    "building": "2",
                    "apartment": 11,
                    "name": "Романова Мария Леонидовна",
                    "birth_date": "23.11.1986",
                    "gender": "female",
                    "relatives": [1,2]}]}
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=tmp_data)
        self.assertEqual(r.status_code, 400)

    def test_method__1__false__no_field_needed(self):
        tmp_data = {
    "citizens": [{
            "citizen_id": 1,
            "street": "Льва Толстого",
            "building": "16к7стр5",
            "name": "Иванов Иван Иванович",
            "birth_date": "26.12.1986",
            "gender": "male",
            "relatives": [2,3]},
                {"citizen_id": 2,
                "town": "Москва",
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Сергей Иванович",
                "birth_date": "17.04.1997",
                "gender": "male",
                "relatives": [1,3]},
                    {"citizen_id": 3,
                    "town": "Керчь",
                    "street": "Иосифа Бродского",
                    "building": "2",
                    "apartment": 11,
                    "name": "Романова Мария Леонидовна",
                    "birth_date": "23.11.1986",
                    "gender": "female",
                    "relatives": [1,2]}]}
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=tmp_data)
        self.assertEqual(r.status_code, 400)

# --------------------------------------------------------------------------------------
    def test_method__1__true___time_less_10_second_if_more_than_10000_citizens(self):
        t1 = time()
        l = []
        # size_not_odd
        size = 10001
        for i in range(1,size):
            t = {
                    "citizen_id": i,
                    "town": "Москва",
                    "street": "Льва Толстого",
                    "building": "jhg",
                    "apartment": 111,
                    "name": "Иванов Иван Иванович",
                    "birth_date": "26.12.1986",
                    "gender": "male",
                    "relatives": [size - i]
                        }
            l.append(t)
            
        l.append({
                    "citizen_id": size+1,
                    "town": "Москва",
                    "street": "Льва Толстого",
                    "building": "jhg",
                    "apartment": 111,
                    "name": "Иванов Иван Иванович",
                    "birth_date": "26.12.1986",
                    "gender": "male",
                    "relatives": list(range(size+2,2*size))
                        })
        tmp_data = {'citizens' : l}
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=tmp_data)
        t2 = time()
        self.assertTrue(t2-t1 < 10)
        
# --------------------------------------------------------------------------------------
    def test_method__2__false___no_field_needed(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        
        
        
        test_patch = {
#                 "town": "Москва",
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Сергей Иванович",
                "relatives": [1,3]}
        
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 200)

    def test_method__2__false___excess_field(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                "excess": "Москва",
                      "town": "Москва",
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Сергей Иванович",
                "relatives": [1,3]}
        
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
# --------------------------------------------------------------------------------------
    def test_method__2__town_valid__false___value_is_null(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                      "town": "",
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Сергей Иванович",
                "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
        
    def test_method__2__street_valid__false___value_is_null(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                      "town": "asdasd",
                "street": "",
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Сергей Иванович",
                "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
        
        
    def test_method__2__building_valid__false___value_is_null(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                      "town": "asdasd",
                "street": "asdasd",
                "building": "",
                "apartment": 7,
                "name": "Иванов Сергей Иванович",
                "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
        
    def test_method__2__name_valid__false___value_is_null(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                      "town": "asdasd",
                "street": "asdasd",
                "building": "asdasd",
                "apartment": 7,
                "name": "",
                "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
# --------------------------------------------------------------------------------------
    def test_method__2__town_valid__false___value_other_type(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                      "town": [],
                "street": "Льва Толстого",
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Сергей Иванович",
                "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
        
    def test_method__2__street_valid__false___value_other_type(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                      "town": "asdasd",
                "street": [],
                "building": "16к7стр5",
                "apartment": 7,
                "name": "Иванов Сергей Иванович",
                "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
        
        
    def test_method__2__building_valid__false___value_other_type(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                      "town": "asdasd",
                "street": "asdasd",
                "building": [],
                "apartment": 7,
                "name": "Иванов Сергей Иванович",
                "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
        
    def test_method__2__name_valid__false___value_other_type(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                      "town": "asdasd",
                "street": "asdasd",
                "building": "asdasd",
                "apartment": 7,
                "name": [],
                "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
# --------------------------------------------------------------------------------------
    def test_method__2__apartment_valid__false___value_other_type(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                      "town": "asdasd",
                "street": "asdasd",
                "building": "asdasd",
                "apartment": "asdasd",
                "name": "asdasd",
                "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
    def test_method__2__apartment_valid__true(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                      "town": "asdasd",
                "street": "asdasd",
                "building": "asdasd",
                "apartment": 43,
                "name": "asdasd",
                "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 200)
        
    def test_method__2__apartment_valid__false___less_than_0(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                      "town": "asdasd",
                "street": "asdasd",
                "building": "asdasd",
                "apartment": -1,
                "name": "asdasd",
                    "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
# --------------------------------------------------------------------------------------
    def test_method__2__birth_date__valid__false___value_other_type(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                      "town": "asdasd",
            "birth_date" : [],
                "street": "asdasd",
                "building": "asdasd",
                "apartment": "asdasd",
                "name": "asdasd",
                "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
    def test_method__2__birth_date_valid__true(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                      "town": "asdasd",
            "birth_date" : "20.02.2018",
                "street": "asdasd",
                "building": "asdasd",
                "apartment": 43,
                "name": "asdasd",
                "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 200)
        
    def test_method__2__birth_date_valid__false___birth_date_after_today(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
                      "town": "asdasd",
            "birth_date" : "20.02.2222",
                "street": "asdasd",
                "building": "asdasd",
                "apartment": 23,
                "name": "asdasd",
                    "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
# --------------------------------------------------------------------------------------
    def test_method__2__gender__valid__false___value_other_type(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
            "gender" : []}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
    def test_method__2__gender__valid__true(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
             "gender" : "male",
               }
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 200)
        
    def test_method__2__gender__valid__false___other_values(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        self.assertEqual(r.status_code, 201)
        test_patch = {
            "gender" : "male222",
               }
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 400)
# --------------------------------------------------------------------------------------
    def test_method__2__relatives_valid__true__not__changes(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        test_patch = {
                    "relatives": [1,3]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        self.assertEqual(r.status_code, 200)
        
    def test_method__2__relatives_valid__true__case_1(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        test_patch = {
                    "relatives": []}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        
        url = self.main_url + "/imports/" +str(int(import_id)) +  "/citizens"
        d = json.loads(requests.get(url).text)
        self.assertEqual(d['data'][0]['relatives'], [])
        self.assertEqual(d['data'][2]['relatives'], [])
        
    def test_method__2__relatives_valid__true__case_2(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        test_patch = {
                    "relatives": [1,3,5,6,7]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        
        url = self.main_url + "/imports/" +str(int(import_id)) +  "/citizens"
        d = json.loads(requests.get(url).text)
        
        self.assertEqual(d['data'][0]['relatives'], [2])
        self.assertEqual(d['data'][2]['relatives'], [2])
        self.assertEqual(d['data'][1]['relatives'], [1,3,5,6,7])
        
# --------------------------------------------------------------------------------------
    def test_method__2__emprty_patch__false(self):
        data = self.data.copy()
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=data)
        t2 = time()
        import_id = json.loads(r.text)['data']['import_id']
        test_patch = {}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        
        url = self.main_url + "/imports/" +str(int(import_id)) +  "/citizens"
        self.assertEqual(r.status_code, 400)
        
    def test_method__2__true___case_3(self):
        t1 = time()
        l = []
        # size_not_odd
        size = 10001
        for i in range(1,size):
            t = {
                    "citizen_id": i,
                    "town": "Москва",
                    "street": "Льва Толстого",
                    "building": "jhg",
                    "apartment": 111,
                    "name": "Иванов Иван Иванович",
                    "birth_date": "26.12.1986",
                    "gender": "male",
                    "relatives": [size - i]
                        }
            l.append(t)
        tmp_data = {'citizens' : l}
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=tmp_data)
        import_id = json.loads(r.text)['data']['import_id']
                
        test_patch = {"relatives": [1]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)

        url = self.main_url + "/imports/" +str(int(import_id)) +  "/citizens"
        d = json.loads(requests.get(url).text)
        
        self.assertEqual(d['data'][1]['relatives'], [1])
        self.assertEqual(set(d['data'][0]['relatives']), set([2,size-1]))
        self.assertEqual(d['data'][-2]['relatives'], [])
        
        
        
    def test_method__2__true___change__time_less_10_second_if_more_than_10000_citizens(self):
        t1 = time()
        l = []
        # size_not_odd
        size = 10001
        for i in range(1,size):
            t = {
                    "citizen_id": i,
                    "town": "Москва",
                    "street": "Льва Толстого",
                    "building": "jhg",
                    "apartment": 111,
                    "name": "Иванов Иван Иванович",
                    "birth_date": "26.12.1986",
                    "gender": "male",
                    "relatives": [size - i]
                        }
            l.append(t)
            
        l.append({
                    "citizen_id": size+1,
                    "town": "Москва",
                    "street": "Льва Толстого",
                    "building": "jhg",
                    "apartment": 111,
                    "name": "Иванов Иван Иванович",
                    "birth_date": "26.12.1986",
                    "gender": "male",
                    "relatives": list(range(size+2,2*size))
                        })
        tmp_data = {'citizens' : l}
        api_url = self.main_url + '/imports'
        r = requests.post(url=api_url, json=tmp_data)
        import_id = json.loads(r.text)['data']['import_id']
                
        test_patch = {"relatives": [1]}
        api_url = self.main_url + '/imports/' + str(int(import_id)) + '/citizens/2'
        r = requests.patch(url=api_url, json=test_patch)
        t2 = time()
        self.assertEqual(r.status_code, 200)
        self.assertTrue(t2-t1 < 10)
        
        
        
        
#         url = self.main_url + "/imports/" +str(int(import_id)) +  "/citizens"
#         self.assertEqual(r.status_code, 200)
        
unittest.main(argv=[''],
              verbosity=2, 
              exit=False)