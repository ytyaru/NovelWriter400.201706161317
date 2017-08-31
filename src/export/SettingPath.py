import os.path
class SettingPath:
    def __init__(self, base_path=None):
        self.__paths = []
        self.__SetBasePath(base_path)

    def Load(self):
        self.__paths.clear()
        with open('./setting/path.txt') as f:
            for line in f:
                line = line.rstrip('\r\n')
                line = line.rstrip('\r')
                line = line.rstrip('\n')
                if 0 == len(line.strip()):
                    continue
                if '#' == line[0]:
                    continue
                path = self.__RelToAbs(line)
                if not os.path.isdir(path): os.makedirs(path, exist_ok=True)
                self.__paths.append(path)
        return self.__paths
    
    def __RelToAbs(self, path):
        if not os.path.isabs(path):
            # ./
            if path.startswith('./'):
                return os.path.join(self.__base_path, path[2:])
            # ../../../
            abs_path = self.__base_path
            rel_path = path
            while rel_path.startswith('../'):
                rel_path = rel_path[3:]
                abs_path = os.path.dirname(abs_path)
            return os.path.join(abs_path, rel_path)
        return path
    
    def __SetBasePath(self, base_path):
        if base_path:
            self.__base_path = base_path
        else:
            self.__base_path = os.path.dirname(os.path.abspath( __file__ ))

