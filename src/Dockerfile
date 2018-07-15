FROM python:3.6-alpine3.6
RUN apk add --no-cache libxml2-dev libxslt-dev build-base
ADD requirements.txt /
RUN python -m pip install -r /requirements.txt
RUN apk del build-base
ADD . /comicbot/
WORKDIR /comicbot
CMD ["python","comic_bot.py"]