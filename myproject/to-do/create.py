from app import db, To_do

db.drop_all()
db.create_all()

test = To_do(title='Clean Room', description='Put away clothes and vacuum the floor', completed=True)
db.session.add(test)
db.session.commit()