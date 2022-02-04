FROM python:3.9
WORKDIR /code
COPY /cloud_project/requirements.txt /code/
RUN apt install libpq-dev
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
COPY /cloud_project/cloud /code/cloud
COPY /cloud_project/myproject /code/myproject
COPY /cloud_project/manage.py .
RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
