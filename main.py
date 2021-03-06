# _*_ coding:utf-8 _*_

__author__ = 'caimiao'
__date__ = '2015-03-03'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, session
from config import DevConfig as global_settings
from lib.site.server_session import RedisSessionInterface

# 导入应用
from workflow import workflow_app

app = Flask(__name__)

app.register_blueprint(workflow_app)

app.session_interface = RedisSessionInterface()

@app.route('/')
def hello_world():
    print(app.config)
    if not session.get('name', None):
        session['name'] = 'caimmy'
    else:
        print(session.get('name'))
        return "sessioned : " + str(session.get('name'))

    return '阿三服阿斯顿服'

@app.errorhandler(404)
def test_404(error):
    print(app.config)
    return '<h1>404 occured</h1><br />%s' % (str(error)), 404

app.config.from_object(global_settings)
app.run(host='0.0.0.0', port=5000)
# app.run()