FROM python:3

RUN python3 -m pip install Flask

COPY app /opt/app
WORKDIR /opt/app
EXPOSE 5000
ENTRYPOINT ["python3", "-u", "app.py"]