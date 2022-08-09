class Default(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:**@124.221.249.48/website?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'asl;nadflkgaasdfasyfgher'   # 这里需要一个非常复杂的密码字符串


class Development(Default):
    ENV = 'development'
    DEBUG = True


class Production(Default):
    ENV = 'production'
    DEBUG = False

