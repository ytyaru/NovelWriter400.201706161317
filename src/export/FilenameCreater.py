import datetime
import re
class FilenameCreater:
    def __init__(self, format=None):
        self.__re_created = re.compile(r'{created}', re.IGNORECASE)
        self.__re_title = re.compile(r'{title}', re.IGNORECASE)
        self.__re_title_pre = re.compile(r'{title:[-+]?\d+}', re.IGNORECASE)
        self.__re_content_pre = re.compile(r'{content:[-+]?\d+}', re.IGNORECASE)
        self.__format = format

    def Create(self, record, format=None):
        d = datetime.datetime.strptime(record['Created'], '%Y-%m-%d %H:%M:%S')
        dtstr = '{0:%Y%m%d%H%M%S}'.format(d)
        if None is self.__format and None is format: return dtstr + '.txt'
        if None is format: format = self.__format
        file_name = format
        file_name = re.sub(self.__re_created, dtstr, file_name)
        file_name = re.sub(self.__re_title, record['Title'], file_name)
        file_name = self.__LengthStr(self.__re_title_pre, file_name, record['Title'])
        file_name = self.__LengthStr(self.__re_content_pre, file_name, record['Content'])
        return file_name

    def __LengthStr(self, find_reg, file_name, record_value):
        for match in re.findall(find_reg, file_name):
            str_len = int(match.split(':')[1][:-1])
            if len(record_value) < str_len:
                str_len = len(record_value)
            file_name = file_name.replace(match, record_value[:str_len])
        return file_name

"""
if __name__ == '__main__':
    c = FilenameCreater()
    file_name = c.Create({'Title': 'タイトル', 'Content': '本文ですよ。', 'Created': '2017-01-02 12:34:56'}, format='{created}_{title:10}_{content:20}.txt')
    print(file_name)
    file_name = c.Create({'Title': 'とってもかなり超長いタイトル', 'Content': 'それなりにだいぶわりと長い少なくとも20文字以上はある本文ですよ。', 'Created': '2017-01-02 12:34:56'}, format='{created}_{title:10}_{content:20}.txt')
    print(file_name)
    file_name = c.Create({'Title': 'とってもかなり超長いタイトル', 'Content': 'それなりにだいぶわりと長い少なくとも20文字以上はある本文ですよ。', 'Created': '2017-01-02 12:34:56'}, format='{created}_{title}_{content:20}.txt')
    print(file_name)
    file_name = c.Create({'Title': 'とってもかなり超長いタイトル', 'Content': 'それなりにだいぶわりと長い少なくとも20文字以上はある本文ですよ。', 'Created': '2017-01-02 12:34:56'}, format='{title}.txt')
    print(file_name)
    file_name = c.Create({'Title': 'とってもかなり超長いタイトル', 'Content': 'それなりにだいぶわりと長い少なくとも20文字以上はある本文ですよ。', 'Created': '2017-01-02 12:34:56'})
    print(file_name)
"""
