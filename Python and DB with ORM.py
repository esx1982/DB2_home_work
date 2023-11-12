import sqlalchemy
import psycopg2
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:XInazkRgqj1982@localhost:5432/home_db_orm'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

pub1 = Publisher(name='Гуманитарный издательский центр Владос')
book1 = Book(title='Обломов', id_publisher=1)
shop1 = Shop(name='Республика')
stock1 = Stock(id_book=1, id_shop=1, count=10)
sale1 = Sale(price=184, date_of_sale='2023-10-10', id_stock=1, count=9)

book2 = Book(title='Война и мир', id_publisher=1)
stock2 = Stock(id_book=2, id_shop=1, count=15)
sale2 = Sale(price=2284, date_of_sale='2023-09-15', id_stock=2, count=10)

pub2 = Publisher(name='Издательская группа "АСТ"')
book3 = Book(title='Хмурые люди', id_publisher=2)
shop2 = Shop(name='Культура')
stock3 = Stock(id_book=3, id_shop=2, count=9)
sale3 = Sale(price=375, date_of_sale='2023-08-22', id_stock=3, count=15)

book4 = Book(title='Преступление и наказание', id_publisher=2)
stock4 = Stock(id_book=4, id_shop=2, count=9)
sale4 = Sale(price=496, date_of_sale='2023-07-16', id_stock=4, count=11)

pub3 = Publisher(name='Издательская группа "URSS.ru"')
book5 = Book(title='Вечера на хуторе близ Диканьки', id_publisher=3)
shop3 = Shop(name='Буквоед')
stock5 = Stock(id_book=5, id_shop=3, count=10)
sale5 = Sale(price=763, date_of_sale='2023-09-16', id_stock=5, count=12)

book6 = Book(title='Отцы и дети', id_publisher=3)
stock6 = Stock(id_book=6, id_shop=2, count=11)
sale6 = Sale(price=440, date_of_sale='2023-10-16', id_stock=6, count=13)

session.add_all([pub1, pub2, pub3, book1, book2, book3, book4, book5, book6, shop1, shop2, shop3, stock1, stock2, stock3, stock4, stock5, stock6, sale1, sale2, sale3, sale4, sale5, sale6])
session.commit()

pub_req = input("введите id издателя: ")

q = session.query(Book.title, Shop.name, Sale.price, Sale.date_of_sale).select_from(Shop).join(Stock).join(Book).join(Publisher).join(Sale). filter(Publisher.id == pub_req)
for book, shop, price, date in q:
        print(f"{book: <40} | {shop: <10} | {price: <8} | {date.strftime('%d-%m-%Y')}")

session.close()