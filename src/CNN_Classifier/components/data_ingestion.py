import os
import urllib.request as request
from zipfile import ZipFile
from CNN_Classifier import logger
from pathlib import Path
from tqdm import tqdm
from CNN_Classifier.entity.config_entity import DataIngestionConfig
from CNN_Classifier.utils import utils


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config




    def download_file(self):
        logger.info("Trying Downlode File")
        if not os.path.exists(self.config.local_data_file):
            request.urlretrieve(
                url = self.config.Source_URL,
                filename=self.config.local_data_file
            )

        else:
            logger.info("File Already Exixt")

    def get_updated_list_of_files(self,list_of_files):
        return  [f for f in list_of_files if f.endswith("jpg")]



    def preprocess(self,zf,f,working_dir):
        target_filepath = os.path.join(working_dir,f)
        if not os.path.exists(target_filepath):
            zf.extract(f,working_dir)

        

    def unzip_and_clean(self):
        with ZipFile(file=self.config.local_data_file,mode="r") as zf:
            list_fo_file = zf.namelist()
            updated_list_of_file = self.get_updated_list_of_files(list_fo_file)
            for f in tqdm(updated_list_of_file):
                self.preprocess(zf, f, self.config.unzip_dir)


