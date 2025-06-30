import multiprocessing

workders = multiprocessing.cpu_count() * 2 + 1
bind = "0.0.0.0:8000"
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"