import flask
import json
import datetime
import logging
from logging.handlers import RotatingFileHandler
import os.path
import src.Database
import src.export.OutputFile
import src.export.OutputListHtml
import src.export.SingleDirectoryExporter

app = flask.Flask(__name__)
db = src.Database.DatabaseAccesser('./src/db/')
__base_path = os.path.dirname(os.path.abspath( __file__ ))
app.logger.setLevel(logging.DEBUG)
debug_file_handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=10)
app.logger.addHandler(debug_file_handler)

@app.route('/')
def index():
    """
    html = ''
    for record in db.Loads():
        app.logger.debug('record: {0}'.format(record))
        html += '<pre title=' + record['Created'] + " " + record['Title'] +  '>' + record['Content'] + '</pre>'
    if '' == html: html = '<pre></pre>'
    return flask.render_template('index.html', archives=flask.Markup(html))
    """
#    exp = src.export.SingleDirectoryExporter.SingleDirectoryExporter(base_path=__base_path)
#    exp.Export()
    return flask.render_template('index.html')

@app.route('/Loads')
def loads():
    return flask.jsonify(json.dumps(db.Loads()))

# DBに登録する。他、settingされたとおりに出力する
@app.route('/Regist', methods=['POST'])
def regist():
    app.logger.debug('regist()')
    app.logger.debug('引数: {0}'.format(flask.request.json))
    record = db.Insert(flask.request.json['Content'], title=flask.request.json['Title'])
    app.logger.debug('戻り値: {0}'.format(record))
    
    __output_file(record)
    return flask.jsonify(json.dumps(record))

# DBにあるデータをすべてファイルに出力する
@app.route('/OutputAll', methods=['POST'])
def output_all():
    for record in db.Loads():
        __output_file(record)

def __output_file(record):
    if os.path.isfile(os.path.join(__base_path, 'setting/path.txt')):
        f = src.export.OutputFile.OutputFile(base_path=__base_path)
        file_name = f.Output(record)
        l = src.export.OutputListHtml.OutputListHtml(base_path=os.path.join(__base_path, 'contents/'))
        l.Output(file_name, record)


if __name__ == '__main__':  
    app.run() # localhost:5000
#    app.run(host="127.0.0.1", port=8080)

