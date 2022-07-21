FROM python:3.10

COPY requirements.txt .

RUN pip freeze > requirements.txt

RUN pip install -r requirements.txt

RUN pip install git+https://github.com/Pycord-Development/pycord

RUN pip install python-dotenv

RUN pip install PyDictionary --use-deprecated=backtrack-on-build-failures

RUN pip install python-gist

COPY . .

EXPOSE 1337

USER 1000

CMD [ "python3", "Scrybe-2/bot.py" ]
