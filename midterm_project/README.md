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
- train.py: a training script. It will train the best model found on notebook.ipynb and store one file: `xgb_model_with_dv_eta=0.1_max_depth=6_min_child_weight=1.bin` This file is already provided in this repo; running `train.py` should overwrite the file with new but identical ones, due to the code defining a seed for its random state.
- predict.py: Flask app that receives a query and outputs a prediction.
- predict-test.py: Contains test script to test model API service
- service.py: Contains flow to test with BentoML
- requirements.txt: Contains all python modules used for this project
- Dockerfile: a dockerfile for containerizing the Flask app.

## Run the Code

To get started with this project:

1) Install Conda on your platform. Follow [these steps](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#) if you have not installed it before.

2) Create environment
      - Create a new virtual environment with conda `conda create --name test_env python=3.8`

      - activate your environment with `conda activate test_env`

      - cd into the project folder and run `pip install -r requirements.txt`

3) start the prediction server locally
      - Run `predict.py` either directly or with a WSGI server for deployment. Use gunicorn or waitress-serve if you are on a Windows

      - Run this code for quick testing from the terminal: `python predict.py`

      - Run this code on a WSGI server (Gunicorn) from the terminal: `gunicorn --bind 0.0.0.0:9696 predict:app`

      - Run this code on a WSGI server (Waitress-serve) from the terminal: `waitress-serve --listen 0.0.0.0:9696 predict:app`. You can simply do `pip install waitress` to install it in your environment

      - Stop running either of these by typing `CTRL + C` on your keyboard.

4) Test the API
      - open `notebook_test_api.ipynb` and run the code there.
      - open any API testing software like Postman or Thunder Client and put this in the address bar: `http://localhost:9696/predict` and check the notebook for a sample JSON data to pass to the body.

5) After you're done, you may deactivate your virtual environment with: `conda deactivate.`

## Docker

1) [Install Docker](https://docs.docker.com/get-docker/)
2) Build the image.
      - `docker build -t heart-disease .`
3) Run the docker image.
      - `docker run -it --rm -p 9696:9696 heart-disease`
4) Test the service locally.

## AWS Elastic Beanstalk Deployment

Please follow these steps to create a new app and environment in AWS EB Using pipenv shell:

1) [Create](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) an AWS account.

2) Install **awsebcli**: `pipenv install awsebcli`. If you don't have `pipenv` install it by using `pip install pipenv`

3) After installing awsebcli, open **pipenv shell** using `pipenv shell`

4) Now create with docker platform, choose a region and give it a suitable name. Example: `eb init -p docker -r eu-west-1 heart-disease`

5) Run it locally by using: `eb local run --port 9696` (ensure to change docker file to gunicorn if you are not running on a Windows)

6) Create Web Service with: `eb create heart-disease-checker-env`

7) Copy the generated URL, open `predict-test.py` paste the URL in the `host` variable then test the API endpoint by running the script `python predict-test.py`. (change the values as you like to experiment and see different results)

8) Kill Service after usage: `eb terminate heart-disease-checker-env`

9) Enter `exit` to leave subshell in virtual environment.
