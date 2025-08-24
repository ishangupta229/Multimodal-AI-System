import logging
from config import LOG_PATH

logging.basicConfig(
    filename=LOG_PATH,
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
