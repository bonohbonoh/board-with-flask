from apps.src.models.Comment import comment
from apps.src.models.User import user
from apps.src.dto.request.Comment_request_dto import comment_request_dto
from flask import session
from .. import db


class comment_service:

    def registration_comment_service(self):
        try:
            if session['username'] is not None:
                User = db.session.query(user).filter(
                    user.email == session['username']).first()
                self['author'] = User.nickname
                self['user_email'] = User.email
        except Exception as e:
            self['author'] = 'Guest'
            self['user_email'] = 'Guest'
        registration = comment_request_dto.dto_to_model(self)
        db.session.add(registration)
        db.session.commit()
        registration_comment = db.session.query(comment).get(registration.id)
        return registration_comment.id

    def update_comment_service(self, comment_id):
        update_comment = db.session.query(comment).get(comment_id)
        update_comment.update_contents(self['contents'])
        db.session.commit()
        return comment_id

    def delete_comment_service(self, comment_id):
        delete_comment = db.session.query(comment).get(comment_id)
        db.session.delete(delete_comment)
        db.session.commit()
