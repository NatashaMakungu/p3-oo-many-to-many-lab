class Author:
    pass
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of Book")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    pass
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    pass
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise Exception("Invalid author")
        self._author = new_author

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, new_book):
        if not isinstance(new_book, Book):
            raise Exception("Invalid book")
        self._book = new_book

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        if not isinstance(new_date, str):
            raise Exception("Invalid date")
        self._date = new_date

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, new_royalties):
        if not isinstance(new_royalties, int):
            raise Exception("Invalid royalties")
        self._royalties = new_royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]