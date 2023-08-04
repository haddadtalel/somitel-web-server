from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

mogo_url = os.getenv("MONGO_URI")
db = PyMongo(app)

from webserver import route