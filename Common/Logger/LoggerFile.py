import logging
from Common.Variables.Variables import ProjectVariables



class LoggerClass():
    def __init__(self):
        var = ProjectVariables()
        pjRoot = var.get_project_root()
        self.loggerFilePath = pjRoot + "/Common/_trash/logger.log"


    def add_log(self,level,message):
        logging.basicConfig(level=logging.INFO, filename=self.loggerFilePath, filemode="a",
                            format="%(asctime)-12s %(levelname)s %(message)s",
                            datefmt="%d-%m-%Y %H:%M:%S")
        if level == "INFO":
            logging.info(message)
            return
        if level == "DEBUG":
            logging.debug(message)
            return
        if level == "WARNING":
            logging.warning(message)
            return
        if level == "ERROR":
            logging.error(message)
            return
        if level == "CRITICAL":
            logging.critical(message)
            return



