import tinydb
db = tinydb.TinyDB('0.json')
db.insert({'name': '山田'})
for item in db:
    print(item)
