from db import db

service = db.Table(
    'service',
    db.Column('number', db.Integer, db.ForeignKey('room.number')),
    db.Column('passport_id', db.Integer, db.ForeignKey('staff.passport_id'))
)


class Room(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String)
    status = db.Column(db.String)
    price = db.Column(db.Integer)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.passport_id'))
    served = db.relationship('Staff', secondary=service, backref=db.backref('served'))


class Staff(db.Model):
    name = db.Column(db.String)
    passport_id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String)
    salary = db.Column(db.Integer)


class Tenant(db.Model):
    name = db.Column(db.String)
    passport_id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String)
    city = db.Column(db.String)
    address = db.Column(db.String)
    room = db.relationship('Room', backref='tenant')

