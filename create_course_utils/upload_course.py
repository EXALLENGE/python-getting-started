import os
import json

import requests


token = 'qwe123rty456'

URL = 'http://127.0.0.1/'
COURSE_PATH = '../meta/python/'


with open(f'{COURSE_PATH}meta.json') as json_file:
    data = json.load(json_file)
    print(data)
