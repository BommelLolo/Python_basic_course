class Pizza:
    def __init__(self, pineapples=False, chicken=False, sausages=False):
        pass


class PizzaBuilder:
    def __init__(self):
        self._ingredients = {}

    def add_pineapples(self):
        self._ingredients['pineapples'] = True
        return self

    def add_chicken(self):
        self._ingredients['chicken'] = True
        return self

    def add_sausages(self):
        self._ingredients['sausages'] = True
        return self

    def build(self):
        return Pizza(**self._ingredients)


# class Havaii(Pizza):
#     def __init__(self, pineapple, chicken):
#         pass
#
#
# class Peperoni(Pizza):
#     def __init__(self, sausages):
#         pass


class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    def authored_by(self):
        return self._author


class Author:
    def __init__(self, full_name):
        self._full_name = full_name

    def write_book(self, name):
        return Book(name, self)


if __name__ == '__main__':
    havaii = Pizza(True, True)
    pepperoni = Pizza(False, False, True)

    builder = PizzaBuilder()
    builder.add_chicken()
    builder.add_sausages()
    new_pizza = builder.build()

    new_pizza2 = PizzaBuilder().add_sausages().add_chicken().build()
    assert isinstance(new_pizza2, Pizza)

    rowling = Author('J.K. Rowling')
    book_hp = rowling.write_book('HP')

    assert rowling is rowling

    assert isinstance(book_hp, Book)
    assert isinstance(book_hp.authored_by(), Author)
    assert book_hp.authored_by() is rowling
    