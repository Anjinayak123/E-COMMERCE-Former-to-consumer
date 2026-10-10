import os
import sqlite3
from werkzeug.security import generate_password_hash
import getpass

def run_setup():
    from app import app, db
    from models import User

    with app.app_context():
        # Create tables
        db.create_all()
        print("✅ Tables created (if they didn't exist).")

        # Database info
        db_path = app.config['SQLALCHEMY_DATABASE_URI']
        print(f"✅ Database URI: {db_path}")

        # Verify tables
        if "sqlite" in db_path:
            db_file = db_path.replace("sqlite:///", "")
            if os.path.exists(db_file):
                conn = sqlite3.connect(db_file)
                cur = conn.cursor()
                cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cur.fetchall()
                print(f"📂 Tables in database: {tables}")
                conn.close()
            else:
                print("⚠️ Database file not found:", db_file)

        # Admin user setup
        admin = User.query.filter_by(username='admin').first()
        print("⚡ Admin setup")
        email = input("Admin email: ").strip()
        while True:
            password = getpass.getpass("Admin password: ").strip()
            password_confirm = getpass.getpass("Confirm password: ").strip()
            if password == password_confirm and password != "":
                break
            print("❌ Passwords do not match or empty. Try again.")

        if not admin:
            # Create new admin
            admin = User(
                username="admin",
                email=email,
                password_hash=generate_password_hash(password),
                is_admin=True
            )
            db.session.add(admin)
            print("✅ Admin user created.")
        else:
            # Update existing admin password/email
            admin.email = email
            admin.password_hash = generate_password_hash(password)
            print("✅ Admin user updated with new password.")

        db.session.commit()

if __name__ == "__main__":
    run_setup()
