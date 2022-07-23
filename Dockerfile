FROM python:3
COPY requirements.txt .
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt
RUN pip install python-dotenv
RUN pip install PyDictionary --use-deprecated=backtrack-on-build-failures
RUN python3 -m pip install git+https://github.com/Pycord-Development/pycord
RUN cd .
COPY . .
USER 1000
CMD [ "python3", "bot.py" ]