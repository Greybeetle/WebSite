from .config import SQL_CONFIG, SECRET_KEY


class Default(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (SQL_CONFIG['SQL_USER'], SQL_CONFIG['SQL_PASSWORD'], SQL_CONFIG['SQL_IP'], SQL_CONFIG['DATABASE'])
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'asl;nadflkgaasdfasyfgher'   # 这里需要一个非常复杂的密码字符串


class Development(Default):
    ENV = 'development'
    DEBUG = True


class Production(Default):
    ENV = 'production'
    DEBUG = False

