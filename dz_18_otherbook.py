from json import *


class Book(object):

    def __init__(self, title_book='Angels and Demons', year_issue=2000, publisher='Pocket Books',
                 genre='Detective', author='Dan Brown', price=15):
        self.title_book = title_book
        self.year_issue = year_issue
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def __str__(self):
        return f'Название книги: {self.title_book}\nГод выпуска: {self.year_issue}\nИздательство: {self.publisher}' \
               f'\nЖанр:{self.genre}\nАвтор: {self.author}\nЦена: {self.price}\n'

    def __doc__(self):
        return "\n\nПереопределенный метод с документацией\nКонструктор для класса Book\nПеременные: Название книги - title_book\n" \
               "Год выпуска - __year_issue\nИздательство - publisher\nЖанр - genre\nАвтор - author\nЦена - price\n" \
               "С getter и setter для каждой переменной"

    def get_info(self):
        return f' Название: {self.title_book}\n Год выпуска: {self.year_issue}\n Издательство: {self.publisher}\n ' \
               f'Жанр: {self.genre}\n Автор: {self.author}\n Цена: {self.price}'

    @property
    def _title(self):
        return self.title_book

    @_title.setter
    def _title(self, value):
        self.title_book = value

    @property
    def _year(self):
        return self.price

    @_year.setter
    def _year(self, value):
        if str(value).isdigit():
            self.year_issue = value
        else:
            print('Неверное значение')

    @property
    def _publisher(self):
        return self.publisher

    @_publisher.setter
    def _publisher(self, value):
        self.publisher = value

    @property
    def _genre(self):
        return self.genre

    @_genre.setter
    def _genre(self, value):
        self.genre = value

    @property
    def _author(self):
        return self.author

    @_author.setter
    def _author(self, value):
        self.author = value

    @property
    def _price(self):
        return f'Цена книги {self.title_book} составляет {self.price}'

    @_price.setter
    def _price(self, value):
        if str(value).isdigit():
            self.price = value
        else:
            print('Неверное значение')


def serialized(instance):
    res = dumps(instance.__dict__, indent=3)
    return res


def unpacking_data(data_row, cls):
    res = loads(data_row)
    print(type(res))  # десериализация в dict
    exem = cls()
    exem.title_book = res['title_book']
    exem.year_issue = res['year_issue']
    exem.publisher = res['publisher']
    exem.genre = res['genre']
    exem.author = res['author']
    exem.price = res['price']
    return exem


try:


    book5 = Book('The Da Vinci Code', 2000, 'Publisher', 'detective', "Dan Brown", 20)
    packing_data = serialized(book3)
    print(type(packing_data))  # тип str
    print(packing_data)  # сериализация

    book4 = unpacking_data(packing_data, Book)  # десериализация в объект класса
    print(book4)
    print(type(book4))
except Exception as e:
    print(e)

