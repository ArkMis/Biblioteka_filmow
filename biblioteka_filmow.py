# Biblioteka filmów

class Film:
   def __init__(self,title,publ_year,film_genre):
        self.title=title
        self.publ_year=publ_year
        self.film_genre=film_genre
        #variables
        self.__play_count=0

   def count_play(self):
       self.__play_count += 1

   @property
   def play_count(self):
        return self.__play_count

class FilmSerial(Film):
    def __init__(self, episode_no, season_no,  *args, **kwargs):
        super().__init__(*args, ** kwargs)
        self.episode_no=episode_no
        self.season_no=season_no
    
    def __str__(self):
        return f'{self.title} S{self.season_no:02d}E{self.episode_no:02d}'

    def play(self):
        super().count_play()
        
class FeatureFilm(Film):
    def __str__(self):
        return f'{self.title} {self.publ_year}'

    def play(self):
        super().count_play()
       
def get_movies():
    """
    funkcja filtruje listę i zwraca tylko filmy fabularne posortowane alfabetyczne
    """
    for i in range(len(film_list)):
       if isinstance(film_list[i],FeatureFilm):
          ffilm_list.append(film_list[i])
        
def get_series():
    """
    funkcja filtruje listę i zwraca tylko seriale posortowane alfabetycznie
    """
    for i in range(len(film_list)):
       if isinstance(film_list[i],FilmSerial):
          sfilm_list.append(film_list[i])
    

def search(self,stitle):
    """
    fukcja wyszukuje film lub serial po jego tytule
    """
    pass

def generate_views():
    """
    funkcja losowo wybiera element z biblioteki, a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń
    """
    pass

def top_titles(content_type):
    """
    funkcja zwraca wybraną ilość najpopularniejszych tytułów z biblioteki
    """
    pass

def generate_view_10():
    pass

def init_list():
    film_list.append(FeatureFilm(title='CK Dezerterzy', publ_year=1995, film_genre='komedia'))
    film_list.append(FeatureFilm(title='Milczenie owiec', publ_year=1996, film_genre='triller'))
    film_list.append(FeatureFilm(title='Gorączka', publ_year=1997, film_genre='triller'))
    film_list.append(FeatureFilm(title='Pulp Fiction', publ_year=1994, film_genre='triller'))
    film_list.append(FeatureFilm(title='Milczenie owiec', publ_year=1996, film_genre='triller'))
    film_list.append(FeatureFilm(title='Star Wars', publ_year=2002, film_genre='Sci-Fi'))
    film_list.append(FeatureFilm(title='Dom Gucci', publ_year=2021, film_genre='Dramat'))

    for s in range(1, 4):
        for e in range(1, 9):
            film_list.append(FilmSerial(title='Niania', publ_year=1996+s, film_genre='komedia', season_no=s, episode_no=e))
        for e in range(1, 7):
            film_list.append(FilmSerial(title='Chicago Fire', publ_year=1996+s, film_genre='dramat', season_no=s, episode_no=e))
        for e in range(1,10):
            film_list.append(FilmSerial(title='Chicago Med', publ_year=2015+s, film_genre='dramat', season_no=s, episode_no=e))
        for e in range(1,7):
            film_list.append(FilmSerial(title='New Amsterdam', publ_year=2018+s, film_genre='dramat', season_no=s, episode_no=e))


film_list=[]
ffilm_list=[]
sfilm_list=[]


init_list()

for i in range(len(film_list)):
    if isinstance(film_list[i],FilmSerial):
        sfilm_list.append(film_list[i])
    else:
        ffilm_list.append(film_list[i])

for i in range(len(film_list)):
    print(film_list[i])
    #print(type(film_list[i]))
    #print(film_list[i].play())

print('--- Filmy fabularne ---')
for i in range(len(ffilm_list)):
    print(ffilm_list[i])
print('')
print('--- Seriale ---')
for i in range(len(sfilm_list)):
    print(sfilm_list[i])

