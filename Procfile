web: gunicorn fileUpload.wsgi --log-level debug --worker-class gevent -c gunicorn.conf.py --threads=3 --worker-connections=1000 --bind=0.0.0.0 --capture-output 
