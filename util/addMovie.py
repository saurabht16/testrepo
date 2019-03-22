dictmovies ={'name':['Jurassic Park', 'Jurasic Park: The Last World', 'Jurassic Park III', 'Jurassic World','Jurassic World:Fallen Kingdom','The Mummy', 'The Mummy Returns'],'year':['1993', '1997', '2001', '2015', '2018', '1999', '2001'],'director':['Steven Spielberg', 'Steven Spielberg', 'Joe Johnson', 'Collin Trevorrow','J.A.Bayona', 'Stephen Summers', 'Stephen Summers']}
listmovies = []
listmovies=list(dictmovies["name"])
listmoviesyear = list(dictmovies["year"])
listmoviesdirector = list(dictmovies["director"])

def viewmovie():
    dash = '-' * 100

    for i in range(len(listmovies)):
        if i == 0:
            print(dash)
            print('{:<40s}{:>4s}{:>20s}'.format("Movies", "Year", "Director"))
            print(dash)
        else:
            print('{:<40s}{:>4s}{:^30s}'.format(listmovies[i].strip(), listmoviesyear[i].strip(),listmoviesdirector[i].strip()))


def addmovie():
    name  = input("Enter movie\'s name ")
    listmovies.append(name)
    year = input("Enter year of the movie")
    listmoviesyear.append(year)
    director = input("Enter director of the movie")
    listmoviesdirector.append(director)
    viewmovie()


def searchmovie():

    print(" Search Criteria...")
    c = input('Enter Y -> By Year D ->By Director ')

    if c.upper()=='Y':
        year= input("Enter Year")
        for i in range(len(listmovies)):
            if listmoviesyear[i]== year:
                print('{:<40s}{:>4s}{:^30s}'.format(listmovies[i], listmoviesyear[i], listmoviesdirector[i]))

    elif c.upper() == 'D':
        director = input("Enter director name")
        for i in range(len(listmovies)):
            if listmoviesdirector[i]== director:
                print('{:<40s}{:>4s}{:^30s}'.format(listmovies[i], listmoviesyear[i], listmoviesdirector[i]))
