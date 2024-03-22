from flask_smorest import Blueprint

bpgen = Blueprint('gen', 'gen', description='Holds console generation info.')

from . import gen_res