import logging
import os
from datetime import datetime

# Create a log file name with timestamp
log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the logs directory path
logs_path=os.path.join(os.getcwd(),"logs", log_file) # log file creation within the current directory
os.makedirs(logs_path, exist_ok=True) # even though there's a folder keep on appending the files inside

# Combine the directory and log file name to get the full log file path
log_file_path=os.path.join(logs_path, log_file)

# Configure the logging
logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, 

)

