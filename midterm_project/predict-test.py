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

#  {"bmi": 23.63,
#   "smoking": "no",
#   "alcohol_drinking": "no",
#   "stroke": "yes",
#   "physical_health": 0,
#   "mental_health": 15,
#   "diff_walking": "no",
#   "sex": "female",
#   "age_category": 11,
#   "race": "other",
#   "diabetic": "no",
#   "physical_activity": "yes",
#   "gen_health": 3,
#   "sleep_time": 8,
#   "asthma": "yes",
#   "kidney_disease": "yes",
#   "skin_cancer": "yes"}

response = requests.post(url, json=patient).json()
print(response)

if response['heart_disease'] > 0.5:
    print('sending recommeded treatments to %s' % ' patient_xyz')
else:
    print('not sending recommeded treatments to%s' % ' patient_xyz')
