from CNN_Classifier.config.configation import ConfigurationManager
from CNN_Classifier.components.prepare_base_moel import PrepareBaseModel
from CNN_Classifier.constants import *
from CNN_Classifier import logger


try:
    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()
except Exception as e:
    raise e


