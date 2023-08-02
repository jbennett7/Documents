from tinydb import Query
from documents import Documents
import os
import unittest

db_path = '/tmp/foo.json'

dummys = [
    {'files': ['87b2.png', '8ba68.png', 'e225.png', '166c8.png'],
     'labels': ['pingpong', 'bingbang', 'motor'],
     'created': '2023-07-22 13:53:44.338127'},
    {'files': ['195be.png', 'f43.png'],
     'labels': ['motor', 'mom'],
     'created': '2023-07-22 14:42:30.382977'},
    {'files': ['d6e7.png'],
     'labels': ['tunnel', 'dad'],
     'created': '2023-07-22 14:50:03.937615'},
    {'files': ['d344.png'],
     'labels': ['prop', 'bing'],
     'created': '2023-07-22 15:08:54.553278'},
    {'files': ['55422.png'],
     'labels': ['foo', 'dad'],
     'created': '2023-07-22 15:11:51.486777'},
    {'files': ['d75.png', '612.png'],
     'labels': ['foo', 'motor'],
     'created': '2023-07-22 15:13:18.061376'},
    {'files': ['4953.png'],
     'labels': ['barber', 'bingo'],
     'created': '2023-07-22 15:14:49.264192'},
    {'files': ['dfd.png', '482.png', 'f7e.png', '49b762.png'],
     'labels': ['motor', 'dad', 'jen'],
     'created': '2023-07-22 15:21:28.384061'},
    {'files': ['ff6ff.png', 'a8f04.png'],
     'labels': ['follow', 'sheep'],
     'created': '2023-07-22 15:31:09.010078'}]

class TestDocuments(unittest.TestCase):

    def setUp(self):
        self.database = Documents(db_path)
        for item in dummys:
            self.database._.insert(item)

    def test_database(self):
           self.assertEqual(len(self.database._.all()), len(dummys)) 

    def test_insert(self):
        new_entry = {'files': ['uieid.png'],
                     'labels': ['wanda', 'jen', 'james'],
                     'created': '2023-08-01 23:08:20.092342'}
        self.database.insert(new_entry)
        verify = self.database.get_document('2023-08-01 23:08:20.092342')
        self.assertEqual(new_entry, verify[0])

    def test_get(self):
        item = dummys[3]
        verify = self.database.get_document(item['created'])
        self.assertEqual(item,verify[0])

    def test_search_labels(self):
        results = self.database.search_labels('dad')
        self.assertTrue('2023-07-22 15:11:51.486777' in 
                        [i['created'] for i in results])

    def test_update_labels(self):
        new_labels = ['mom','jen','dad']
        cid = '2023-07-22 15:31:09.010078'
        self.database.update_labels(cid,new_labels)
        CID = Query()
        verify_labels = self.database._.search(CID.created == cid)[0]['labels']
        self.assertEqual(new_labels,verify_labels)

    def tearDown(self):
        os.remove(db_path)
