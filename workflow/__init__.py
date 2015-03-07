# _*_ coding:utf-8 _*_
__author__ = 'caimiao'
__date__ = '2015-03-07'


from flask import Blueprint, request

workflow_app = Blueprint('workflow', __name__, url_prefix='/workflow')

@workflow_app.route('/')
def Index():
    return "Hello world"