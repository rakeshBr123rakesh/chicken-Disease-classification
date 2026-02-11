import logging
import os
import sys

# Log format
LOG_FORMAT = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Create logs directory
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "running_logs.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create logger object
logger = logging.getLogger("cnnClassifier")
