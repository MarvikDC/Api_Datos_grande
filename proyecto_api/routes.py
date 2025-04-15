# routes.py

from flask import Blueprint, request, jsonify
from models import Empresa
from database import db
from utils import paginate_query, validate_ruc_exists

api_bp = Blueprint('api', __name__)

# 1. Consulta por RUC (único registro)
@api_bp.route('/empresa/<string:ruc>', methods=['GET'])
def get_empresa_by_ruc(ruc):
    empresa = Empresa.query.filter_by(ruc=ruc).first()
    if empresa:
        return jsonify(empresa.to_dict()), 200  # Usa el método to_dict
    return jsonify({"message": "Empresa no encontrada"}), 404

# 2. Consulta de Departamentos (valores únicos)
@api_bp.route('/departamentos', methods=['GET'])
def get_departamentos():
    departamentos = db.session.query(Empresa.departamento).distinct().all()
    return jsonify([d[0] for d in departamentos]), 200

# 3. Consulta de Provincias (valores únicos)
@api_bp.route('/provincias', methods=['GET'])
def get_provincias():
    provincias = db.session.query(Empresa.provincia).distinct().all()
    return jsonify([p[0] for p in provincias]), 200

# 4. Consulta de Distritos (valores únicos)
@api_bp.route('/distritos', methods=['GET'])
def get_distritos():
    distritos = db.session.query(Empresa.distrito).distinct().all()
    return jsonify([d[0] for d in distritos]), 200

# 5. Consulta por Departamento y Distrito
@api_bp.route('/departamento-distrito/<string:departamento>/<string:distrito>', methods=['GET'])
def get_empresas_by_departamento_distrito(departamento, distrito):
    cursor = request.args.get('cursor')
    empresas = Empresa.query.filter_by(departamento=departamento, distrito=distrito)
    paginated = paginate_query(empresas, cursor)
    return jsonify([e.to_dict() for e in paginated]), 200  # Usa el método to_dict

# 6. Consulta por Departamento (todos los registros)
@api_bp.route('/departamento/<string:departamento>', methods=['GET'])
def get_empresas_by_departamento(departamento):
    cursor = request.args.get('cursor')
    empresas = Empresa.query.filter_by(departamento=departamento)
    paginated = paginate_query(empresas, cursor)
    return jsonify([e.to_dict() for e in paginated]), 200  # Usa el método to_dict

# 7. Consulta por Provincia (todos los registros)
@api_bp.route('/provincia/<string:provincia>', methods=['GET'])
def get_empresas_by_provincia(provincia):
    cursor = request.args.get('cursor')
    empresas = Empresa.query.filter_by(provincia=provincia)
    paginated = paginate_query(empresas, cursor)
    return jsonify([e.to_dict() for e in paginated]), 200  # Usa el método to_dict

# 8. Consulta por Distrito (todos los registros)
@api_bp.route('/distrito/<string:distrito>', methods=['GET'])
def get_empresas_by_distrito(distrito):
    cursor = request.args.get('cursor')
    empresas = Empresa.query.filter_by(distrito=distrito)
    paginated = paginate_query(empresas, cursor)
    return jsonify([e.to_dict() for e in paginated]), 200  # Usa el método to_dict

# 9. Consulta por Departamento y Provincia (todos los registros)
@api_bp.route('/departamento-provincia/<string:departamento>/<string:provincia>', methods=['GET'])
def get_empresas_by_departamento_provincia(departamento, provincia):
    cursor = request.args.get('cursor')
    empresas = Empresa.query.filter_by(departamento=departamento, provincia=provincia)
    paginated = paginate_query(empresas, cursor)
    return jsonify([e.to_dict() for e in paginated]), 200  # Usa el método to_dict

# 10. Consulta por Departamento, Provincia y Distrito (todos los registros)
@api_bp.route('/departamento-provincia-distrito/<string:departamento>/<string:provincia>/<string:distrito>', methods=['GET'])
def get_empresas_by_departamento_provincia_distrito(departamento, provincia, distrito):
    cursor = request.args.get('cursor')
    empresas = Empresa.query.filter_by(departamento=departamento, provincia=provincia, distrito=distrito)
    paginated = paginate_query(empresas, cursor)
    return jsonify([e.to_dict() for e in paginated]), 200  # Usa el método to_dict

# 11. Edición de un registro por RUC
@api_bp.route('/editar-empresa/<string:ruc>', methods=['PUT'])
def update_empresa(ruc):
    empresa = Empresa.query.filter_by(ruc=ruc).first()
    if not empresa:
        return jsonify({"message": "Empresa no encontrada"}), 404
    data = request.json
    for key, value in data.items():
        setattr(empresa, key, value)
    db.session.commit()
    return jsonify({"message": "Empresa actualizada exitosamente"}), 200

# 12. Creación de un nuevo registro
@api_bp.route('/nueva-empresa', methods=['POST'])
def create_empresa():
    data = request.json
    if validate_ruc_exists(data['ruc']):
        return jsonify({"message": "El RUC ya existe"}), 400
    nueva_empresa = Empresa(**data)
    db.session.add(nueva_empresa)
    db.session.commit()
    return jsonify({"message": "Empresa creada exitosamente"}), 201