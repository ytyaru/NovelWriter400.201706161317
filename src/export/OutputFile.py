import os
import os.path
import datetime
import src.export.FileWriter
import src.export.SettingPath
import src.export.OutputListFile
class OutputFile:
    def __init__(self, base_path=None):
        self.__setting = src.export.SettingPath.SettingPath(base_path)
        self.__writer = src.export.FileWriter.FileWriter()
    def Output(self, record):
        file_name = self.__GetFilename(record)
        for path in self.__setting.Load():
            self.__writer.Write(os.path.join(path, file_name), record)
            list_file = src.export.OutputListFile.OutputListFile(path)
            list_file.Output(file_name, record)
        return file_name

    def __GetFilename(self, record):
        d = datetime.datetime.strptime(record['Created'], '%Y-%m-%d %H:%M:%S')
        return '{0:%Y%m%d%H%M%S}'.format(d) + '.txt'

