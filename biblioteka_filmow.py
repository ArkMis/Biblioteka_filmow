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
    
    def play(self):
        #self.__play_count+=1
        super().count_play()
        print('Title: %s  Season: %d  Episode: %d ' % (self.title, self.season_no, self.episode_no))

class FeatureFilm(Film):
    def play(self):
        super().count_play()
        print('Title: %s  rok: %d ' % (self.title, self.publ_year))

ff1=FeatureFilm(title='CK Dezerterzy', publ_year=1995, film_genre='komedia')
fs1=FilmSerial(title='Niania', publ_year=1996, film_genre='komedia', season_no=1, episode_no=1)

print('--- fabularny ---')
print(ff1.title)
print(ff1.publ_year)
print(ff1.film_genre)
print(ff1.play_count)
ff1.play()
print(ff1.play_count)
#ff1.play_count=5
#print(ff1.play_count)

print('--- serial ---')
print(fs1.title)
print(fs1.publ_year)
print(fs1.film_genre)
print(fs1.play_count)
fs1.play()
print(fs1.play_count)
