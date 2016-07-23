# -*- coding: utf-8 -*-

import unittest
import requests
import json
from datetime import date, timedelta
from random import randint


class TestUsersService(unittest.TestCase):
    def assertOneUserResponse(self, r):
        try:
            users = json.loads(r.text)
            self.assertIsInstance(users, list)
            self.assertEqual(len(users), 1)
            return users
        except ValueError:
            self.fail()

    def assertMultipleUsersResponse(self, r):
        try:
            users = json.loads(r.text)
            self.assertIsInstance(users, list)
        except ValueError:
            self.fail()

    def test_list(self):
        r = requests.request('GET', 'http://localhost:5000/users/list')
        self.assertMultipleUsersResponse(r)

    def test_list_get_one(self):
        r = requests.request('GET', 'http://localhost:5000/users/list', params={'id': 1})
        self.assertOneUserResponse(r)

    def test_save_new(self):
        user = {
            'name': u'Николаев (test) %d' % randint(1, 1000000),
            'birthdate': date(1980, 1, 1) + timedelta(days=randint(-10000, 3650)),
            'account_value': 10000 + randint(-5000, 5000),
            'state': randint(1, 3),
            'address': u'Moscow',
            'hire_date': date(2016, 7, 20) + timedelta(days=randint(-100, 100)),
        }
        r = requests.request('POST', 'http://localhost:5000/users/save', data=user)
        self.assertOneUserResponse(r)

    def test_save_edit(self):
        user = {
            'id': 1,
            'name': u'Иванов (test) %d' % randint(1, 1000000),
            'birthdate': date(1980, 1, 1) + timedelta(days=randint(-10000, 3650)),
            'account_value': 10000 + randint(-5000, 5000),
            'state': randint(1, 3),
            'address': u'Moscow',
            'hire_date': date(2016, 7, 20) + timedelta(days=randint(-100, 100)),
        }
        r = requests.request('POST', 'http://localhost:5000/users/save', data=user)

        users = self.assertOneUserResponse(r)
        self.assertEqual(user['name'], users[0]['name'])

    def test_counter(self):
        r = requests.request('GET', 'http://localhost:5000/count', data='hire_date')
        try:
            result = json.loads(r.text)
            self.assertIsInstance(result, dict)
        except ValueError:
            self.fail()

if __name__ == '__main__':
    unittest.main()
