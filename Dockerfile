FROM python:3
COPY . /app
WORKDIR /app
RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 5000
CMD python3 ./app.py