# _*_ coding:utf-8 _*_
__author__ = 'caimiao'
__date__ = '15-3-7'

import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, TEXT
from sqlalchemy.orm import relationship
from lib.db import Base

class Order(Base):
    '''
    工单记录表
    '''
    __tablename__ = 'order'

    STATUS_CLOSE    = '0'             # 工单状态： 关闭
    STATUS_OPEN     = '1'           # 工单状态： 流转中

    id = Column(Integer, primary_key=True, autoincrement=True)
    catalog = Column(Integer, nullable=False, default=0)        # 工单类型，普通工单
    create_tm = Column(DateTime, default=datetime.datetime.now())
    locked = Column(Enum('0', '1'))                             # 工单状态，是否被锁定
    lock_user = Column(String(128))                             # 工单的锁定者
    status = Column(Enum('0', '1'))                             # 工单的状态，0：关闭状态， 1：流转状态
    stage = Column(Integer, nullable=False, default=0)          # 工单的阶段，默认0,初始阶段
    flow_times = Column(Integer, default=0)                     # 工单的流转次数
    creator = Column(Integer, nullable=False)                   # 工单的创建者编号

    title = Column(String(64), nullable=False)                  # 工单标题
    account = Column(String(128), nullable=False)               # 用户帐号
    phone = Column(String(20))                                  # 用户电话
    product = Column(Integer, nullable=False)                   # 相关产品
    evt_tm_start = Column(DateTime)                             # 问题开始时间
    evt_tm_end = Column(DateTime)                               # 问题结束时间
    content = Column(TEXT, nullable=False)                      # 工单的内容

    answer_list = relationship('Flows')

class Flows(Base):
    '''
    工单回复表
    '''
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    create_tm = Column(DateTime, default=datetime.datetime.now())
    stage = Column(Integer, nullable=False)
    content = Column(TEXT, nullable=False)
    retention_tm = Column(Integer, default=0)                   # 本阶段滞留时间
    creator = Column(Integer, nullable=False)                   # 流程处理者的编号

