from app import create_app
from extensions import db
from models import User, Product, Category
from app import create_app
from extensions import db
from models import User
app = create_app()

def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Categories
        c1 = Category(name='Electronics')
        c2 = Category(name='Clothing')
        c3 = Category(name='Books')
        db.session.add_all([c1, c2, c3])
        db.session.commit()

        # Products
        products = [
            Product(
                name='Wireless Headphones',
                description='High quality wireless headphones with noise cancellation.',
                price=2299.00,
                image_filename='product1.jpg',
                category_id=c1.id
            ),
            Product(
                name='Smart Watch',
                description='Feature-rich smart watch with heart rate monitoring.',
                price=4999.00,
                image_filename='product2.jpg',
                category_id=c1.id
            ),
            Product(
                name='Men T-Shirt',
                description='Comfortable cotton t-shirt for casual wear.',
                price=499.00,
                image_filename='product3.jpg',
                category_id=c2.id
            ),
            Product(
                name='Women Jeans',
                description='Stylish and comfortable women\'s jeans.',
                price=1299.00,
                image_filename='product4.jpg',
                category_id=c2.id
            ),
            Product(
                name='Science Fiction Novel',
                description='A thrilling sci-fi novel full of adventure and mystery.',
                price=299.00,
                image_filename='product5.jpg',
                category_id=c3.id
            ),
        ]
        db.session.add_all(products)

        # Default user
        user = User(username='user1', email='user1@example.com')
        user.set_password('password')
        db.session.add(user)

        db.session.commit()
        print("Database initialized with sample data and default user.")


app = create_app()

with app.app_context():
    # Check if admin user exists
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(username='admin', email='admin@example.com')
        admin.set_password('admin123')  # Set secure admin password here
        db.session.add(admin)
        db.session.commit()
        print("Admin user created with username 'admin' and password 'admin123'")
    else:
        print("Admin user already exists.")

if __name__ == '__main__':
    init_db()
