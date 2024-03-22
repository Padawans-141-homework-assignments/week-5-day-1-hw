from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.gen_model import gen_Model
from models.ygo_model import ygo_Model

from resources.gen import bpgen as gen_bp
app.register_blueprint(gen_bp)
from resources.ygo import bpygo as ygo_bp
app.register_blueprint(ygo_bp)