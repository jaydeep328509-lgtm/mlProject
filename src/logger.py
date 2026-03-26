import logging
import os
from datetime import datetime

# 1. Define the file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the folder path to sit right next to this script
current_dir = os.path.dirname(os.path.abspath(__file__))
logs_path = os.path.join(current_dir, "logs") 
os.makedirs(logs_path, exist_ok=True) 

# 3. Combine folder + file name
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# 4. Configure logging to handle BOTH File and Terminal (Stream)
logging.basicConfig(
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH), # Saves logs to the file
        logging.StreamHandler()             # Prints logs to the terminal
    ],
    force=True # Ensures old configs from other scripts/notebooks don't interfere
)

if __name__ == "__main__":
    logging.info("Logging has started successfully!")