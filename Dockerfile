FROM python:3.8.5
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]