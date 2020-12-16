FROM python:3.9.0

COPY ./*.py ./app/
COPY ./requirements.txt ./app/

WORKDIR ./app

RUN pip install -r requirements.txt

RUN pytest

### Please don't add an entrypoint here, instead use params or kubernetes overrides