# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m5lOSreOFmlMJCmujx6uz4SFNmBCSpmf
"""

import urllib.request

url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
urllib.request.urlretrieve(url, '1.json')

import json
with open("1.json", 'r') as f:
    data = json.load(f)

print(data)

import pandas as pd
df = pd.DataFrame.from_dict(data['products'],orient='index')

df.head()

df['popularity'] = df['popularity'].astype(int)

df.dtypes

df = df.sort_values(by='popularity',ascending=False)
df.head()

df.to_csv('ex.csv')
df.to_html('index.html')