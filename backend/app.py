from flask import Flask
import logging


app = Flask(__name__)

logger = logging.getLogger("mylogger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("backend.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

@app.route("/")
def home():
    logger.info("Logging Here")
    return "Working"


if __name__ == "__main__":
    app.run(debug=True)