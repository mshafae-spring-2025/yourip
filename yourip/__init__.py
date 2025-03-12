
import logging
from os import makedirs
import sys
from flask import Flask

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
handler.setFormatter(formatter)
logger.addHandler(handler)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        makedirs(app.instance_path)
    except OSError as excpt:
        logger.info(f"Instance dir already exists, {excpt}.")
    
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import show
    app.register_blueprint(show.bp)
    
    return app
