FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install pipenv
RUN pipenv install
RUN chmod +x manage.py
RUN pipenv run python manage.py makemigrations
RUN pipenv run python manage.py migrate
EXPOSE 8000
CMD pipenv run python manage.py runserver 0.0.0.0:8000