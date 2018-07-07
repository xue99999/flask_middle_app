from flask import Blueprint, render_template
from flask_middle_app.models import Course, User

user = Blueprint('user', __name__, url_prefix='/user/<username>')


@user.route('/')
def admin_index(username):
    user = User.query.filter_by(username=username).first()
    courses = Course.query.filter_by(author_id=user.id).all()
    user.courses = courses

    return render_template('user.html', user=user)
