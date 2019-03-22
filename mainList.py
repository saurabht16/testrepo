# Hello i am a git lover
from util import addMovie
def menu():
    print("Favorite Movie Collection")
    print("Please Choose")
    print("A     Add your favorite movie")
    print("V     View your favorite movie collection")
    print("S     Search for a favorite movie")
    print("X     Exit")


menu()

while(1):
    choice = input("Enter your choice").strip()
    if choice.upper() == 'A':
        addMovie.addmovie()
        menu()

    elif choice.upper() == 'V':
        addMovie.viewmovie()
        menu()
    elif choice.upper() == 'S':
        addMovie.searchmovie()
        menu()
    else:
        exit(0)

