from sqlalchemy import Column, Integer, String

from data.DBManager import Base


class TransactionTRef(Base):
    __tablename__ = "transaction_ref"

    id = Column(Integer, primary_key=True)
    type = Column(String(45), nullable=False)
