class Movies:
    def __init__(self, title, hero, heroine) :
        self.title = title
        self.hero = hero
        self.heroine = heroine
    
    def info(self):
        print("Movie title is:",self.title)
        print("Hero name is:",self.hero)
        print("Heroine name is:",self.heroine) 
    
listOfMovies = []
while True:
    title = input("Enter movie title: ")
    hero = input("Enter movie's hero name: ")
    heroine = input("Enter movie's heroine name: ")
    m = Movies(title, hero, heroine)
    listOfMovies.append(m)
    print("Movie added successfully.......!!")
    option = input("Do you want to add more movies(y/n): ")
    if option.lower() == 'n':
        break
    
    
print("All movies in the list are:")
for movie in listOfMovies:
    movie.info()
    print()