import bentoml

from bentoml.io import JSON

model_ref = bentoml.xgboost.get("heart_disease_risk_model:latest")
model_runner = model_ref.to_runner()
dv = model_ref.custom_objects['dv']

service = bentoml.Service("heart_disease_risk_identifier", runners=[model_runner])

# create the service

@service.api(input=JSON(), output=JSON())
def predict(application_data):
    vector = dv.transform(application_data)

    prediction = model_runner.predict.run(vector)
    result = prediction[0]
    if result > 0.5:
        return {"heart_disease": True, "heart_disease_probability": result}
    else:
        return {"heart_disease": False, "heart_disease_probability": result}