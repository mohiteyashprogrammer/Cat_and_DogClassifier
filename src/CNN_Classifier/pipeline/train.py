from CNN_Classifier.config.configation import ConfigurationManager
from CNN_Classifier.components.train import Training
from CNN_Classifier import logger
from CNN_Classifier.constants import *
from CNN_Classifier.entity.config_entity import TrainingConfig


try:
    config = ConfigurationManager()
  
    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train()
    
except Exception as e:
    raise e