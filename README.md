# curation app

## Create env file

* create a file with all the necessary environment variables. 

    sample: `.env_dev`

## Running application locally

* Build the curation-web (React SPA) application
    
    `docker-compose -f dev.yml build curation-web`

* Extract static files for React SPA

    `docker-compose -f dev.yml run curation-web`

* Build the django app server

    `docker-compose -f dev.yml build app`

* Run postgres db service 

    `docker-compose -f dev.yml up -d postgres`

* Run the django app server 

    `docker-compose -f dev.yml up app`

## Run tests

* Build the curation-web (React SPA) application

    `docker-compose -f docker-compose-travis.yml build curation-web`

* Run tests in curation-web (React SPA) application

    `docker-compose -f docker-compose-travis.yml run curation-web`

* Build the django app server

    `docker-compose -f docker-compose-travis.yml build app`

* Run the django app tests

    `docker-compose -f docker-compose-travis.yml run app`
