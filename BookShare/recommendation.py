from BookShare.models import Uuser
import operator
# need some tests

def recommend(c_user):
    '''
        c_user: a user object
        '''

    book_score = {}
    '''
    if c_user.subjects == None and c_user.keywords == None:
        for peruser in user.objects.all():
            userslist.append(peruser)
        return userslist
    '''
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

