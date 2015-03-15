#_*_ coding:utf-8 _*_

__author__ = 'caimiao'
__date__ = '2015-03-03'

"""
应用的静态配置
"""

"""
wrong configuration may lead the server to respond 404 to any request.
"""
class Config:
    DEBUG = False
    # SERVER_NAME = 'BRONZE_CRM 0.1'
    SECRET_KEY = '!#\xa6\xc4\xab\xe2\xcd\xa0X\x11\xe27W\x01\xb8~E\xf0\xea\x9f\xd6d\xcc\x9e'

class DevConfig(Config):
    DEBUG = True

# the following type of configuration not working
global_settings = {
    'DEBUG': True,
    'SERVER_NAME': 'BRONZE_CRM 0.1',
    'SECRET_KEY': '!#\xa6\xc4\xab\xe2\xcd\xa0X\x11\xe27W\x01\xb8~E\xf0\xea\x9f\xd6d\xcc\x9e'
}

db_config = {
    'MASTER_HOST': '127.0.0.1',
    'SLAVE_HOST': '127.0.0.1',
    'PORT': 3306,
    'USER': 'root',
    'PASSWD': 'abcd1234',
    'DB_NAME': 'bronze_crm'
}