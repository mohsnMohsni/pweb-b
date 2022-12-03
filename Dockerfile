FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements ./requirements

RUN pip install --upgrade pip --no-warn-script-location; pip install wheel
RUN pip install -r requirements/production.txt --user --no-warn-script-location
RUN pip install gunicorn==20.1.0

COPY . .

EXPOSE 8000

RUN export DJANGO_ENV=production

ENTRYPOINT ["/app/entrypoint.sh"]
