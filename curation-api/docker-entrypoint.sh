#!/bin/bash
set -e
# This entrypoint is used to play nicely with the current cookiecutter configuration.
# Since docker-compose relies heavily on environment variables itself for configuration, we'd have to define multiple
# environment variables just to support cookiecutter out of the box. That makes no sense, so this little entrypoint
# does all this for us.

# the official postgres image uses 'postgres' as default user if not set explictly.
if [ -z "$POSTGRES_USER" ]; then
    export POSTGRES_USER=postgres
fi

export DATABASE_URL=postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB

export SKIP_DB_STATUS_CHECK=0

function postgres_ready(){
  python checkdb.py
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "connected to postgres://$POSTGRES_USER:<password>@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB"

echo "***Preparing schema migrations***"
python manage.py makemigrations --noinput
echo "***Running schema migrations***"
python manage.py migrate --noinput

exec "$@"
