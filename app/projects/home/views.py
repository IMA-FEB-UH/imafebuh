from flask import Blueprint, render_template

homeBlueprint = Blueprint('home', __name__, static_folder='staticHome', template_folder='templates')

@homeBlueprint.route('/')
@homeBlueprint.route('/home')
def index():
    return render_template('index.html')

@homeBlueprint.route('/tentang_ima')
def about():
    return render_template('about.html')