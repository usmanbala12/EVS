import os
from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_session import Session
from models import *


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


#keeping a list logged voters
voted_list = []
        

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        matric_no = request.form.get("matric_no")
        phone = request.form.get("phone_no")
        password = request.form.get("password")
        phone_no = int(phone)

        voter = Voters(matric_no=matric_no, phone_no=phone_no, password=password)
        db.session.add(voter)
        db.session.commit()
        return redirect(url_for('vote'))

    else:
        return render_template("register.html")


@app.route("/addCandidates", methods = ["POST", "GET"])
def addCandidates():
    if request.method == "POST":
        name = request.form.get("name")
        matric_no = request.form.get("matric_no")
        aspiring_office = request.form.get("aspiring_office")

        check_candidate = Candidates.query.filter_by(matric_no=matric_no).count()
        if check_candidate > 0:
            flash('the matriculation number you added is not available, please re-enter the information', 'warning')
            return redirect(url_for("addCandidates"))
        else:       
            candidate = Candidates(name=name, matric_no=matric_no, aspiring_office=aspiring_office, vote_count=0)
            db.session.add(candidate)
            db.session.commit()

        return redirect(url_for("addCandidates"))
    else:
        return render_template("addCandidates.html")

@app.route("/vote", methods=["POST", "GET"])
def vote():
    if request.method == "POST":
        choice_president = int(request.form.get("choice_president"))
        choice_vp = int(request.form.get("choice_vp"))
        choice_treasurer = int(request.form.get("choice_treasurer"))
        choice_advisor = int(request.form.get("choice_advisor"))

        vote_president = Candidates.query.get(choice_president)
        vote_president.vote_count += 1

        vote_vp = Candidates.query.get(choice_vp)
        vote_vp.vote_count += 1
        
        vote_treasurer = Candidates.query.get(choice_treasurer)
        vote_treasurer.vote_count += 1

        vote_advisor = Candidates.query.get(choice_advisor)
        vote_advisor.vote_count += 1
        db.session.commit()

        return render_template("success.html")
    else:
        president = Candidates.query.filter_by(aspiring_office=" president").all()
        vice_president = Candidates.query.filter_by(aspiring_office=" vice president").all()
        treasurer = Candidates.query.filter_by(aspiring_office=" treasurer").all()
        advisor = Candidates.query.filter_by(aspiring_office=" advisor").all()

        return render_template("vote.html", president=president, vice_president=vice_president, treasurer=treasurer, advisor=advisor)








    
