# -*- coding: utf-8 -*-

from app import app, db
from datetime import datetime
from flask_sqlalchemy import inspect


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    birthdate = db.Column(db.DateTime)
    account_value = db.Column(db.Float)
    state = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    hire_date = db.Column(db.DateTime, default=datetime.now, index=True)

    __table_args__ = (
        db.CheckConstraint('state <= 3 and state > 0', name='state_constraint'),
    )

    def as_dict(self):
        mapper = inspect(self)
        return {col.key: getattr(self, col.key) for col in mapper.attrs}
