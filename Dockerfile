FROM python:latest

RUN pip install pytest pytest-cov "radon>=5.1,<6"

CMD [ "sleep", "infinity" ]