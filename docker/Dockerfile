FROM python:3.5
RUN apt-get -y update

RUN apt-get install -y libpq-dev
ENV PYTHONIOENCODING=UTF-8
RUN apt-get install -y postgresql-client
RUN apt-get install -y build-essential
RUN mkdir /code
RUN mkdir /static
RUN mkdir /static_tel
WORKDIR /code

COPY requirement.txt /code/requirement.txt
RUN pip install -U pip
RUN pip install -r requirement.txt
COPY last_requirement.txt /code/last_requirement.txt
RUN pip install -r last_requirement.txt
EXPOSE 8010



