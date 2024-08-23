from sqlalchemy import create_engine, update
from sqlalchemy.orm import Session
import pandas as pd

from models.customer import Customer


class DB:
    def __init__(self):
        self.engine = create_engine('sqlite:///assets/data/database.db')

    def get_customers(self):
        with self.engine.connect() as conn:
            return pd.read_sql("SELECT * FROM CUSTOMER;", conn)

    def insert_customer(self, customer):
        with Session(self.engine) as session:
            try:
                session.add(customer)
                session.commit()
            except Exception as e:
                print(e)
                return False
        return True

    def update_customer(self, customer):
        stmt = update(Customer).where(Customer.dni.in_([customer.dni])).values(customer.to_update_dict())
        with Session(self.engine) as session:
            try:
                session.execute(stmt)
            except Exception as e:
                print(e)
                return False
        return True
