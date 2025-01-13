import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import authenticate_kaggle_api
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
# from src.components.data_transformation import DataTransformation, DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifact', 'train.csv')
    test_data_path: str=os.path.join('artifact', 'test.csv')
    raw_data_path: str=os.path.join('artifact', 'StudentsPerformance.csv')
    dataset_name: str="spscientist/students-performance-in-exams" 
    download_path: str="./artifact"

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Start Data Ingestion Process')
        try:
            # download data from kaggle
            logging.info(f"Downloading dataset {self.ingestion_config.dataset_name} to {self.ingestion_config.download_path}")
            api = authenticate_kaggle_api()
            api.dataset_download_files(
                self.ingestion_config.dataset_name, 
                path=self.ingestion_config.download_path, 
                unzip=True
            )
            logging.info(f"Dataset downloaded and extracted to {self.ingestion_config.download_path}")

            # load data
            if not os.path.exists(self.ingestion_config.raw_data_path):
                raise FileExistsError(f"Expected data file not found at {self.ingestion_config.raw_data_path}")
            df = pd.read_csv(self.ingestion_config.raw_data_path)
            logging.info('loaded raw data into dataframe')

            # save raw data inot the configured path
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info(f"Raw data saved at {self.ingestion_config.raw_data_path}")

            # split data into train and test sets
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
            train_df.to_csv(self.ingestion_config.train_data_path, index=False)
            logging.info(f"Train data saved at {self.ingestion_config.train_data_path}")
            test_df.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info(f"Test data saved at {self.ingestion_config.test_data_path}")

            logging.info("Data ingestion completed successfully")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
        except Exception as e:
            logging.error("Error occured during data ingestion")
            raise CustomException(e, sys)

# if __name__=="__main__":
#     obj=DataIngestion()
#     train_data,test_data=obj.initiate_data_ingestion()

#     data_transformation=DataTransformation()
#     data_transformation.initiate_data_transformation(train_data,test_data)