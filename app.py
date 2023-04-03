from flask import Flask
from flask_restful import Api
from .models import db, InstitutionModel

app = Flask(__name__)
@app.get("/")
def home():
    return "hello, world"

api = Api(app)

if __name__== '__main__':
    ap.run(host='localhost',port=5000)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ofyotcwq:HAnnLiVmGMEHPOilYLM5iqiMAIzgXroF@babar.db.elephantsql.com/ofyotcwq'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()