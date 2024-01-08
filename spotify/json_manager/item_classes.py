#Here I'll create classes for itens received by json user data

class ItensList:
    def __init__(self) -> None:
        self.current_list = []
    
    def add_item_on_list(self, item):#receive one item, artist or song item
        self.current_list.append(item)

    def return_list(self):
        return self.current_list

class SongItem:
    pass


class ArtistItem:
    pass