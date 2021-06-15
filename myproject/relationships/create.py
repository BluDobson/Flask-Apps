from app import db, Countries, Cities
db.drop_all()
db.create_all()

UK = Countries(name = 'United Kingdom')
db.session.add(UK)
db.session.commit()

ldn = Cities(name='London', country = Countries.query.filter_by(name='United Kingdom').first())
mcr = Cities(name='Manchester', country = Countries.query.filter_by(name='United Kingdom').first())

db.session.add(ldn)
db.session.add(mcr)
db.session.commit()