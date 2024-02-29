
from flask import request, jsonify
from flask_restx import Resource
from .src import oracle_config
from .src import OracleConnection
import sys
from risk_models_api.model.tasks import test_task

from . import (
    api
)


oracle = OracleConnection(oracle_config)


@api.route('/api/cns/<cns_version>')
class TestClass(Resource):
    def get(self, cns_version):
        result = test_task.delay(f"CNS data - {cns_version}")  # Trigger the task

        # Assuming you want to return the task ID for tracking
        return jsonify({"cns_version": cns_version, "task_id": result.id})
