import os
import sys
from mlopsProject.components import data_ingestion

sys.stdout.reconfigure(encoding='utf-8')

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/kjambani/Mlops-end.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="kjambani"
os.environ["MLFLOW_TRACKING_PASSWORD"]="41fd6ac15ed1729eecda790e1bd58ea6d7221984"

from mlopsProject import logger
from mlopsProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlopsProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlopsProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline  
from mlopsProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlopsProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline



STAGE_Name = "Data Ingestion Stage"
try:
    logger.info(f"stage {STAGE_Name}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info("Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_Name = "Data Validation Stage"
try:
    logger.info(f"stage {STAGE_Name}")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info("Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_Name = "Data Transformation Stage"
try:
    logger.info(f"stage {STAGE_Name}")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info("Completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_Name = "Model Training Stage"
try:
    logger.info(f"stage {STAGE_Name}")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info("Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_Name = "Model Evaluation Stage"
try:
    logger.info(f"stage {STAGE_Name}")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info("Completed")
except Exception as e:
    logger.exception(e)
    raise e





