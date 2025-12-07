import unittest
import json
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import app as tested_app

class PasswordCheckerTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_root(self):
        r = self.app.get('/')
        self.assertEqual(r.data, b'Password Checker')

    def test_strong_password(self):
        r = self.app.post('/check', content_type='application/json',
                          data=json.dumps({'password': 'abc12345'}))
        self.assertEqual(r.json, {'status': 'strong'})

    def test_weak_password(self):
        r = self.app.post('/check', content_type='application/json',
                          data=json.dumps({'password': 'short'}))
        self.assertEqual(r.json, {'status': 'weak'})

    def test_bad_input(self):
        r = self.app.post('/check', content_type='application/json', data=json.dumps({}))
        self.assertEqual(r.status_code, 400)
