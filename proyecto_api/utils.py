# utils.py

from models import Empresa


def paginate_query(query, cursor=None, page_size=100):
    """Paginación basada en cursor."""
    if cursor:
        query = query.filter(Empresa.RUC > cursor)
    return query.limit(page_size).all()

def validate_ruc_exists(ruc):
    """Valida si un RUC ya existe en la base de datos."""
    return Empresa.query.filter_by(RUC=ruc).first() is not None