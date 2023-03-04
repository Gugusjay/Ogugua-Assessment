import os

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

def get_config(env):
    if env == 'production':
        return ProductionConfig
    elif env == 'development':
        return DevelopmentConfig
    elif env == 'testing':
        return TestingConfig
    else:
        raise ValueError(f"Invalid environment: {env}")
