from logging_config import get_logger


logger = get_logger()


logger.info("RDRS logging system started")
logger.info("This is a test system event")
logger.error("This is a test error message")


print("Logging test completed successfully")