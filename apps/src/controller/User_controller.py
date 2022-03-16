from flask import request, session
from flask_restx import Resource

from apps.src.dto.request.User_request_dto import user_request_dto
from apps.src.service.User_service import user_service

user_api = user_request_dto.api


@user_api.route('/')
class User_signup_controller(Resource):
    user_signup_dto = user_request_dto.signup_dto

    @user_api.expect(user_signup_dto)
    def post(self):
        '''회원가입'''
        sign_up_user = user_request_dto.dto_to_model(request.json)
        return user_service.signup_user_service(sign_up_user)


@user_api.route('/<string:password>')
class User_auth_controller(Resource):

    def get(self, password):
        return user_service.read_user_info(password)


@user_api.route('/login')
class User_login_controller(Resource):
    user_login_dto = user_request_dto.login_dto

    @user_api.expect(user_login_dto)
    def post(self):
        return user_service.login_user_service(request.json)


@user_api.route('/logout')
class UserLogOutController(Resource):
    def post(self):
        session.clear()
