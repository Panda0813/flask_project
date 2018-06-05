import pymysql
class Config():
    DEBUG = True
    SECRET_KEY ='dsger8q43trij532'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@10.35.163.30:3306/modelflask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False