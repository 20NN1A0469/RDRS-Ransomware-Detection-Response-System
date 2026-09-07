from pathlib import Path
from loguru import logger


# Create logs directory if it doesn't exist
LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)


# Remove Loguru's default logger
logger.remove()


# System log
logger.add(
    "logs/system.log",
    rotation="10 MB",
    retention="7 days",
    level="INFO"
)


# Error log
logger.add(
    "logs/errors.log",
    rotation="10 MB",
    retention="7 days",
    level="ERROR"
)


def get_logger():
    return logger