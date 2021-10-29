FROM python:3.8

WORKDIR /

COPY openweather templates main.py LICENSE requirements.txt ./

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "main.py"]