from flask import request, jsonify
from flask_restx import Resource
import sys
import pickle
# from risk_models_api.model.tasks import task_1, task_2
import pandas as pd
import threading  # Import threading module

from . import api

# Load the model and data outside of the request handler



# Define a lock for synchronization
predict_lock = threading.Lock()

@api.route('/api/cns/<cns_version>')
class Main(Resource):
    def get(self, cns_version):
        # Acquire the lock before making the prediction
        with predict_lock:
            with open("risk_models_api/calibrated_clf.pkl", "rb") as f:
                clf = pickle.load(f)
            print("Model loaded successfully!")
            data = pd.read_csv("risk_models_api/X_test.csv")
            a = clf.predict(data[0:1])[0]

        return jsonify({"result": f"Model prediction: {a}"})
