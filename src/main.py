from scanner import Scanner
from uuid import uuid4
from tinydb import TinyDB, Query
import datetime

documents_path = '/run/media/jbennett/Joe/Documents'
database_path = '/run/media/jbennett/Joe/Documents/documents.json'

input("Make sure the scanner is on and paper is in the feed...")
scanner = Scanner()
scanner.initialize_device()

smodes = scanner.get_modes()
modes = ', '.join(smodes)
selected_mode = ''
while selected_mode not in smodes:
    selected_mode = input(f'Select a mode:  {modes}  ')
    if selected_mode not in smodes:
        print(f'{selected_mode} is not a mode')
scanner.set_mode(selected_mode)
print(scanner.get_current_mode())

sc_sources = scanner.get_sources()
sources = ', '.join(sc_sources)
selected_source = ''
while selected_source not in sc_sources:
    selected_source = input(f'Select a source: {sources}  ')
    if selected_source not in sc_sources:
        print(f'{selected_source} is not a source')
scanner.set_source(selected_source)
print(scanner.get_current_source())

multi = input('Scanning more than one (y/n)? ')
images = None
if multi == 'y':
    multi = True
    images = scanner.multi_page_scan()
else:
    multi = False
    images = scanner.single_page_scan()

linput = input("What labels do you want to add (separate with a comma): ")
labels = linput.split(', ')

created = str(datetime.datetime.now())

file_names = []
if multi:
    for image in images:
        file_name = str(uuid4())+'.png'
        file_names.append(file_name)
        image.save(documents_path+'/'+file_name)
else:
    file_name = str(uuid4())+'.png'
    file_names.append(file_name)
    images.save(documents_path+'/'+file_name)

document = {'files': file_names, 'labels': labels, 'created': created}
db = TinyDB(database_path)
db.insert(document)
