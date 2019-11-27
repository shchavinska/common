import os


class Config:
    SECRET_KEY = 'secret_key'
    DEBUG = True


class TestConfig:
    SECRET_KEY = 'test_key'
    TESTING = True


class ProdConfig:
    SECRET_KEY = 'prod_key'


def run_config():
    env = os.environ.get('ENV')
    if env == 'TEST':
        return TestConfig
    elif env == 'PROD':
        return ProdConfig
    else:
        return Config

