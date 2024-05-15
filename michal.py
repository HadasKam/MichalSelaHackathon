from dotenv import load_dotenv
from pprint import pprint
import requests
import os


load_dotenv()

def g(age):
    if age<15:
        