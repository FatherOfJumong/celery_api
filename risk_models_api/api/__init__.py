from flask import Blueprint
from flask_restx import Api


api_blueprint = Blueprint('risk_models_api', __name__)
api = Api(api_blueprint)