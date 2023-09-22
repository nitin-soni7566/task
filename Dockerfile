FROM python:3.9-slim-bullseye

WORKDIR /src

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python app/manage.py runserver  
