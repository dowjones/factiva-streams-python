import os
# import sys
import logging


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
log_path = os.path.join(BASE_DIR, 'logs')
articles_path = os.path.join(BASE_DIR, 'articles')
logging.basicConfig(level=logging.INFO)
# TODO: Create a mechanism for each component to contribute to the same log file
logger = logging.getLogger('Component')

print("Will log to: {}".format(log_path))
print("Will save articles to {}".format(articles_path))

if not os.path.exists(log_path):
    os.mkdir(log_path)

if not os.path.exists(articles_path):
    os.mkdir(articles_path)

fileHandler = logging.FileHandler(os.path.join(log_path, 'factiva-streams-python.log'))

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s] [%(name)s]  %(message)s")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

# consoleHandler = logging.StreamHandler(sys.stdout)
# consoleHandler.setFormatter(logFormatter)
# logger.addHandler(consoleHandler)
