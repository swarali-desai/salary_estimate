'''
created on September 08, 2020
Author: swarali desai
'''
import requests
from data_input import dummy_data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": dummy_data_in}

r = requests.get(URL,headers=headers, json=data) 

print(r.json())