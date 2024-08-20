import logging
import os


class SingletonLogger:
    _instance = None

    def __new__(cls, log_file='app.log'):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
            cls._instance._init_logger(log_file)
        return cls._instance

    def _init_logger(self, log_file):
        self.logger = logging.getLogger('app_logger')

        # Define the project root directory
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'twitch'))
        log_file_path = os.path.join(project_root, log_file)
        print(f"Calculated log file path: {log_file_path}")

        print("Setting up logger handlers.")
        self.logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        fh = logging.FileHandler(log_file_path, mode='w')
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        self.logger.addHandler(ch)
        self.logger.addHandler(fh)
        print("Logger handlers added.")
        for handler in self.logger.handlers:
            print(f"Handler: {handler}, Level: {handler.level}, Formatter: {handler.formatter}")

    def get_logger(self):
        return self.logger


def configure_logging():
    logger_instance = SingletonLogger()
    return logger_instance.get_logger()
