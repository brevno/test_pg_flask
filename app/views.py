# -*- coding: utf-8 -*-

from app import app, db
from app.models import User
from flask import jsonify, request, abort


@app.route('/users/list')
def users_list():
    if 'id' in request.args:
        user = User.query.get_or_404(request.args['id'])
        return jsonify([user.as_dict()])
    else:
        return jsonify(map(User.as_dict, User.query.all()))


@app.route('/users/save', methods=['POST'])
def save_user():
    if 'id' in request.form:
        user = User.query.get_or_404(request.form['id'])
        form_dict = request.form.to_dict()
        for key in form_dict:
            setattr(user, key, form_dict[key])
    else:
        user = User(**request.form.to_dict())
    db.session.add(user)
    db.session.commit()
    return jsonify([user.as_dict()])


@app.route('/count')
def get_count():
    if request.data not in ['state', 'hire_date']:
        abort(404)
    grouping_field = getattr(User, request.data)
    res = User.query.with_entities(grouping_field, db.func.count(User.id)).group_by(grouping_field).all()
    return jsonify({str(group_value): cnt for (group_value, cnt) in res})
