FROM python:3.11-slim

 WORKDIR /opt/sde/spoteng

 ENV PYTHONPATH=/opt/sde

 RUN apt-get update \
     && apt-get -y install libpq-dev gcc \
     && pip install psycopg2

 COPY requirements.txt requirements.txt
 RUN pip3 install -r requirements.txt

 COPY ../.. /opt/sde/spoteng/
 CMD ["python3", "main.py"]
