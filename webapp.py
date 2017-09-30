from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email


app=Flask(__name__)
#Update the username and password of the URL and the databasename
#'postgresql://username:password!@endpointURL:port/databasename'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password!@flaskpythonapp.cwyt1tt0eioi.us-east-1.rds.amazonaws.com:5432/databasename'
db=SQLAlchemy(app)


class Data(db.Model):
    __tablename__="flaskTable"
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(120),unique=True)
    height=db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.email=email_
        self.height=height_

db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/success",methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height"]
        send_email(email,height)
        data=Data(email,height)
        if db.session.query(Data).filter(Data.email==email).count()==0:
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
        return render_template("index.html",text="Email already exists")

if __name__=='__main__':
    app.debug=True
    app.run()