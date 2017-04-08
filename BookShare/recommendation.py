from class_user import user
from class_book import book

# need some tests

def potential_recommend(c_user):
    '''
        c_user: a user object
        '''
    userslist = []
    if c_user.author == None and c_user.subject == None and c_user.keyword == None:
        for peruser in user.objects.all():
            userslist.append(peruser)
        return userslist
    else:
        p_recommend = []
        for peruser in user.objects.all():
            if (book.author == c_user.author) or (book.subject == c_user.subject) or (c_user.keyword in book.review):
                p_recommend.append(peruser)
        return p_recommend

def recommend(c_user):
    p_recommend = potential_recommend(c_user)
    d = {}
    maxi = 0
    for otheruser in p_recommend:
        matching = c_user.match(otheruser)
        score = matching
        if otheruser.books not in d:
            d[otheruser.books] = 0
        d[otheruser.books] += score
    recommend = sorted(d.items(), key=lambda x: x[1])
    recommend = [book[0] for book in recommend]
    if len(recommend) >=20:
        return recommend[:20]
    else:
        return recommend
