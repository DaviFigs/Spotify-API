#Here I'll create classes for itens received by json user data

class SongItem:
    def __init__(self, link, name, album, artist, duration) -> None:
        self.link = link
        self.name = name
        self.album = album
        self.artist = artist
        self.duration = duration


class ArtistItem:
    def __init__(self, link, name, popularity) -> None:
        self.link = link
        self.name = name
        self.popularity = popularity
