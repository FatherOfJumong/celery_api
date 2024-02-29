from sys import path
from pathlib import Path
working_directory_path = Path(__file__).parent.absolute()
path.append(str(working_directory_path))

from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'hgqawerfgsdhsredgfsdh'
    app.config['PROPAGATE_EXCEPTIONS'] = True

    from api import api_blueprint
    from api.cns import api as cns_api
    
    app.register_blueprint(api_blueprint)

    return app


application = create_app()