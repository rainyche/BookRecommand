import user

class Book(object):
    '''
    A book object is constructed when a book is recommended.
    Attributes: title, author, subject, recommender
    '''
    def __init__(self, title, author, subject, recommender):
        self.title = title
        self.author = author
        self.subject = subject
        book.review = None
        book.rating = None
        book.recommender = recommender
    
    def add_review(self, user, review):
        self.review = review

    def add_rating(self, user, rating):
        self.rating = rating



     