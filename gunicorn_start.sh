#!/bin/bash

NAME="projeto"                              #Name of the application (*)
DJANGODIR=/home/fabiano/Documentos/projetos/www/html/api-rest-python-servicenet/api             # Django project directory (*)
SOCKFILE=/home/fabiano/Documentos/projetos/www/html/api-rest-python-servicenet/run/gunicorn.sock        # we will communicate using this unix socket (*)
USER=fabiano                                        # the user to run as (*)
GROUP=fabiano                                     # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/fabiano/Documentos/projetos/www/html/api-rest-python-servicenet/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/fabiano/Documentos/projetos/www/html/api-rest-python-servicenet/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE