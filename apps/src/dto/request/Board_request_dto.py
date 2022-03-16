from flask_restx import fields, Namespace

from apps.src.models.Board import board


class board_request_dto:
    api = Namespace('board')

    registration_dto = api.model('/board', {
        'title': fields.String(),
        'text': fields.String()}
                                 )

    update_dto = api.model('/board/<int:boardId>', {
        'title': fields.String(),
        'text': fields.String()}

                           )

    def dto_to_model(self):
        return board(
            self['title'],
            self['author'],
            self['text'],
            self['user_email'],
        )
