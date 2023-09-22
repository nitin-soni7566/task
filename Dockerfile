FROM python:3

COPY requirements.txt .env /src/
COPY app /src/app

WORKDIR /src

RUN pip3 install -r requirements.txt

CMD ["python","manage.py" , "run server" , "--host", "0.0.0.0", "--port", "8000"]
