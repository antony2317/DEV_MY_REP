from sqlalchemy import create_engine, Integer, String, Date, Boolean, ForeignKey, Enum, Float, Column
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_email = Column(String)

    leases = relationship('Lease', back_populates='user')


class Property(Base):
    __tablename__ = 'properties'

    property_id = Column(Integer, primary_key=True)
    address = Column(String)

    property_type_enum = Enum('Жилая', 'Коммерческая', name='property_type_enum')
    property_type = Column(property_type_enum, default='Жилая')

    rent_price = Column(Float)
    leases = relationship('Lease', back_populates='property')


class Lease(Base):
    __tablename__ = 'leases'

    lease_id = Column(Integer, primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    status_lease = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    property_id = Column(Integer, ForeignKey('properties.property_id'))

    user = relationship('User', back_populates='leases')
    property = relationship('Property', back_populates='leases')
    payments = relationship('Payment', back_populates='lease')


class Payment(Base):
    __tablename__ = 'payments'

    payment_id = Column(Integer, primary_key=True)
    amount = Column(Float)
    payment_date = Column(Date)
    lease_id = Column(Integer, ForeignKey('leases.lease_id'))

    lease = relationship('Lease', back_populates='payments')


engine = create_engine('sqlite:///library_new.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_user():
    user_1 = User(user_name='Pavel', user_email='pavel@gmail.com')
    user_2 = User(user_name='Anton', user_email='anton@mail.ru')

    session.add_all([user_1, user_2])
    session.commit()


def add_property():
    property_1 = Property(address='Lesnaya 16/1', property_type='Жилая', rent_price=5678.19)
    property_2 = Property(address='Комсомольская 45', property_type='Коммерческая', rent_price=10500.87)

    session.add_all([property_1, property_2])
    session.commit()


def add_lease():
    user_1 = session.query(User).filter(User.user_name == 'Pavel').first()
    property_1 = session.query(Property).filter(Property.property_id == 1).first()

    lease_1 = Lease(
        start_date=datetime.strptime('2024.01.01', '%Y.%m.%d').date(),
        end_date=datetime.strptime('2025.09.15', '%Y.%m.%d').date(),
        status_lease=True,
        user_id=user_1.user_id,
        property_id=property_1.property_id
    )

    session.add(lease_1)
    session.commit()

    pay_1 = Payment(amount=3435, payment_date=datetime.strptime('2025.04.13', '%Y.%m.%d').date(),
                    lease_id=lease_1.lease_id)
    pay_2 = Payment(amount=9876, payment_date=datetime.strptime('2025.05.15', '%Y.%m.%d').date(),
                    lease_id=lease_1.lease_id)

    session.add_all([pay_1, pay_2])
    session.commit()


def add_payment():
    pass


add_user()
add_property()
add_lease()

leases = session.query(Lease).all()
users = session.query(User.user_name).all()
properties = session.query(Property.address).all()

print("Leases:", leases)
print("Users:", users)
print("Properties:", properties)
