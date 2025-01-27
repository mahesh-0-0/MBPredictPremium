from flask import Flask, request, jsonify
import os
import pickle
import numpy as np

app = Flask(__name__)

model_path = "final_predict_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict_premium():
    input_data = request.json
    features = np.array([
        input_data['Age'],
        input_data['Diabetes'],
        input_data['BloodPressureProblems'],
        input_data['AnyTransplants'],
        input_data['AnyChronicDiseases'],
        input_data['Height'],
        input_data['Weight'],
        input_data['KnownAllergies'],
        input_data['HistoryOfCancerInFamily'],
        input_data['NumberOfMajorSurgeries'],
        input_data['BMI']
    ]).reshape(1, -1)

    prediction = model.predict(features)[0]
    return jsonify({"PredictedPremium": round(prediction, 2)})

if __name__ == '__main__':
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
