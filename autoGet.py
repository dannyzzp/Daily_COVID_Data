# -*- coding: utf-8 -*-

"""
Created on Tue Aug  3 16:36:48 2021

@author: danny
"""
import pandas as pd
import numpy as np
import urllib.parse
import urllib.request
import urllib.error
import json
import ssl

url='https://api.covidactnow.org/v2/states.json?apiKey=614bb0c5e7f64dcf989097ac9d85fc63'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=url, headers=headers)
result=urllib.request.urlopen(req).read()
data=json.loads(result)

state=[]
new_cases=[]
new_deaths=[]

pop=[]
for d in data:
    state.append(d['state'])
    new_cases.append(d['actuals']['newCases'])
    new_deaths.append(d['actuals']['newDeaths'])

df=pd.DataFrame([state,new_cases,new_deaths])
df=df.transpose()
df.columns=['state', 'new_cases','new_deaths']

print(np.sum(df))


