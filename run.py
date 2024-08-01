from app.routes import app
from db import create_db
from app.Models import *


if __name__ == '__main__':
    create_db()
    app.run()
