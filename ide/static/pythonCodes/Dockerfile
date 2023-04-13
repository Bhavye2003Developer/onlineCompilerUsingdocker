FROM ubuntu

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y python3

WORKDIR /usr/share/myfile/

COPY pyCode.py .

CMD ["python3" ,"pyCode.py"]