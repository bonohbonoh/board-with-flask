from flask_restx import Namespace, fields

from apps.src.models.User import user


class user_request_dto:
    api = Namespace('user')

    signup_dto = api.model('/user', {
        'email': fields.String(),
        'password': fields.String(),
        'nickname': fields.String(),
        'name': fields.String()
    }
                           )

    login_dto = api.model('/login', {
        'email': fields.String(),
        'password': fields.String()
    })

    auth_dto = api.model('/user/<string:password>', {
        'password': fields.String()
    })

    def dto_to_model(sign_up_object):
        sign_up_object['role'] = 'Guest'
        return user(
            sign_up_object['email'],
            sign_up_object['password'],
            sign_up_object['nickname'],
            sign_up_object['name'],
            sign_up_object['role']
        )
