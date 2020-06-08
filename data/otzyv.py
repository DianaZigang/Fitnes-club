import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Otzyv(SqlAlchemyBase):
    __tablename__ = 'otzyv'


    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    Name = sqlalchemy.Column(sqlalchemy.String)
    Text = sqlalchemy.Column(sqlalchemy.String)
    Data = sqlalchemy.Column(sqlalchemy.Date, default=datetime.datetime.now)
