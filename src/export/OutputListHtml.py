import os
import os.path
import datetime
from bs4 import BeautifulSoup
import logging
class OutputListHtml:
    def __init__(self, base_path=None):
        self.__SetBasePath(base_path)
        self.__path = []
        self.__parser = 'html.parser' # lxml

    def Output(self, file_path, record):
        self.__CreateFileListHtml()
        self.__InsertRecord(file_path, record)
        return self.__list_file_path

    def __CreateFileListHtml(self):
        if not os.path.isdir(self.__base_path): os.makedirs(self.__base_path, exist_ok=True)
        if not os.path.isfile(self.__list_file_path) or 0 == os.path.getsize(self.__list_file_path):
            with open(self.__list_file_path, 'w') as f:
                f.write(self.__CreateTable())
    
    def __InsertRecord(self, file_path, record):
        html_str = ''
        with open(self.__list_file_path) as f:
            html_str = f.read()
        soup = BeautifulSoup(html_str, self.__parser)
        tbody = soup.find('tbody')
        first = tbody.find('tr')
        if first:
            first.insert_before(BeautifulSoup(self.__CreateRecord(file_path, record), self.__parser))
        else:
            tbody.append(BeautifulSoup(self.__CreateRecord(file_path, record), self.__parser))
        with open(self.__list_file_path, 'w') as f:
            f.write(str(soup))
            
    def __SetBasePath(self, base_path):
        if base_path:
            self.__base_path = base_path
        else:
            self.__base_path = os.path.join(os.path.dirname(os.path.abspath( __file__ )), 'contents/')
        self.__list_file_path = os.path.join(self.__base_path, 'list.html')
        print(self.__list_file_path)
    
    def __CreateTable(self):
        return '<html><head><meta charset="utf-8"></meta></head><body><table><thread><tr><th>ファイル名</th><th>タイトル</th><th>本文</th></tr><thread><tbody></tbody></table></body></html>'
    
    def __CreateRecord(self, file_path, record):
        return '<tr><td><a href="{file_name}">{file_name}</a></td><td>{title}</td><td>{content}</td></tr>'.format(file_name=file_path, title=self.__GetLengthStr(record['Title'], 10), content=self.__GetLengthStr(record['Content'], 20))
    
    def __GetLengthStr(self, target, max_len):
        length = max_len
        if len(target) < length: length = len(target)
        return target[:length]
        
