from flask import Flask
from extensions import db, migrate  # Import db and migrate from extensions
from routes.hero_routes import hero_routes  # Import the hero_routes blueprint

def create_app():
    app = Flask(__name__)

    # Configure your app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the db and migrate objects
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models after db initialization to avoid circular imports
    with app.app_context():
        from models.hero import Hero
        from models.power import Power
        from models.hero_power import HeroPower

    # Register blueprints
    app.register_blueprint(hero_routes, url_prefix='/api')  # Add a prefix for API routes

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
