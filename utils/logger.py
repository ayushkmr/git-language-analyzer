import logging

class Logger:
    def __init__(self):
        logging.basicConfig(filename='git_language_analyzer.log', level=logging.ERROR,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def error(self, message):
        logging.error(message)

    def info(self, message):
        logging.info(message)