# -*- coding: utf-8 -*-

import asyncio,logging

import aiomsql

def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomsql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port',3306),
        user=kw['user'],
        password=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )
