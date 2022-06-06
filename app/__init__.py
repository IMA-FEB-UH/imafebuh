from flask import Flask

app = Flask(__name__)
app.secret_key = "nfiwqcuhnf0134751f08y192837cd4n"

# Import MainViews dari folder projects
from app.projects import MainViews
