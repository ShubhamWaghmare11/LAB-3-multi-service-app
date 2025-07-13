import logging
import time

log_file = "/logs/logger.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


while True:
    time.sleep(1)
    logging.info("Logger service is active")