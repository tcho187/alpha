#!/usr/bin/env python
# coding: utf-8

import requests
import pandas as df
import json


with open('test_set.json', ) as f:
    i = json.load(f)

first_row = i['data'][0]

mydict = [first_row]


backtojson = json.dumps(mydict)


# api-endpoint
URL = "http://localhost:5000/predict"

headers = {"Content-Type": "application/json; charset=utf-8"}
  
# sending get request and saving the response as response object
r = requests.post(url = URL, data = backtojson, headers=headers)
  
print(r.json())





