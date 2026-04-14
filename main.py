from mlopsProject.components import data_ingestion
from mlopsProject import logger
from mlopsProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_Name = "Data Ingestion Stage"
try:
    logger.info(f"stage {STAGE_Name}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info("Completed")
except Exception as e:
    logger.exception(e)
    raise e
    




