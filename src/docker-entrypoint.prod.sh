#!/bin/bash
# $0 is a script name, $1, $2, $3 etc are passed arguments
# $1 is our command
# Credits: https://rock-it.pl/how-to-write-excellent-dockerfiles/

wait_for_db () {
    # Wait until postgres is ready
    until nc -z $DB_HOST 5432; do
        echo "$(date) - waiting for postgres... ($DB_HOST:5432)"
        sleep 3
    done
}

setup_django () {
    echo Running migrations
    python manage.py migrate --noinput
    
    echo Create dummy user if none exists
    python manage.py create_superuser_if_none_exists --user=admin --password=admin
    
    echo Collecting static-files
    python manage.py collectstatic --noinput

    echo Create cache table
    python manage.py createcachetable
}

echo Starting ssh service
/usr/sbin/sshd
eval $(printenv | sed -n "s/^\([^=]\+\)=\(.*\)$/export \1=\2/p" | sed 's/"/\\\"/g' | sed '/=/s//="/' | sed 's/$/"/' >> /etc/profile)

wait_for_db
setup_django

echo Starting using gunicorn
exec gunicorn pipit.wsgi:application --bind 0.0.0.0:8000 --workers 3
