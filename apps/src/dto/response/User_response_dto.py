from flask_restx import Namespace


class user_response_dto:
    api = Namespace('/user')

    def read_user_info(read_object):
        board_list = []
        for board in read_object.boards:
            board_list.append({
                'id': board.id,
                'title': board.title,
                'text': board.text,
                'author': board.author,
                'user_email': board.user_email
            })
        comment_list = []
        for comment in read_object.comments:
            comment_list.append({
                'id': comment.id,
                'contents': comment.contents,
                'author': comment.author,
                'board_id': comment.board_id,
                'user_email': comment.user_email
            })
        return {
            'id': read_object.id,
            'email': read_object.email,
            'password': read_object.password,
            'name': read_object.name,
            'nickname': read_object.nickname,
            'boards': board_list,
            'comments': comment_list

        }
