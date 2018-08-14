import unittest
import json


from test.base import BaseTestCase

def register_user(self):
    return self.client.post(
        '/api/user',
        data = json.dumps(dict(
            username = 'test',
            email = 'test@test.com',
            password = 'testpassword'
        )),
        content_type = 'application/json'
    )

def register_user_with_no_data(self):
    return self.client.post(
        '/api/user',
        data = json.dumps(dict(
            ''
        )),
        content_type = 'application/json'
    )

def login_user(self):
    return self.client.post(
        '/api/auth/login',
        data = json.dumps(dict(
            email = 'test@test.com',
            password = 'testpasssword'
        )),
        content_type = 'application/json'
    )

def login_user_with_no_data(self):
    return self.client.post(
        '/api/auth/login',
        data = json.dumps(dict(
            ''
        )),
        content_type = 'application/json'
    )

def login_user_with_non_exists_user(self):
    return self.client.post(
        '/api/auth/login',
        data = json.dumps(dict(
            email = 'no_user@no_user.com',
            password = 'nopassword'
        )),
        content_type = 'application/json'
    )

class TestAuthBlueprint(BaseTestCase):
    def test_register_user(self):
        """ Test register user"""
        with self.client:
            response = register_user(self)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data['status'] == "OK")
            self.assertTrue(data['message'] == "Success register")

    def test_register_user_with_no_data(self):
        """ Test register user with no data """
        with self.client:
            response = register_user_with_no_data(self)
            self.assertEqual(response.status_code, 400)
    
    def test_register_user_already_exist(self):
        """ Test register user with exist user """
        with self.client:
            response = register_user(self)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data['status'] == "ERROR")
            self.assertTrue(data['message'] == "User already exists")
    
    def test_registered_user_login(self):
        """ Test login user with correct password"""
        with self.client:
            response = login_user(self)
            data = json.loads(response.data.decode())
            expected_dict = ["status", "message", "token"]
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data['status'] == "OK")
            self.assertTrue(data['message'] == "Success Login")
            self.assertListEqual(expected_dict, data.keys())
    
    def test_login_user_with_no_data(self):
        """ Test login user with no data """
        with self.client:
            response = login_user_with_no_data(self)
            self.assertEqual(response.status_code, 400)
    
    def test_login_user_not_exists(self):
        """ Test login user not exists """
        with self.client:
            response = login_user_with_non_exists_user(self)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data['status'] == "ERROR")
            self.assertTrue(data['message'] == "User not exists")
            

if __name__ == '__main__':
    unittest.main()