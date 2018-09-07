"""Flask blog app config"""
import os
import os.path as op

here = op.dirname(__file__)

SECRET_KEY = os.getenv('SECRET_KEY', 'flask blog')
DEFAULT_ADMIN_PASSWORD = 'admin'
WTF_CSRF_ENABLED = True

if 'RDS_HOSTNAME' in os.environ:    # AWS environment
    db_name = os.environ['RDS_DB_NAME']
    db_user = os.environ['RDS_USERNAME']
    db_password = os.environ['RDS_PASSWORD']
    db_host = os.environ['RDS_HOSTNAME']
    db_port = os.environ.get('RDS_PORT')
    if db_port:
        SQLALCHEMY_DATABASE_URI = ('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'
                                   .format(db_user, db_password, db_host, db_port,
                                           db_name))
    else:
        SQLALCHEMY_DATABASE_URI = ('mysql+pymysql://{}:{}@{}/{}?charset=utf8'
                                   .format(db_user, db_password, db_host,
                                           db_name))
elif 'DATABASE_URL' in os.environ:     # Heroku environment
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + op.join(here, 'db.sqlite3')

SQLALCHEMY_TRACK_MODIFICATIONS = False
BLOG_PER_PAGE = 10

ENABLE_COS_UPLOAD = True
COS_SECRET_ID = os.getenv('COS_SECRET_ID')
COS_SECRET_KEY = os.getenv('COS_SECRET_KEY')
COS_BUCKET = "frostming-tencent-1252779928"
COS_REGION = "ap-guangzhou"
