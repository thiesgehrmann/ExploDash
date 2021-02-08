"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment


def create_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment()

    with app.app_context():
        # Import Flask routes
        from . import routes

        # Import Dash application
        from application.plotlydash.dashboard import create_dashboard
        app = create_dashboard(app)

        # Compile CSS
        from application.assets import compile_assets
        compile_assets(assets)

        return app
    #ewith
#edef