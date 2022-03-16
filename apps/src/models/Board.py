from .. import db


class board(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    comments = db.relationship('comment', backref='board', lazy=True)
    user_email = db.Column(db.ForeignKey('user.email'), nullable=False)

    def __init__(self, title, author, text, user_email):
        self.title = title
        self.author = author
        self.text = text
        self.user_email = user_email

    def update_title(self, title):
        self.title = title

    def update_text(self, text):
        self.text = text

    def __repr__(self):
        return '<id: {}>'.format(self.id)
