from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask:Gerrard12!@flaskpythonapp.cwyt1tt0eioi.us-east-1.rds.amazonaws.com:5432/flaskdb'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(120),unique=True)
    height=db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.email=email_
        self.height=height_

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/success",methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height"]

    return render_template("success.html")

if __name__=='__main__':
    app.debug=True
    app.run()