class Song:
    count =0
    genres =[]
    artists =[]
    genre_count ={}
    artist_count ={}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()
    
    @classmethod
    def add_song_to_count(cls):
        cls.count +=1


    def add_to_genres(self):
        if self.genre not in self.genres:
            self.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in self.artists:
            self.artists.append(self.artist)

    #a dictionary in which the keys are the names of each genre. Each genre 
    # name key should point to a value that is the number of songs that have that genre.

    def add_to_genre_count(self):
        self.genre_count[self.genre] = self.genre_count.get(self.genre, 0)+1

    def add_to_artist_count(self):
        self.artist_count[self.artist] = self.artist_count.get(self.artist, 0)+1


# Test examples
# Runit =Song("Runnit","Breezy", "Hip-hop")
# numb =Song("numb","Linkin Park", "Rock")
# yellow =Song("yellow","cold play", "Rock")
# overdrive =Song("overdrive","Post malone", "Hip-hop")
# white_inversion =Song("white_inversion","Post malone", "Hip-hop")

# print(Song.genre_count)
# print(Song.artist_count)

    
