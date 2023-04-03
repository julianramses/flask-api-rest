from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class InstitutionModel(db.Model):
    __tablename__ = "institutions"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    address = db.Column(db.String(120), nullable=True)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, name, description, address, creation_date):
        self.name = name
        self.description = description
        self.address = address
        self.creation_date = creation_date

    def __repr__(self):
        return f"<Institution {self.name}>"

class ProjectModel(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    start_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)
    institution_id = db.Column(db.Integer, db.ForeignKey("institutions.id"), nullable=False)

    institution = db.relationship("InstitutionModel", backref="projects")

    def __init__(self, name, description, start_date, end_date, institution_id):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.institution_id = institution_id

    def __repr__(self):
        return f"<Project {self.name}>"

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    rut = db.Column(db.String(10), unique=True, nullable=False)
    birth_date = db.Column(db.DateTime, nullable=True)
    job_title = db.Column(db.String(120), nullable=True)

    projects = db.relationship("ProjectModel", backref="user", lazy=True)

    def __init__(self, name, last_name, rut, birth_date, job_title):
        self.name = name
        self.last_name = last_name
        self.rut = rut
        self.birth_date = birth_date
        self.job_title = job_title

    def __repr__(self):
        return f"<User {self.name} {self.last_name}>"

