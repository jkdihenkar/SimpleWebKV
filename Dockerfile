FROM python:3.9.0

EXPOSE 5000

COPY ./*.py ./app/
COPY ./requirements.txt ./app/

WORKDIR ./app

RUN pip install -r requirements.txt

RUN pytest

ENTRYPOINT [ "python" ]
CMD [ "./simplekv_server.py" ]