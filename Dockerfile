FROM python:latest

RUN pip install pytest pytest-cov

CMD [ "sleep", "infinity" ]