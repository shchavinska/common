import os


class Config:
    SECRET_KEY = 'secret_key'
    PG_USER = 'anastasiia'
    PG_PASSWORD = 'paswoord'
    PG_HOST = 'localhost'
    PG_PORT = 5432
    DB_NAME = 'flask_orm_homework'
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    TEST_VALUE = "DEV_CONFIG_VALUE"


class TestConfig(Config):
    TEST_VALUE = "TEST_CONFIG_VALUE"


def run_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig
    elif env == "TEST":
        return TestConfig
    else:
        return Config
