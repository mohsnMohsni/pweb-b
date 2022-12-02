FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install gunicorn==20.1.0
RUN pip install -r requirements/production.txt
COPY . /code/
EXPOSE 8000
HEALTHCHECK --interval=12s --timeout=12s --start-period=5s \
CMD python manage.py test
CMD ["sh", "/code/migrate_run.sh"]
