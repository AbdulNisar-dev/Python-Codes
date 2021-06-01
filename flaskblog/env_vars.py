import os

db_email = os.environ.get('DB_EMAIL')
db_password = os.environ.get('DB_PASSWORD')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
print(db_email)
print(db_password)
print(SECRET_KEY)
print(SQLALCHEMY_DATABASE_URI)