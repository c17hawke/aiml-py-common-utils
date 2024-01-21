import sys
from pathlib import Path
from loguru import logger

###################################################################
# logging configuration
# --------------------------
# DEBUG: if True then it set logging level to DEBUG
# LOG_LOCAL: if True then it save logs to a local file 
#            including standard terminal output
# log_dir: the directory where log files are saved
# log_filepath: the path where log files are saved
###################################################################

DEBUG = True
TERMINAL = False
log_dir = Path("logs")
log_filepath = log_dir / "logs.log"

logger.remove()

def _log_to_terminal(sink=sys.stdout, level="DEBUG", colorize=True):
    logger.add(
        sink=sink, 
        level=level, 
        colorize=colorize, 
        format=\
            "<cyan>[{time:YYYY-MM-DD HH:mm:ss}</cyan> <level><cyan>{level} {module}.{function}:{line}]:</cyan> {message}</level>") # noqa

def _log_to_local_file(sink=str(log_filepath), level="DEBUG", rotation="20MB"):
    logger.add(
        sink=sink, 
        level=level, 
        rotation=rotation, 
        format=\
            "<cyan>[{time:YYYY-MM-DD HH:mm:ss}</cyan> <level><cyan>{level} {module}.{function}:{line}]:</cyan> {message}</level>") # noqa

if DEBUG:
    if TERMINAL:
        LEVEL = "DEBUG"
        _log_to_terminal(sink=sys.stdout, level=LEVEL, colorize=True)
        _log_to_local_file(sink=str(log_filepath), level=LEVEL, rotation="200MB")
    else:
        _log_to_terminal(sink=sys.stdout, level="INFO", colorize=True)
        _log_to_local_file(sink=str(log_filepath), level="DEBUG", rotation="200MB")
else:
    _log_to_terminal(sink=sys.stdout, level="INFO", colorize=True)
    _log_to_local_file(sink=str(log_filepath), level="DEBUG", rotation="200MB")


logger = logger.bind(zignal_logger=True)

__version__ = "0.0.1"