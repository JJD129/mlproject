from src.utils import authenticate_kaggle_api

def download_kaggle_dataset(dataset_name, download_path):
    api = authenticate_kaggle_api()
    api.dataset_download_files(dataset_name, path=download_path, unzip=True)
