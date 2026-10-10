from app import create_app
from extensions import db
from models import User

app = create_app()
with app.app_context():
    admin = User.query.filter_by(username='admin').first()
    if admin:
        admin.is_admin = True
        db.session.commit()
        print("Admin user updated with is_admin=True.")
    else:
        # If admin user doesn't exist yet, create it:
        admin = User(username='admin', email='admin@example.com', is_admin=True)
        admin.set_password('admin123')  # Use a strong password!
        db.session.add(admin)
        db.session.commit()
        print("Admin user created.")
