from CNN_Classifier.config.configation import ConfigurationManager
from CNN_Classifier.components.evaluation import Evaluation
from CNN_Classifier import logger




try:
    config = ConfigurationManager()
    val_config = config.get_validation_config()
    evaluation = Evaluation(val_config)
    evaluation.evaluation()
    evaluation.save_score()
except Exception as e:
   raise e