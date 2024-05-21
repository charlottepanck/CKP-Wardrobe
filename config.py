import os

class Config:
    SECRET_KEY = 'your_secret_key'
    DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'site.db')
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/images')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit file size to 16MB