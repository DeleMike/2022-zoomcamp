import bentoml

from bentoml.io import JSON
from bentoml.io import NumpyNdarray

from pydantic import BaseModel

class UserProfile(BaseModel):
   name: str
   age: int
   country: str
   rating: float

model_ref = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5")

# run the model
model_runner = model_ref.to_runner()

service = bentoml.Service("mlzoomcamp_homework", runners=[model_runner])

# create the service

@service.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(vector):
    #application_data = credit_application.dict()

   # prediction = await model_runner.predict.async_run(application_data)
     prediction =  model_runner.predict.run(vector)

     return prediction
   #  result = prediction[0]
   #  if result > 0.5:
   #      return {"status":  "Declined","prediction": result}
   #  else:
   #      return {"status":  "Approved","prediction": result}
