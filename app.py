from flask import Flask
from config import Config
from extensions import db, login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Import blueprints inside the factory function to avoid circular imports
    from routes.auth import auth_bp
    from routes.products import products_bp
    from routes.cart import cart_bp
    from routes.reviews import reviews_bp
    from routes.admin import admin_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')  # Admin blueprint with prefix

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
