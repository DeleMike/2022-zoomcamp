import pickle

from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model2.bin'
dv_file = "dv.bin"
print('loading model and dv...')

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in2:
    dv = pickle.load(f_in2)

print('Loaded model: ', (dv, model))

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()
     
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0,1]
    default = y_pred >=0.5

    result = {
        'default_probability':float(y_pred),
        'default':bool(default)
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
