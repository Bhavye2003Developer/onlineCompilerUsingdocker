FROM ubuntu

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y g++

WORKDIR /usr/share/myfile/

COPY c++Code.cpp .

CMD g++ c++Code.cpp; ./a.out