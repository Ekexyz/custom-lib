from robot.api import logger

class Test():
    def __init__(self):
        pass

    def custom_log(self, message):
        logger.console(f"Logging to console from custom_log, msg:\n{message}")
        logger.info(f"Logging to info level from custom_log, msg:\n{message}")
        logger.trace(f"Logging to trace level from custom_log, msg:\n{message}")
