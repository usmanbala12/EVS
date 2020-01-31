import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Ghani2001@localhost:5432/testvote"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("candidates.csv")
    reader = csv.reader(f)
    for name, matric_no, aspiring_office, vote_count in reader:
        candidates = Candidates(name=name, matric_no=matric_no, aspiring_office=aspiring_office, vote_count=vote_count)
        db.session.add(candidates)
        print(f"Added a candidate named {name} aspiring for {aspiring_office} with matric_no {matric_no}")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()