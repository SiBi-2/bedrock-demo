import logging
from datetime import datetime
from pathlib import Path

class LoggerConfig:
    def __init__(self, log_level=logging.INFO):
        self.log_level = log_level
        output_dir = Path("logs")
        output_dir.mkdir(parents=True, exist_ok=True)
    
    def setup_logging(self):
        current_date = datetime.now()
        log_directory="./logs/"
        formatted_date = current_date.strftime('%Y%m%d')
        log_filename = f"{log_directory}{formatted_date}.log"
        
        logging.basicConfig(
            level=self.log_level,
            format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
            filename=log_filename,
            filemode='a')
