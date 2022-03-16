from flask import session, jsonify, Response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from apps.src.dto.response.User_response_dto import user_response_dto
from apps.src.models.User import user
from .. import db


class user_service:

    def signup_user_service(user_signup_dto):
        user_signup_dto.set_password(user_signup_dto.password)
        db.session.add(user_signup_dto)
        db.session.commit()
        User = db.session.query(user).get(user_signup_dto.id)
        return User.id

    def login_user_service(user_login_dto):
        try:
            User = db.session.query(user).filter(
                user.email == user_login_dto['email']).first()
            if User.check_password(user_login_dto['password']):
                User.update_role('user')
                session['username'] = User.email
                db.session.commit()
                return jsonify(
                    access_token='Bearer ' + create_access_token(identity=User.email,
                                                                 expires_delta=False)
                )
            return Response(
                'wrong password info',
                status=400
            )
        except Exception as e:
            return Response(
                'wrong user info',
                status=400
            )

    @jwt_required()
    def read_user_info(password):
        '''my-page'''
        user_auth_val = get_jwt_identity()
        if user_auth_val is not None:
            User = db.session.query(user).filter(user.email == user_auth_val).first()
            if User.check_password(password):
                return user_response_dto.read_user_info(User)
            return jsonify(
                "wrong user info",
                status=400
            )
        return Response(
            "user is not auth",
            status=403
        )
