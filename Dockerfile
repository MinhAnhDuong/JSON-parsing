FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY test.py .
COPY sample-data.json .

CMD [ "python", "./test.py" ]