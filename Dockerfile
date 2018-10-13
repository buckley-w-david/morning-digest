FROM python:3.7-alpine as env

FROM env as build

RUN apk add curl

# Currently a bug in pip 18.1 preventing poetry install
# https://github.com/pypa/pip/issues/5868
RUN pip install --upgrade pip==10.0.1

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

COPY . /opt/morning-digest
WORKDIR /opt/morning-digest

RUN poetry build -f wheel

FROM env as run

COPY --from=build /opt/morning-digest/dist/* /packages/
RUN apk add build-base && pip install /packages/* && rm -rf /packages/ && apk del build-base && apk add mutt

COPY scripts /scripts
WORKDIR /scripts
RUN chmod a+x *.sh

CMD ./run.sh
