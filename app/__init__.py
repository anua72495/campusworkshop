"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7pejhp8u7g2een2o0-a.oregon-postgres.render.com",
        database="todo_fnyl",
        user="root",
        password="Zm4KBJMyWsZ347XMVcI2QoaK7T3VZ73s")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
