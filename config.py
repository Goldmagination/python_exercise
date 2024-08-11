import os

# In the live app this file should be concealed within .gitignore

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/python_Excercise')
