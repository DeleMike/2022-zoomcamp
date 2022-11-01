#!/usr/bin/env python
# coding: utf-8
import requests
host = 'heart-disease-checker-env.eba-nndkkwn3.eu-west-1.elasticbeanstalk.com'
url = f'http://{host}/predict'

patient = {"bmi": 29.84,
 "smoking": "no",
 "alcoholdrinking": "no",
 "stroke": "no",
 "physicalhealth": 5.0,
 "mentalhealth": 0.0,
 "diffwalking": "no",
 "sex": "male",
 "agecategory": "60-64",
 "race": "white",
 "diabetic": "no",
 "physicalactivity": "yes",
 "genhealth": "very good",
 "sleeptime": 8.0,
 "asthma": "no",
 "kidneydisease": "no",
 "skincancer": "no"}

response = requests.post(url, json=patient).json()
print(response)

if response['heart_disease'] > 0.5:
    print('sending recommeded treatments to %s' % ' patient_xyz')
else:
    print('not sending recommeded treatments to%s' % ' patient_xyz')
