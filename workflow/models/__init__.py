# _*_ coding:utf-8 _*_
__author__ = 'caimiao'
__date__ = '15-3-7'

import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from lib.db import Base

class Order(Base):
    '''
    工单记录表
    '''
    __tablename__ = 'order'

    STATUS_CLOSE  = '0'             # 工单状态： 关闭
    STATUS_OPEN     = '1'           # 工单状态： 流转中

    id = Column(Integer, primary_key=True, autoincrement=True)
    catalog = Column(Integer, nullable=False, default=0)        # 工单类型，普通工单
    create_tm = Column(DateTime, default=datetime.datetime.now())
    locked = Column(Enum('0', '1'))                             # 工单状态，是否被锁定
    lock_user = Column(String(128))                             # 工单的锁定者
    status = Column(Enum('0', '1'))                             # 工单的状态，0：关闭状态， 1：流转状态
    stage = Column(Integer, nullable=False, default=0)          # 工单的阶段，默认0,初始阶段
    flow_times = Column(Integer, default=0)                     # 工单的流转次数

    answer_list = relationship('Answer')

class Answer(Base):
    '''
    工单回复表
    '''
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    create_tm = Column(DateTime, default=datetime.datetime.now())

