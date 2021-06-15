from app import db, Customers, Products, Orders
db.drop_all()
db.create_all()

Tom = Customers(first_name='Tom', last_name='Davies', email='td@hotmail.com')
Dave = Customers(first_name='Dave', last_name='Ward', email='dw@hotmail.com')
db.session.add(Tom)
db.session.add(Dave)
db.session.commit()

Mic = Products(name='Mic', price='50.00')
Keyboard = Products(name='Keyboard', price='70.00')
db.session.add(Mic)
db.session.add(Keyboard)
db.session.commit()

t1 = Orders(customers = Customers.query.filter_by(first_name='Tom').first(), products = Products.query.filter_by(name='Mic').first())
t2 = Orders(customers = Customers.query.filter_by(first_name='Tom').first(), products = Products.query.filter_by(name='Keyboard').first())
d1 = Orders(customers = Customers.query.filter_by(first_name='Dave').first(), products = Products.query.filter_by(name='Keyboard').first())

db.session.add(t1)
db.session.add(t2)
db.session.add(d1)
db.session.commit()