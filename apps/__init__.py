from flask import Blueprint
from flask_restx import Api

from .src import create_app, authorizations
from .src.controller.Board_controller import board_api
from .src.controller.Comment_controller import comment_api
from .src.controller.Index_controller import index_api
from .src.controller.User_controller import user_api

app = create_app()

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

blueprintIndex = index_api

api = Api(blueprint, security='Bearer Auth', authorizations=authorizations)

api.add_namespace(board_api, '/board')
api.add_namespace(user_api, '/user')
api.add_namespace(comment_api, '/comment')
