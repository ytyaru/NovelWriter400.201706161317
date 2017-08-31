import os.path
import src.export.Exporter
import src.export.OutputListFile
import src.export.OutputListHtml
class SingleDirectoryExporter(src.export.Exporter.Exporter):
    def __init__(self, base_path=None, file_name_format=None):
        super().__init__(base_path=base_path, file_name_format=file_name_format)
    
    """
    ファイル出力する。
    is_overwrite: 上書きするか否か
    """
    def Export(self, is_overwrite=False):
        for record in super().Database.Loads():
            file_name = super().FilenameCreater.Create(record)
            for path in super().SettingPath.Load():
                file_path = os.path.join(path, file_name)
                print(file_path)
                if os.path.isfile(file_path) and not(is_overwrite): continue
                super().FileWriter.Write(file_path, record)
                list_file = src.export.OutputListFile.OutputListFile(path)
                list_file.Output(file_name, record)
                list_html = src.export.OutputListHtml.OutputListHtml(path)
                list_html.Output(file_name, record)
