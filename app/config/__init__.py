class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'INffmZH~4?8Z^^,B/`$JtKv6)$2i+|'


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    # MONGO_URI = 'mongodb://myUserAdmin:abc123@35.231.166.198'
    MONGO_URI = 'mongodb://localhost:27017/test_flask'



class TestingConfig(Config):
    TESTING = True
    MONGO_URI = 'mongodb://localhost:27017/test_unittest'