# GUNICORN SETTINGS
loglevel = 'info'
bind = '0.0.0.0:5000'
timeout = 0
workers = 5
worker_class = 'sync'
threads = 1
