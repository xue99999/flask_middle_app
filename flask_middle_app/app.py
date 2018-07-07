from flask import Flask
from flask_middle_app.config import configs
from flask_middle_app.models import db


def create_app(config):
    app = Flask(__name__)

    app.config.from_object(configs.get(config))

    db.init_app(app)
    register_blueprints(app)

    return app

def register_blueprints(app):
    from .handlers import front, course, admin, user
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)
    app.register_blueprint(user)

# create tables
def create_data():
    db.create_all()
    user = User(username='admin')
    course1 = Course(name='python course', author=user)
    course2 = Course(name='flask course', author=user)
    db.session.add(user)
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()

if __name__ == '__main__':
    create_data()
