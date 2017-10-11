FROM python:3.5.2

ENV PYTHONUNBUFFERED 1

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./curation-api/requirements /requirements

RUN pip install -r /requirements/production.txt

COPY ./curation-api/docker-entrypoint.sh /docker-entrypoint.sh
COPY ./curation-api/start.sh /start.sh
COPY ./curation-api/tests.sh /tests.sh

RUN sed -i 's/\r//' /start.sh \
    && chmod +x /start.sh \
    && sed -i 's/\r//' /docker-entrypoint.sh \
    && chmod +x /docker-entrypoint.sh \
    && sed -i 's/\r//' /tests.sh \
    && chmod +x /tests.sh

COPY . /usr/src/app/

EXPOSE 5000

WORKDIR /usr/src/app/curation-api/

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/start.sh"]