from abc import ABCMeta, abstractmethod
import os
import os.path
import dataset
import urllib.parse
import datetime
import collections
import traceback
class DatabaseAccesser:
    def __init__(self, path='./db/'):
        dbc = DatabaseConnector()
        self.__novels = dbc.Connect(Novels(), path)
        self.__dbs = [self.__novels]

    def DbBegin(self):
        [x.begin() for x in self.__dbs]
    def DbCommit(self):
        [x.commit() for x in self.__dbs]
    def DbRollback(self):
        [x.rollback() for x in self.__dbs]

    def __Transact(func):
        def wrapper(self, *args, **kwargs):
            ret = None
            try:
                self.DbBegin()
                ret = func(self, *args, **kwargs)
                self.DbCommit()
                print('DBにコミットしました。')
                return ret
            except:
                import traceback
                traceback.print_exc()
                self.DbRollback()
                print('DBをロールバックしました。')
                return ret
        return wrapper
        
    """
    DBにある全データを1つずつ返す。
    """
    def Loads(self, is_latest=True) -> collections.OrderedDict:
        if is_latest: return self.__novels['Novels'].find(order_by=['-Created'])
        else: return self.__novels['Novels'].find(order_by=['Created'])
#        return self.__novels['Novels'].find()
    
    """
    DBへ挿入する。
    """
    @__Transact
    def Insert(self, content, title=None):
        now = datetime.datetime.now()
#        if None is title or '' == title.strip(): title = "{0:%Y%m%d%H%M%S}".format(now)
        if None is title or '' == title.strip(): title = ''
        d = dict(
            Title=title,
            Content=content,
            Length=len(content),
            Created="{0:%Y-%m-%d %H:%M:%S}".format(now)
        )
        self.__novels['Novels'].insert(d)
        return d

class DatabaseConnector():
    def __init__(self):
        self.__db = None
        self.__tables = []
        self.__extension = 'db'
        self.__file_name = self.__class__.__name__ + '.' + self.__extension

    """
    DBに接続する。DBファイルがないなら作成しテーブルを作成する。
    @param {Database.__Database} databaseは__Database継承クラス。このDatabaseを開く。
    @param {str} path_dirはDBファイルを作成するディレクトリ。
    """
    def Connect(self, database, path_dir=None):
        path = self.__GetDbFilePath(database, path_dir)
        if not(os.path.isfile(path)):
            self.__CreateFile(path)
        db = dataset.connect('sqlite:///' + path)
        if database.Name not in db:
            db.query(database.CreateTableString)
        return db

    def __GetDbFilePath(self, database, path):
        if path:
            return os.path.abspath(os.path.join(path, database.Filename))
        else:
            return os.path.join(os.path.abspath(os.path.dirname(__file__)), database.Filename)

    def __CreateFile(self, path):
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, 'w') as f:
            pass
        print('ディレクトリやファイルを作成しました。: {0}'.format(path))

class Database(metaclass=ABCMeta):
    def __init__(self):
        self.__db = None
        self.__extension = 'db'
        self.__file_name = self.__class__.__name__ + '.' + self.__extension
    @property
    def Extension(self):
        return self.__extension
    @property
    def Filename(self):
        return self.__file_name
    @property
    def Name(self):
        return self.__class__.__name__
    @property
    @abstractmethod
    def CreateTableString(self):
        return self.__tables

class Novels(Database):
    def __init__(self):
        super().__init__()

    @Database.CreateTableString.getter
    def CreateTableString(self):
        return """create table "Novels" (
    "Id"                integer primary key,
    "Title"             text,
    "Content"           text not null,
    "Length"            integer, -- Contentの文字数
    "Created"           text
);
"""

