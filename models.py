import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Voters(db.Model):
    __tablename__ = "voters"
    id = db.Column(db.Integer, primary_key=True)
    matric_no = db.Column(db.String, nullable=False)
    phone_no = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=False)

class Candidates(db.Model):
    __tablename__ = "candidates"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    matric_no = db.Column(db.String, nullable=False)
    aspiring_office = db.Column(db.String, nullable=False)
    vote_count = db.Column(db.Integer, nullable=False)


