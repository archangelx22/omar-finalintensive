class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("{} email has been updated.".format(self.name))

    def __repr__(self):
        return "User {name}, email: {email}, books read: {bookcount}".format(name=self.name, email=self.email,
                                                                             bookcount=len(self.books))

    def read_book(self, book, rating):
        self.books[book] = rating

    def get_average_rating(self):
        num_items = 0
        total = 0
        for i in self.books.values():
            if i is not None:
                num_items += 1
                total += i
        return total / num_items

    def __eq__(self, other_user):
        if other_user.name == self.name and other_user.email == self.email:
            return True
        else:
            return False

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{} isbn has been updated.".format(self.title))

    def add_rating(self, rating):
        valid = [0,1,2,3,4,5]
        if  rating in valid:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
    def __eq__(self, other):
        if other.title == self.title and other.isbn == self.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        num_items = 0
        total = 0
        for i in self.ratings:
            num_items += 1
            total += i
        return total / num_items

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fictionbook(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title =  self.title, author = self.author)


class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level,
                                                               subject = self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title,isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_fiction = Fictionbook(title, author, isbn)
        return new_fiction

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = NonFiction(title, subject, level, isbn)
        return non_fiction

    def add_book_to_user(self, book, email, rating = None):
        if self.users[email]:
            activeuser = self.users[email]
            activeuser.read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {}".format(email))

    def add_user(self, name, email, user_books = None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for i in user_books:
                self.add_book_to_user(i, email)

    def print_catalog(self):
        for i in self.books:
            print(i)

    def print_users(self):
        for i in self.users:
            print(i)

    def most_read_book(self):
        good_book = 5
        rating = 0
        for i in self.books:
            if self.books[i] > rating:
                rating = self.books[i]
                good_book = i
            else:
                continue
        return good_book

    def highest_rated_book(self):
        top_rating = 0
        topbook = ""
        for book in self.books:
            if book.get_average_rating() > top_rating:
                top_rating = book.get_average_rating()
                topbook = book
            else:
                continue
        return topbook

    def most_positive_user(self):
        top_user = ""
        top_rating = 0
        for i in self.users.values():
            if i.get_average_rating() > top_rating:
                top_rating = i.get_average_rating()
                top_user = i
            else:
                continue
        return top_user



