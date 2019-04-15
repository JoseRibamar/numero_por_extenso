FROM python:3.7.3
COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy
CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]
