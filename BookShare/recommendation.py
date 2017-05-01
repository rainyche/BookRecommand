from BookShare.models import Uuser
import operator

# This is the recommendation function. 
# We give higher weights to books recommended by people that
# are similar to the current user.

def recommend(c_user):

    book_score = {}

    for peruser in Uuser.objects.all():
        if peruser.books not in book_score.keys():
            book_score[peruser.books] = 0
        if (peruser.keywords == c_user.keywords):
            book_score[peruser.books] += 1
        if (peruser.subjects == c_user.subjects):
            book_score[peruser.books] += 1
        if (peruser.industry == c_user.industry):
            book_score[peruser.books] += 1
        if (peruser.major == c_user.major):
            book_score[peruser.books] += 1

    l_book = sorted(book_score.items(), key=operator.itemgetter(1), reverse = True)
    return l_book

