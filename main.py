from user import app
from user.db.model import db

# choosing environment profile
if app.config['ENV'] == "production":
    app.config.from_object("config.ProductionConfig")
    db.create_all()

elif app.config['ENV'] == "development":
    app.config.from_object("config.DevelopmentConfig")
    db.create_all()

elif app.config["ENV"] == "testing":
    app.config.from_object("config.DevelopmentConfig")
    db.create_all()
