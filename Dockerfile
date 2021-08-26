FROM python:3.9
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY poetry.lock pyproject.toml /code/
RUN pip3 install poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --with-credentials
RUN pip3 install -r requirements.txt
COPY . /code/