FROM python:3.7
RUN mkdir /app
WORKDIR /app/
ADD . /app/
RUN pip install -r requirements.txt
EXPOSE 90
CMD ["flask","run","--host=0.0.0.0"]
