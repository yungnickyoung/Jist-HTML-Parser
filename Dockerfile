FROM python:3

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD [ "python", "main.py" ]
