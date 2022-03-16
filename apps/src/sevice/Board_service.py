from apps.src.dto.response.Board_response_dto import board_response_dto
from apps.src.dto.request.Board_request_dto import board_request_dto
from apps.src.models.Board import board
from apps.src.models.User import user
from apps.src.models.Comment import comment
from flask import session
from .. import db


class board_service:

    def registration_board_service(self):
        try:
            if session['username'] is not None:
                User = db.session.query(user).filter(
                    user.email == session['username']).first()
                self['author'] = User.nickname
                self['user_email'] = User.email
        except Exception as e:
            self['author'] = 'Guest'
            self['user_email'] = 'Guest'
        registration = board_request_dto.dto_to_model(self)
        db.session.add(registration)
        db.session.commit()
        registration_board = db.session.query(board).get(registration.id)
        return registration_board.id

    def read_detail_board_service(self):
        read_board = db.session.query(board).get(self)
        return board_response_dto.read_detail_dto(read_board)

    def read_list_board_service(self):
        board_list = db.session.query(board).all()
        return board_response_dto.read_list(board_list)

    def update_board_service(self, board_id):
        update_board = db.session.query(board).get(board_id)
        if self['text'] != '':
            update_board.update_text(self['text'])
        if self['title'] != '':
            update_board.update_title(self['title'])
        db.session.commit()
        return board_id

    def delete_board_service(self):
        delete_board = db.session.query(board).get(self)
        if delete_board.comments is not None:
            db.session.query(comment).delete()
        db.session.delete(delete_board)
        db.session.commit()
