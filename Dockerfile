FROM django

EXPOSE 8000

RUN apt update && apt upgrade -y
RUN pip install -U pip poetry

ADD . /docker_image
WORKDIR /docker_image

ADD poetry.lock pyproject.toml /app/src/
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install --no-deps -r requirements.txt
ADD . /docker_image/

RUN pip install django-tinymce

RUN ls -a

CMD [ "python3", "./manage.py runserver 0.0.0.0:8000" ]