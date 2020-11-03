#!/usr/bin/python3
"""
Actualización models/__init__.py:
para crear una FileStorageinstancia única para su aplicación
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
