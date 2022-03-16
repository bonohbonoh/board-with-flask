from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

app.config.update(
    JWT_SECRET_KEY="X-AUTH-TOKEN"
)

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

jwt = JWTManager(app)


def create_app():
    app.config['SECRET_KEY'] = 'this is secret'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:00000000@localhost:3306/todo_list'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db_name = 'board.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    bcrypt.init_app(app)
    db.init_app(app)
    db.app = app
    # db.drop_all()
    db.create_all()
    migrate.init_app(app, db)
    return app
