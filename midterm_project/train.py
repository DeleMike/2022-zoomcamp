#!/usr/bin/env python
# coding: utf-8

# Mid Term Project 
# Heart Disease Indicator
# This script contains the best model to help identify or indicate the likelihood of heart disease

# import necessary libraries
import pandas as pd
import xgboost as xgb
import pickle
import bentoml

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

# Loading and Reading data
print('Loading data...')
df = pd.read_csv('heart_2020_cleaned.csv')
print('Finished loading data...')

# convert all columns to lower
df.columns = df.columns.str.lower()

# change all "string" data to lowercase
string_columns = list(df.dtypes[df.dtypes == 'object'].index)
for col in string_columns:
    df[col] = df[col].str.lower()
df['heartdisease'] = (df.heartdisease == 'yes').astype(int)

y = df['heartdisease']

numerical = ['bmi', 'physicalhealth', 'mentalhealth', 'sleeptime']
categorical = list(df.dtypes[df.dtypes == 'object'].index)

print('Preparing data...')
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

# reset indexes
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.heartdisease.values
y_val = df_val.heartdisease.values
y_test = df_test.heartdisease.values

# drop target column
df_train = df_train.drop('heartdisease', axis=1)
df_val = df_val.drop('heartdisease', axis=1)
df_test = df_test.drop('heartdisease', axis=1)
print('Finished preparing data.')

# Train / Build a model
print('Training model...')

dv = DictVectorizer(sparse=False)

train_dicts = df_train.to_dict(orient='records')
dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dicts)

val_dicts = df_val.to_dict(orient='records')
X_val = dv.transform(val_dicts)

# we have to convert our data to a form that can be processed by XGBoost
# features = dv.get_feature_names_out()
dtrain = xgb.DMatrix(X_train, label=y_train) # remove feature names to solve issue with bentoML
dval = xgb.DMatrix(X_val, label=y_val)

# the best model after tuning is
xgb_params = {
    'eta': 0.1, 
    'max_depth': 6,
    'min_child_weight': 1,
    
    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
}

xgb_model = xgb.train(xgb_params, dtrain, num_boost_round=200)
print('Finished training model.')


# Save the model
# hyper-parameters for xgb model
print('Saving model...')
eta = 0.1
max_depth = 6
min_child_weight = 1

output_file = 'xgb_model_with_dv_eta={}_max_depth={}_min_child_weight={}.bin'.format(eta, max_depth, min_child_weight)
with open(output_file, 'wb') as f_out:
    pickle.dump((dv, xgb_model), f_out)

# save model using Bentoml
bentoml.xgboost.save_model('heart_disease_risk_model', xgb_model,
                           custom_objects={
                               'dv':dv
                           })
print('Model has been saved as {}'.format(output_file))
