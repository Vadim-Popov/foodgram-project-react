FROM python:3.11.4-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install gunicorn==20.1.0
RUN pip install -r requirements.txt --no-cache-dir
COPY . ./
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0.0.0.0:8000" ]
