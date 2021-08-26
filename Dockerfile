FROM python:3
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY poetry.lock /code/
COPY pyproject.toml /code/
RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --with-credentials
RUN pip install -r requirements.txt
COPY . /code/