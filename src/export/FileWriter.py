class FileWriter:
    def __init__(self):
        pass
    def Write(self, path, record):
        with open(path, 'w') as f:
            if None is not record['Title'] and 0 != len(record['Title']):
                f.write(record['Title'])
                f.write('\n\n')
            f.write(record['Content'])
