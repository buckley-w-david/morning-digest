FROM 3.7-alpine as env
FROM env as build

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

COPY . /opt/morning-digest
WORKDIR /opt/morning-digest

RUN poetry build -f wheel

FROM env as run

COPY --from=build /opt/morning-digest/dist/* /packages/morning-digest.whl
COPY scripts /scripts
WORKDIR /scripts

RUN pip install /install/morning-digest.whl && rm -rf /packages

CMD ./run.sh
