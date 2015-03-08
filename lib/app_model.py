# _*_ coding:utf-8 _*_
__author__ = 'caimiao'
__date__ = '15-3-7'

import datetime
from sqlalchemy import Column, Integer, String, DateTime, Enum
from lib.db import Base

class User(Base):
    '''
    用户帐号表
    '''
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    email = Column(String(128), nullable=False)
    passwd = Column(String(32), default='')
    phone = Column(String(20))
    avatar = Column(String(256))        # 头像
    status = Column(Enum('0', '1'))     # 帐号状态 0：禁用；1：可用；
    create_tm = Column(DateTime, default=datetime.datetime.now())


class Department(Base):
    '''
    部门表
    '''
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    about = Column(String(1024))
    status = Column(Enum('0', '1'), default='1')      # 可用
    belong_product = Column(Integer, default=0)       # 所属产品，默认为全产品线部门


class Product(Base):
    '''
    产品表
    '''
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    about = Column(String(1024))
    status = Column(Enum('0', '1'), default='1')        # 可用