import tinydb
import os.path
file_path = '2.json'
db = None
if not os.path.isfile(file_path):
    db = tinydb.TinyDB(file_path)
    db.insert({'name': '山田', 'age': 10})
    db.insert({'name': '鈴木', 'age': 22})
    db.insert({'name': 'Yamada', 'age': 33})
    db.insert({'name': '島田', 'age': 2})
    db.insert({'name': '吉田', 'age': 88})
    db.insert({'name': '福田', 'age': 5})
    db.insert({'name': '田田田', 'age': 5})
if None is db: db = tinydb.TinyDB(file_path)

print(db.all())
query = tinydb.Query()
response = db.search(query.name == 'Yamada')
print(response)
print(db.search(22 <= query.age))
print(db.search(query.name.matches('.田')))
db.close()
