# -*- coding: utf-8 -*-

from app import db
from app.models import User
from datetime import date

db.drop_all()
db.create_all()
db.session.commit()

users = [
    User(name=u'Иванов',
         birthdate=date(1980, 4, 10),
         account_value=10000,
         state=1,
         address=u'Moscow',
         hire_date=date(2016, 7, 20)),
    User(name=u'Петров',
         birthdate=date(1976, 5, 15),
         account_value=12000,
         state=1,
         address=u'Moscow',
         hire_date=date(2016, 4, 11)),
    User(name=u'Сидоров',
         birthdate=date(1984, 7, 22),
         account_value=14000,
         state=1,
         address=u'Moscow',
         hire_date=date(2016, 3, 2)),
]

db.session.bulk_save_objects(users)
db.session.commit()


print 'Reset DB OK'
