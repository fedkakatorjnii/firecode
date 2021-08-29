FROM python:3.9.6

# set work directory
WORKDIR /opt/app

# # install dependencies
# RUN apk update && \
#     apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
#             build-base curl-dev geos-dev giflib-dev jpeg-dev \
#             libjpeg-turbo-dev libpng-dev linux-headers postgresql-dev \
#             python2-dev sqlite-dev swig tiff-dev zlib-dev perl-dev\
#             python3-dev expat-dev libxslt-dev freexl-dev musl-dev git \
#             libreoffice py3-unoconv postgresql-dev postgresql postgis \
#             python3 poppler libxml2 libxslt gcc yarn geos expat tar freexl perl py-pip \ proj-dev

# RUN pip3 install --upgrade pip
# RUN pip3 install gunicorn

# RUN pip3 install pipenv virtualenv

RUN python3 -m venv /opt/app/docker_venv