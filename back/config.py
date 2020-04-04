import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # ...
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/CIDBPP".format("cidbpp", os.environ.get("MYSQL_PASSWORD"),
                                                                       os.environ.get('MYSQL_HOSTNAME'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
