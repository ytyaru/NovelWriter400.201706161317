from abc import ABCMeta, abstractmethod
import os.path
import src.Database
import src.export.SettingPath
import src.export.FilenameCreater
import src.export.FileWriter
class Exporter(metaclass=ABCMeta):
    def __init__(self, base_path=None, file_name_format=None):
#        self.__database = src.Database.DatabaseAccesser()
        db_dir = os.path.join(base_path, 'src/db')
        print(db_dir)
        self.__database = src.Database.DatabaseAccesser(path=db_dir)
        self.__setting = src.export.SettingPath.SettingPath(base_path)
        self.__filename = src.export.FilenameCreater.FilenameCreater(format=file_name_format)
        self.__writer = src.export.FileWriter.FileWriter()
    @property
    def Database(self): return self.__database
    @property
    def SettingPath(self): return self.__setting
    @property
    def FilenameCreater(self): return self.__filename
    @property
    def FileWriter(self): return self.__writer
    @abstractmethod
    def Export(self, is_overwrite=False): pass
