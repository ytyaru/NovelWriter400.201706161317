import os
import os.path
import datetime
import src.export.SettingPath
class OutputListFile:
    def __init__(self, dir_path):
#    def __init__(self, dir_path=None):
        self.__dir_path = dir_path
    
    """
    list.tsvファイル書き出し。
    file_name: 対象レコードのファイル名
    record: 対象レコードのデータ
    """
    def Output(self, file_name, record):
        list_file_name = 'list.tsv'
        list_file_path = os.path.join(self.__dir_path, list_file_name)
        old = ''
        if os.path.isfile(list_file_path):
            with open(list_file_path, 'r') as f:
                old = f.read()
        with open(list_file_path, 'w') as f:
#        with open(os.path.join(dir_path, list_file_name), 'r+') as f:
#        with open(os.path.join(dir_path, list_file_name), 'a+') as f:
#            f.seek(0)
            f.write(self.__GetListFileLine(file_name, record) + old)
    
    def __GetListFileLine(self, file_name, record):
        return file_name + '\t' + self.__GetLengthStr(record['Title'], 10) + '\t' + self.__GetLengthStr(record['Content'], 20) + '\n'
        
    def __GetLengthStr(self, target, max_len):
        length = max_len
        if len(target) < length: length = len(target)
        return target[:length]

