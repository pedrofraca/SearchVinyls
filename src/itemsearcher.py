import itemsearcher_discogs
import itemsearcher_todocoleccion
class itemsearcher:
    def search_items_by_string(self,text):
        items_discogs = itemsearcher_discogs.get_items(text)
        items_todo_coleccion = itemsearcher_todocoleccion.get_items(text)
        return items_discogs + items_todo_coleccion