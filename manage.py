import os
import coverage
import unittest

from flask import current_app

from flask_script import Manager
from pymongo import MongoClient

from app import create_app, mongo

app = create_app()
app.app_context().push()

manager = Manager(app)



@manager.command
def run():
    app.config.from_object('app.config.DevelopmentConfig')
    mongo.init_app(app)
    app.run()


@manager.command
def test():
    """ Runs the unit tests."""
    app.config.from_object('app.config.TestingConfig')
    mongo.init_app(app)
    COV = coverage.coverage(branch=True, include='app/api/*')
    COV.start()
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        COV.html_report()
    client = MongoClient(current_app.config['MONGO_URI'])
    client.drop_database('test_unittest')
    if result.wasSuccessful():
        return 0
    return 1




if __name__ == '__main__':
    manager.run()

