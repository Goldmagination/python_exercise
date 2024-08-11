from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth
from config import Config

# orm part
db = SQLAlchemy()

# auth part
auth = HTTPBasicAuth()

# migrations to handle db tables
migrate = Migrate()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)


    # register blueprints
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #testing because the app didn't detect the routes
    with app.app_context():
        print("Registered routes:")
        for rule in app.url_map.iter_rules():
            print(rule)


    return app
