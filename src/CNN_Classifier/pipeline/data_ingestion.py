from CNN_Classifier.components.data_ingestion import DataIngestion
from CNN_Classifier.config.configation import ConfigurationManager
from CNN_Classifier import logger




logger.info("Data Ingestion Stage Started")

config = ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config()

data_ingestion = DataIngestion(config=data_ingestion_config)

data_ingestion.download_file()

data_ingestion.unzip_and_clean()


logger.info("Data Ingestion Stage Complited")