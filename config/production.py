from config.default import *


SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY =b'w \x95;\xe2\x0b0\xc8 \xe2\xa8\x0c<!\xfbU'

