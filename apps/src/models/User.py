from flask_login import UserMixin

from .. import db, bcrypt


def load_user(email):
    User = user.query.get(email)
    return User


class user(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    nickname = db.Column(db.String(16), nullable=False)
    name = db.Column(db.String(16), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    boards = db.relationship('board', backref='user', lazy=True)
    comments = db.relationship('comment', backref='user', lazy=True)

    def __init__(self, email, password, nickname, name, role):
        self.email = email
        self.password = password
        self.nickname = nickname
        self.name = name
        self.role = role

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def update_role(self, role):
        self.role = role

    def __repr__(self):
        return '<id: {}>'.format(self.id)
