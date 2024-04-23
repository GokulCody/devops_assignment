import os
import signal
import sys
import re
import time
import logging
from logging.handlers import RotatingFileHandler

class CustomLogger:
    def __init__(self, log_file=None, log_level=logging.DEBUG, log_format='%(asctime)s - %(levelname)s - %(message)s', max_bytes=10485760, backup_count=5):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        formatter = logging.Formatter(log_format)

        if log_file:
            self.log_file = log_file
        else:
            script_name = os.path.basename(sys.argv[0])
            self.log_file = f"{os.path.splitext(script_name)[0]}.log"

        file_handler = RotatingFileHandler(self.log_file, maxBytes=max_bytes, backupCount=backup_count)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_critical(self, message):
        self.logger.critical(message)

    def monitor_log(self, log_file=None):
        if log_file:
            self.log_file = log_file
        self.log_info("Monitoring log file: {}".format(self.log_file))
        try:
            with open(self.log_file, "r") as file:
                file.seek(0, os.SEEK_END)
                while True:
                    line = file.readline()
                    if line:
                        self.analyze_log(line)
                    else:
                        time.sleep(0.1)
        except KeyboardInterrupt:
            self.log_info("Monitoring stopped.")
        except Exception as e:
            self.log_error("An error occurred: {}".format(e))

    def analyze_log(self, line):
        keywords = ["error", "warning", "exception"]  # Add more keywords as needed
        for keyword in keywords:
            if re.search(keyword, line, re.IGNORECASE):
                self.log_warning("Found '{}' in log: {}".format(keyword, line.strip()))



