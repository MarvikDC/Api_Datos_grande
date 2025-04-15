# models.py

from database import db

class Empresa(db.Model):
    __tablename__ = 'empresas'

    ruc = db.Column('ruc', db.String, primary_key=True)
    estado = db.Column('estado', db.String)
    condicion = db.Column('condicion', db.String)
    tipo = db.Column('tipo', db.String)
    actividad_economica_ciiu_revision3_principal = db.Column('actividad_economica_ciiu_revision3_principal', db.String)
    actividad_economica_ciiu_revision3_secundaria = db.Column('actividad_economica_ciiu_revision3_secundaria', db.String)
    actividad_economica_ciiu_revision4_principal = db.Column('actividad_economica_ciiu_revision4_principal', db.String)
    nrotrab = db.Column('nrotrab', db.String)
    tipofacturacion = db.Column('tipofacturacion', db.String)
    tipocontabilidad = db.Column('tipocontabilidad', db.String)
    comercioexterior = db.Column('comercioexterior', db.String)
    ubigeo = db.Column('ubigeo', db.String)
    departamento = db.Column('departamento', db.String)
    provincia = db.Column('provincia', db.String)
    distrito = db.Column('distrito', db.String)
    periodo_publicacion = db.Column('periodo_publicacion', db.String)

    def to_dict(self):
        """Convierte el objeto Empresa en un diccionario serializable."""
        return {
            "ruc": self.ruc,
            "estado": self.estado,
            "condicion": self.condicion,
            "tipo": self.tipo,
            "actividad_economica_ciiu_revision3_principal": self.actividad_economica_ciiu_revision3_principal,
            "actividad_economica_ciiu_revision3_secundaria": self.actividad_economica_ciiu_revision3_secundaria,
            "actividad_economica_ciiu_revision4_principal": self.actividad_economica_ciiu_revision4_principal,
            "nrotrab": self.nrotrab,
            "tipofacturacion": self.tipofacturacion,
            "tipocontabilidad": self.tipocontabilidad,
            "comercioexterior": self.comercioexterior,
            "ubigeo": self.ubigeo,
            "departamento": self.departamento,
            "provincia": self.provincia,
            "distrito": self.distrito,
            "periodo_publicacion": self.periodo_publicacion
        }