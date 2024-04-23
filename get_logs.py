from custom_logger import CustomLogger 
import random
import time

logger = CustomLogger()
log_levels = ["INFO","DEBUG","WARNING","ERROR","CRITICAL"]
while True:
    try:
    # Randomly select a log level
        log_level = random.choice(log_levels)
        if log_level == "INFO":
            logger.log_info("Logging info")
        if log_level == "DEBUG":
            logger.log_debug("Logging debug")
        if log_level == "WARNING":
            logger.log_warning("Logging warning")
        if log_level == "ERROR":
            logger.log_error("Logging error")
        if log_level == "CRITICAL":
            logger.log_info("Logging critical")
        time.sleep(1)
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        logger.log_info("\nLogging interrupted. Exiting.")
        break