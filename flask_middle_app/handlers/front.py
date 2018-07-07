from flask import Blueprint, render_template
from flask_middle_app.models import Course

front = Blueprint('front', __name__)


@front.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)
