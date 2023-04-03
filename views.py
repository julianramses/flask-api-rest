from flask import jsonify
from models import InstitutionModel, ProjectModel, UserModel
from datetime import datetime
from app import app

@app.route('/institutions')
def list_institutions():
    institutions = InstitutionModel.query.all()
    return render_template('institutions.html')
app.run(host='localhost', port=5000)

@app.route('/projects', methods=['GET'])
def get_projects():
    projects = ProjectModel.query.all()
    return jsonify([p.serialize() for p in projects])

@app.route('/users', methods=['GET'])
def get_users():
    users = UserModel.query.all()
    return jsonify([u.serialize() for u in users])

@app.route('/projectsdaysleft', methods=['GET'])
def list_projects_with_days_left():
    projects = ProjectModel.query.all()
    today = datetime.today()

    results = []
    for project in projects:
        days_left = (project.due_date - today).days
        results.append({
            'name': project.name,
            'days_left': days_left
        })

    return jsonify(results)