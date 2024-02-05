#!/usr/bin/python3
"""Handling the transition between different storage systems, such as FileStorage and DBStorage"""
from os import getenv

storage_engine_type = getenv('HBNB_TYPE_STORAGE')

if storage_engine_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()