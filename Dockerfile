FROM debian:11

WORKDIR /code

RUN apt-get update && apt-get install -y python3-pip

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install -r ./requirements.txt

COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]