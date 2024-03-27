from flask_smorest import Blueprint

bpusr = Blueprint('usr', 'usr', description='Holds the info of the user')

from . import login