from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluvation import ModelEvaluation
from src.datascience import logger



class ModelEvaluvationTrainingPipeline:
    def __init__(self):
        pass


    def initiate_model_evaluvation(self):
        config=ConfigurationManager()
        model_evaluvation_config=config.get_model_evaluation_config()
        model_evaluvation=ModelEvaluation(config=model_evaluvation_config)
        model_evaluvation.log_into_mlflow()
