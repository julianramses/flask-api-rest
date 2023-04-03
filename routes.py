from app import app, db
from .models import InstitutionModel
from flask import jsonify, request, render_template



@app.route('/institutions', methods=['POST'])
def create_institution():
    name = request.json.get('name')
    description = request.json.get('description')
    address = request.json.get('address')
    creation_date = request.json.get('creation_date')

    new_institution = InstitutionModel(name=name, description=description, address=address, creation_date=creation_date)

    db.session.add(new_institution)
    db.session.commit()

    return jsonify({'message': 'Institucion creada correctamente'})


@app.route('/institutions', methods=['GET'])
def read_institutions():
    institutions = InstitutionModel.query.all()

    return jsonify([{'id': i.id, 'name': i.name, 'description': i.description, 'address': i.address, 'creation_date': i.creation_date} for i in institutions])


@app.route('/institutions/<int:id>', methods=['PUT'])
def update_institution(id):
    institution = InstitutionModel.query.get(id)

    if not institution:
        return jsonify({'message': 'Institucion no encontrada'})

    name = request.json.get('name')
    description = request.json.get('description')
    address = request.json.get('address')
    creation_date = request.json.get('creation_date')

    institution.name = name
    institution.description = description
    institution.address = address
    institution.creation_date = creation_date

    db.session.commit()

    return jsonify({'message': 'Institucion actualizada'})


@app.route('/institutions/<int:id>', methods=['DELETE'])
def delete_institution(id):
    institution = InstitutionModel.query.get(id)

    if not institution:
        return jsonify({'message': 'Instituticion no encontrada'})

    db.session.delete(institution)
    db.session.commit()

    return jsonify({'message': 'Institucion eliminada'})


@app.route('/institutions/all')
def list_all_institutions():
    institutions = InstitutionModel.query.all()
    institutions_list = []

    for institution in institutions:
        address = institution.address.replace(" ", "+") #la url usa + para los espacios o %20
        google_maps_url = f"https://www.google.com/maps/search/{address}"
        abbreviation = institution.name[:3] #la abreviacion usando :3 de python que limita los 3 primeros caracteres

        institutions_list.append({
            'id': institution.id,
            'name': institution.name,
            'abbreviation': abbreviation,
            'address': institution.address,
            'google_maps_url': google_maps_url
        })

    return jsonify({'institutions': institutions_list})
