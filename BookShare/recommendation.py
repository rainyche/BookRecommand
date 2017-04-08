from BookShare.models import Uuser
# need some tests

def potential_recommend(c_user):
    '''
        c_user: a user object
        '''
    userslist = []
    '''
    if c_user.subjects == None and c_user.keywords == None:
        for peruser in user.objects.all():
            userslist.append(peruser)
        return userslist
    '''
    for peruser in Uuser.objects.all():
        if (peruser.keywords == c_user.keywords) or (peruser.subjects == c_user.subjects) or (c_user.industry == peruser.industry) or (peruser.major == c_user.major):
            userslist.append(peruser)
    return userslist

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
