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
        return f'{self.title} S{self.season_no} E{self.episode_no}'

    def play(self):
        super().count_play()
        #print('Title: %s  Season: %d  Episode: %d ' % (self.title, self.season_no, self.episode_no))
        print('Title: %s  S%02dE%02d ' % (self.title, self.season_no, self.episode_no))

class FeatureFilm(Film):
    def __str__(self):
        return f'{self.title} {self.publ_year}'

    def play(self):
        super().count_play()
        #print('Title: %s  rok: %d ' % (self.title, self.publ_year))
        print('%s  (%d) ' % (self.title, self.publ_year))

film_list=[]

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

print('--- fabularny ---')
#print(film_list[0].title)
#print(film_list[0].publ_year)
#print(film_list[0].film_genre)
#print(film_list[0].play_count)
#film_list[0].play()
#print(film_list[0].play_count)


print('--- serial ---')
#print(film_list[10].title)
#print(film_list[10].publ_year)
#print(film_list[10].film_genre)
#print(film_list[10].play_count)
#film_list[10].play()
#print(film_list[10].play_count)

for i in range(len(film_list)):
    print(film_list[i])
    #print(film_list[i].play())