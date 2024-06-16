import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Lib_Key'
    DATABASE_NAME = os.environ.get('DATABASE_NAME') or 'Literary_Loft'
    DATABASE_USER = os.environ.get('DATABASE_USER') or 'Lib_mang_user'
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD') or 'Lib_Key'
    DATABASE_HOST = os.environ.get('DATABASE_HOST') or 'localhost'
    DATABASE_PORT = os.environ.get('DATABASE_PORT') or '5432'
