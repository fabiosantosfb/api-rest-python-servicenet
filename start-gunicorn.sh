#!/usr/bin/env bash

set -e
APP_NAME='api'
APP_PATH=/home/fabiano/Documentos/projetos/www/html/api-rest-python-servicenet
ENV_PATH=$APP_PATH/venv
LOGFILE="$APP_PATH/logs/gunicorn-log"
NUM_WORKERS=2

USER=fabiano

PORT=8007

echo "Starting $APP_NAME as `whoami`"

source $ENV_PATH/bin/activate
cd "$APP_PATH/"

exec gunicorn -w $NUM_WORKERS -b "127.0.0.1:$PORT" --user=$USER --log-level=debug --log-file=$LOGFILE 2>>$LOGFILE "$APP_NAME.wsgi:application"