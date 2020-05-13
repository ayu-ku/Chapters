from tinydb import TinyDB, Query, where


class Storage:
    def __init__(self):
        self.note_db = TinyDB("note_storage.json")

    def search_note_by_id(self, hash_item):
        query = Query()
        result = self.note_db.search(query.hash == hash_item)
        return result

    def add(self, data):
        self.note_db.insert(data)

    def update(self, data, hash_item):
        self.note_db.update(data, where("hash") == hash_item)

    def remove(self, hash_item):
        query = Query()
        self.note_db.db.remove(query.hash == hash_item)

    def list(self):
        self.note_db.all()
