from .. import db


class comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(50), nullable=False)
    contents = db.Column(db.String(500), nullable=False)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    user_email = db.Column(db.ForeignKey('user.email'), nullable=False)

    def __init__(self, board_id, contents, author, user_email):
        self.board_id = board_id
        self.contents = contents
        self.author = author
        self.user_email = user_email

    def update_contents(self, contents):
        self.contents = contents

    def __repr__(self):
        return '<id: {}>'.format(self.id)
