import os

# 创建日志目录
LOG_DIR = "./logs"

# 日志配置字典
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)d] - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '[%(levelname)s] - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        },
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOG_DIR, 'debug.log'),
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
            'encoding': 'utf-8'
        },   
        'file_info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOG_DIR, 'app.log'),
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
            'encoding': 'utf-8'
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
            'encoding': 'utf-8'
        }
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['console', 'file_info', 'file_error'],
            'level': 'INFO',
            'propagate': False
        },
        'app_log': {
            'handlers': ['console', 'file_info'],
            'level': 'INFO',
            'propagate': False
        },
        'tortoise.db_client': {
            'handlers': ['file_debug'],
            'level': 'DEBUG',
            'propagate': False
        },
        'tortoise': {
            'handlers': ['file_debug'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}