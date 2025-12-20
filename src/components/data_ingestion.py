import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Importing other components (commented out as per your snippet)
# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    """
    Configuration class to store paths for data ingestion artifacts.
    Using dataclass for clean, immutable path definitions.
    """
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        # Initialize the config object to access defined paths
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Method to read data from source and split into Train/Test sets.
        """
        logging.info("Starting Data Ingestion component")
        try:
            # READING DATA SOURCE
            # To switch sources (e.g., SQL, MongoDB, or Cloud Storage), only this section needs modification.
            # Example for SQL: df = pd.read_sql_query(query, connection)
            # Example for MongoDB: df = pd.DataFrame(list(collection.find())
            # Reading the dataset from the local notebook folder
            # Note: Ensure the path 'notebook/data/stud.csv' is correct relative to root
            df = pd.read_csv(os.path.join('notebook', 'data', 'stud.csv'))
            logging.info('Successfully read the dataset as a DataFrame')

            # Create 'artifacts' directory if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            logging.info(f"Ensured directory exists: {os.path.dirname(self.ingestion_config.train_data_path)}")

            # Save the raw dataset into the artifacts folder
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Raw data saved at: {self.ingestion_config.raw_data_path}")

            # Perform Train-Test Split (80% Train, 20% Test)
            logging.info("Initiating Train-Test split")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save split datasets to CSV files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info(f"Train data saved at: {self.ingestion_config.train_data_path}")
            logging.info(f"Test data saved at: {self.ingestion_config.test_data_path}")
            logging.info("Data Ingestion process completed successfully")

            # Return paths for the next component (Data Transformation)
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            # Logging error before raising custom exception
            logging.error(f"Error occurred in Data Ingestion: {str(e)}")
            raise CustomException(e, sys)
        

        
if __name__=="__main__":
    # Execution block for testing the component independently
    obj=DataIngestion()
    obj.initiate_data_ingestion()