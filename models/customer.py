from sqlalchemy import Column, String, Boolean, Numeric, Date, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime as dt

from services.formater import DATETIME_DATE_FORMAT, EARLIEST_GOOD_FORMAT_DATE

Base = declarative_base()


class Customer(Base):
    __tablename__ = "Customer"

    dni = Column(String, primary_key=True, name="dni")
    name = Column(String, name="nombre")
    surname1 = Column(String, name="apellido1")
    surname2 = Column(String, name="apellido2")
    birthdate = Column(Date, name="fecha_nacimiento")
    phone = Column(String, name="telefono")
    email = Column(String, name="email")
    street = Column(String, name="calle")
    portal = Column(String, name="portal")
    door = Column(String, name="puerta")
    cp = Column(Integer, name="CP")
    city = Column(String, name="ciudad")
    iban = Column(String, name="IBAN")
    register_date = Column(Date, name="alta")
    drop_date = Column(Date, name="baja", default=dt.strptime(EARLIEST_GOOD_FORMAT_DATE, DATETIME_DATE_FORMAT))
    quota = Column(Numeric, name="cuota")
    active = Column(Boolean, name="activo")

    def to_update_dict(self):
        return {"nombre": self.name, "apellido1": self.surname1, "apellido2": self.surname2,
                "fecha_nacimiento": self.birthdate, "telefono": self.phone, "email": self.email, "calle": self.street,
                "portal": self.portal, "puerta": self.door, "cp": self.cp, "ciudad": self.city, "IBAN": self.iban,
                "alta": self.register_date, "baja": self.drop_date, "cuota": self.quota, "activo": self.active}

    @staticmethod
    def create_empty_customer():
        return Customer(dni="", name="", surname1="", surname2="",
                        birthdate=dt.strptime(dt.today().strftime(DATETIME_DATE_FORMAT), DATETIME_DATE_FORMAT), phone="", email="",
                        street="", portal="", door="", cp="", city="", iban="",
                        register_date=dt.strptime(dt.today().strftime(DATETIME_DATE_FORMAT), DATETIME_DATE_FORMAT),
                        drop_date=dt.strptime(dt.today().strftime(DATETIME_DATE_FORMAT), DATETIME_DATE_FORMAT),
                        quota=0.0, active=True)
