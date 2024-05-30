FROM python:3.9

RUN apt-get update && apt-get install -y cron
RUN apt-get install -y nano
RUN pip install pandas

WORKDIR /01

ADD ./src/countdown.py .
ADD ./src/shell_file.sh .

RUN chmod +x shell_file.sh
COPY crontab /etc/cron.d/mycron

RUN chmod 0644 /etc/cron.d/mycron
# RUN crontab /etc/cron.d/mycron
RUN mkdir -p /var/log && touch /var/log/cron.log /01/countdown.log

CMD cron && tail -f /var/log/cron.log