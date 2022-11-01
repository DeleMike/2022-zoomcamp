import pickle
import xgboost as xgb

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'xgb_model_with_dv_eta=0.1_max_depth=6_min_child_weight=1.bin'
print('loading model and dv...')

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

print('Loaded model: ', (dv, model))

app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    patient = request.get_json()
     
    X = dv.transform([patient])
    dtest = xgb.DMatrix(X, feature_names=dv.get_feature_names_out())
    y_pred = model.predict(dtest)[0]
    default = y_pred >=0.5

    result = {
        'heart_disease_probability':float(y_pred),
        'heart_disease':bool(default)
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
