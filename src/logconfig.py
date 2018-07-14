import logging, coloredlogs, logging.config

class logger:
    def __init__(self, logger_name, log_file):
        self.name = logger_name
        self.file = log_file
        logging.config.dictConfig(
            {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'json': {
                    'format': '[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                    'class': 'pythonjsonlogger.jsonlogger.JsonFormatter'
                },
                'console':{
                    'format':'[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                    'class':'pythonjsonlogger.jsonlogger.JsonFormatter'
                }
            },
            'handlers': {
                'json': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'json'

                },
                'console':{
                    'class': 'logging.FileHandler',
                    'formatter': 'console',
                    'filename': self.file
                }
            },
            'loggers': {
                '': {
                    'handlers': ['json', 'console'],
                    'level': logging.DEBUG
                }
            }
        }
        )
        self.log = logging.getLogger(logger_name)
        coloredlogs.install(level='DEBUG',logger=self.log)