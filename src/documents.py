import re
from tinydb import TinyDB, Query

class Documents(object):

    def __init__(self, path):
        self._ = TinyDB(path)

    def insert(self, document):
        self._.insert(document)

    def search_labels(self,regex):
        query = re.compile(regex, re.IGNORECASE)
        return [ item for item in self._ 
                 if [label for label in item['labels']
                     if query.search(label)]]

    def update_labels(self, created, labels):
        Item = Query()
        self._.update({'labels': labels}, Item.created == created)

    def get_document(self, created):
        Item = Query()
        return self._.search(Item.created == created)

    def __del__(self):
        self._.close()
