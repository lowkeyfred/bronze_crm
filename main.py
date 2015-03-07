# _*_ coding:utf-8 _*_

__author__ = 'caimiao'
__date__ = '2015-03-03'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
from config import global_settings

# 导入应用
from workflow import workflow_app

app = Flask(__name__)
app.register_blueprint(workflow_app)

@app.route('/')
def hello_world():
    print(app.config)
    return '阿三服阿斯顿服'

@app.errorhandler(404)
def test_404(error):
    print(app.config)
    return '<h1>404 occur</h1><br />%s' % (str(error)), 404

app.config.from_object(global_settings)
app.run(host='0.0.0.0', port=5000)