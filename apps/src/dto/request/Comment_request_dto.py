from flask_restx import fields, Namespace

from apps.src.models.Comment import comment


class comment_request_dto:
    api = Namespace('comment')

    registration_dto = api.model('/comment', {
        'board_id': fields.Integer(),
        'contents': fields.String()
    }
                                 )

    update_dto = api.model('/comment/<int:commentId>', {
        'board_id': fields.Integer(),
        'contents': fields.String()
    }
                           )
    delete_dto = api.model('/comment/<int:commentId>', {
        'board_id': fields.Integer()
    }
                           )
    def dto_to_model(self):
        return comment(
            self['board_id'],
            self['contents'],
            self['author'],
            self['user_email']

        )
