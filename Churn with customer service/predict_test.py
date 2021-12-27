#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('autosave', '0')


import requests


url='http://localhost:9696/predict'


customer={
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 24,
    "monthlycharges": 29.85,
    "totalcharges": (24*29.85)
}


response=requests.post(url,json=customer).json()
print(response)

custmer_id='xyz-123'
if response['churn']==True:
    print('sending promo to %s' %custmer_id)
else:
    print('not sending promo to %s' %custmer_id)

