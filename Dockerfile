FROM python:3

COPY requirements.txt .env /src/
COPY accounts accounts media static db.sqlite3 manage.py /src/

WORKDIR /src

RUN pip3 install -r requirements.txt

CMD ["python","manage.py" , "runserver" , "--host", "0.0.0.0", "--port", "8000"]
