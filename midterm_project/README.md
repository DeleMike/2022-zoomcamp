# Heart Disease Indicator

## Dataset Description

_[Original dataset found here](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease)_

Originally, the dataset come from the CDC (Centers for Disease Control and Prevention) and is a major part of the Behavioral Risk Factor Surveillance System (BRFSS), which conducts annual telephone surveys to gather data on the health status of U.S. residents.

According to the CDC, heart disease is one of the leading causes of death for people of most races in the US (AAfrican Americans, American Indians and Alaska Natives, and white people). About half of all Americans (47%) have at least 1 of 3 key risk factors for heart disease: high blood pressure, high cholesterol, and smoking. Other key indicator include diabetic status, obesity (high BMI), not getting enough physical activity or drinking too much alcohol. Detecting and preventing the factors that have the greatest impact on heart disease is very important in healthcare. Computational developments, in turn, allow the application of machine learning methods to detect "patterns" from the data that can predict a patient's condition.

## Attribute Information

      - Heart Disease: have they reported of having heart disease? (Yes/No)
      - BMI: Body Mass Index (BMI)
      - Smoking: Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]? (Yes/No)
      - AlcoholDrinking: Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week ? (Yes/No)
      - Stroke: (Ever told) (you had) a stroke? (Yes/No)
      - PhysicalHealth: Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 ?
      - MentalHealth: Thinking about your mental health, for how many days during the past 30 days was your mental health not good?
      - DiffWalking: Do you have serious difficulty walking or climbing stairs? (Yes/No)
      - Sex: Male or Female
      - AgeCategory: (Range): (45-49), (70-74), (20-24), etc
      - Race: Imputed race/ethnicity value
      - Diabetic: (Ever told) (you had) diabetes?
      - Physical Activity? Adults who reported doing physical activity or exercise during the past 30 days other than their regular job (Yes/No)
      - GenHealth: Would you say that in general your health is? (A range of values)
      - SleepTime: On average, how many hours of sleep do you get in a 24-hour period?
      - Asthma: (Ever told) (you had) asthma? (Yes/No)
      - KidneyDisease: Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease? 
      - SkinCancer: (Ever told) (you had) skin cancer?

## Problem Description

As described above, heart disease is one of the leading causes of death in most races, hence the problem we are solving is **identifying/detecting** a potential heart disease inflicted person and help them **prevent** it by getting some key information ranging from their food choices to lifetyle.

## Project Description

For this midterm project, a binary classification model was trained on the Heart Disease dataset in order to predict the likelihood of a heart disease using some key indicators.

4 models were trained: a Basic Logistic Rgegression Model, a Decision Tree, a Random Forest and a Gradient Boosting model. Out of the 3, Gradient Boosting was the model with the better performance (using the XGBoost library). The trained model is provided in the file `xgb_model_eta=0.1_max_depth=6_min_child_weight=1.bin`, which can be loaded with pickle.

The exploratory data analysis and model selection was done with the help of a Jupyter Notebook, `notebook.ipynb`.

The model training script was exported to `train.py`.

A Flask app was created in `predict.py`, which can be deployed with any WSGI server. This project has been developed and tested with Gunicorn.

## Files

- README.md: the file you're reading right now.
- heart_2020_cleaned.csv: the CSV file containing the Speed Dating dataset.
- notebook.ipynb: a Jupyter Notebook containing all of the Exploratory Data Analysis and model building.
- train.py: a training script. It will train the best model found on notebook.ipynb and store one file: `xgb_model_eta=0.1_max_depth=6_min_child_weight=1.bin` This file is already provided in this repo; running `train.py` should overwrite the file with new but identical ones, due to the code defining a seed for its random state.
- predict.py: Flask app that receives a query and outputs a prediction.

## How to get Started Using this Model

TBC