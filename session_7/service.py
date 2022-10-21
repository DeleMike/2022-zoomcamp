import bentoml

from bentoml.io import JSON
from bentoml.io import NumpyNdarray

from pydantic import BaseModel

class CreditApplication(BaseModel):
    seniority:int
    home:str
    time:int
    age:int
    marital:str
    records: str
    job: str
    expenses: int
    income: float
    assets: float
    debt: float
    amount: int
    price: int

# get a saved model with the saved id
model_ref = bentoml.xgboost.get("credit_risk_model:vhfpklsrik7veico")
dv = model_ref.custom_objects['dict_vectorizer']

# run the model
model_runner = model_ref.to_runner()

service = bentoml.Service("credit_risk_classifier", runners=[model_runner])

# create the service

@service.api(input=JSON(pydantic_model=CreditApplication), output=JSON())
async def classify(credit_application):
    application_data = credit_application.dict()
    vector = dv.transform(application_data)

    prediction = await model_runner.predict.async_run(vector)
    result = prediction[0]
    if result > 0.5:
        return {"status":  "Declined","prediction": result}
    else:
        return {"status":  "Approved","prediction": result}

 
