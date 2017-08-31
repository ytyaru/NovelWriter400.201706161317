import tinydb
import datetime
db = tinydb.TinyDB('human.json')
table = db.table('Human')
table.insert({'name': '山田', 'created': '{0:%Y-%m-%d %H:%M:%S.%f}'.format(datetime.datetime.now())})
print(table.all())
#db.purge_tables()

