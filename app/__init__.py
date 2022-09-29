from flask import Flask
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.secret_key = "nfiwqcuhnf0134751f08y192837cd4n"
ckeditor = CKEditor(app)

# Import MainViews dari folder projects
from app.projects import MainViews
