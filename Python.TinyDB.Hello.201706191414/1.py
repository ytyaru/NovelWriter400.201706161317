import tinydb
db = tinydb.TinyDB('1.json')
table = db.table('Human')
table.insert({'name': '山田'})
print(table.all())
#db.purge_tables()

