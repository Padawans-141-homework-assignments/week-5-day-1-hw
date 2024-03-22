from flask_smorest import Blueprint

bpygo = Blueprint('ygo', 'ygo', description='Holds card information')

from . import ygo_res