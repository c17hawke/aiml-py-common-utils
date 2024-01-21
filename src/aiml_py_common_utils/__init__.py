import sys
from pathlib import Path
from loguru import logger
import os
from aiml_py_common_utils.common import * # noqa
from dotenv import load_dotenv
from typing import TextIO

load_dotenv()

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
LOG_LOCAL = False
if "LOG_LOCAL" in os.environ:
    LOG_LOCAL = bool(int(os.environ["LOG_LOCAL"]))
log_dir = Path("_logs")
log_filepath = log_dir / "logs.log"

logger.remove()

def _log_to_terminal(sink: TextIO=sys.stdout, level: str="DEBUG", colorize: bool=True) -> None:
    logger.add(
        sink=sink, 
        level=level, 
        colorize=colorize, 
        format=\
            "<cyan>[{time:YYYY-MM-DD HH:mm:ss}</cyan> <level><cyan>{level} {module}.{function}:{line}]:</cyan> {message}</level>") # noqa

def _log_to_local_file(sink: str=str(log_filepath), level: str="DEBUG", rotation: str="20MB") -> None:
    if not LOG_LOCAL:
        return None
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

__version__ = "0.0.3"