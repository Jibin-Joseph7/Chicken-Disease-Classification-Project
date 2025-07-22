import os
import sys
import logging

logging_str = "[%(asctimes)s]: %(levelname)s: %(module)s: %(message)s]"


log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    Level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamlHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")