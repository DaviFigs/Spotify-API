#Here I'll create classes for itens received by json user data

class Itens:
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


'''
planning here: Make one def wich receive one big json as parameter
thia parameter can be top artists or top songs
Decript the json item by item inside a for,(or another json func)
take one item data and instance one object, send this objetct for the Itens class and append at the list
one by one item

send this object list to views, and finally send them to html!
'''