FROM python:3.6-slim
RUN mkdir /neighbor
WORKDIR /neighbor
ADD requirements.txt /neighbor/
RUN pip install -Ur requirements.txt
ADD . /neighbor/