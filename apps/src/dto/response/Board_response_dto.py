from flask_restx import Namespace


class board_response_dto:
    api = Namespace('/board')

    def read_list(board_list_obj):
        response_list = []
        for board in board_list_obj:
            response_list.append({
                'id': board.id,
                'title': board.title,
                'author': board.author
            }
            )
        return response_list

    def read_detail_dto(read_object):
        comment_list = []
        for comment in read_object.comments:
            comment_list.append({
                'id': comment.id,
                'contents': comment.contents,
                'author': comment.author
            })

        return {
            'id': read_object.id,
            'title': read_object.title,
            'author': read_object.author,
            'text': read_object.text,
            'comments': comment_list
        }
