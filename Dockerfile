FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
EXPOSE 3306

ENV FLASK_APP=main.py

CMD [ "flask","run" ]