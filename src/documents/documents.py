import re
from tinydb import TinyDB, Query

class Documents(object):

    def __init__(self, path: str):
        self._ = TinyDB(path)

    def insert(self, document: dict):
        self._.insert(document)

    def search_labels(self,regex: str):
        query = re.compile(regex, re.IGNORECASE)
        return [ item for item in self._ 
                 if [label for label in item['labels']
                     if query.search(label)]]

    def pretty_print_search(self,regex: str):
        for j in [(i['labels'], i['created'])
                  for i in self.search_labels(regex)]:
            print(j)

    def update_labels(self, created: str, labels: list):
        Item = Query()
        self._.update({'labels': labels}, Item.created == created)

    def get_document(self, created: str):
        Item = Query()
        return self._.search(Item.created == created)

    def generate_pdf(self, src_path: str, documents: list, dest_pdf_file: str):
        from PIL import image
        images = [Image.open(src_path + f) for f in documents]
        images[0].save(
            dest_pdf_file, "PDF", resolution=100.0, save_all=True, append_images=images[1:])

    def __del__(self):
        self._.close()
