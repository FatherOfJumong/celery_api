
from flask import request, jsonify
from flask_restx import Resource
from .src import oracle_config
from .src import OracleConnection
import sys
from risk_models_api.model.tasks import task_1, task_2
import pandas as pd

from . import (
    api
)


oracle = OracleConnection(oracle_config)


@api.route('/api/cns/<cns_version>')
class TestClass(Resource):
    def get(self, cns_version):
        result1 = task_1.apply_async(args=["Task 1"]).get()
        result2 = task_2.apply_async(args=["Task 2"]).get()
        
        df1 = pd.DataFrame(result1)
        df2 = pd.DataFrame(result2)

        # Assuming result1 and result2 are already DataFrames:
        unified_df = pd.concat([df1, df2])  

        length = len(unified_df) 

        return jsonify({"length": length, 
                        "status": "Task completed successfully"})