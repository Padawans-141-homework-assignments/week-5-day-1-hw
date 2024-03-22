from flask import Flask
from flask_smorest import Api

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

from resources.gen import bpgen as gen_bp
app.register_blueprint(gen_bp)
from resources.ygo import bpygo as ygo_bp
app.register_blueprint(ygo_bp)