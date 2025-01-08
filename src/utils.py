import os
from kaggle.api.kaggle_api_extended import KaggleApi

def authenticate_kaggle_api():
    api = KaggleApi()
    api.authenticate()
    return api
