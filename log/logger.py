import logging
import logging.config
from config.log_config import LOG_DIR, LOGGING_CONFIG
import os

def setup_logging():
    """初始化日志配置"""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.config.dictConfig(LOGGING_CONFIG)
    
def get_logger(name: str = None):
    """获取日志记录器"""
    return logging.getLogger(name)

# 应用日志配置
setup_logging()

logger = get_logger(__name__)


